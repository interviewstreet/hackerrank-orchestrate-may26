#!/usr/bin/env python3
"""
Ticket Triage Agent - Core agent logic for resolving support tickets.

This module contains the core agent implementation that performs:
- Corpus loading and indexing
- Domain classification
- Request type detection  
- Risk assessment
- Semantic retrieval
- Response generation
- Escalation decision logic
"""

import csv
import re
from pathlib import Path
from typing import List, Dict, Tuple
from difflib import SequenceMatcher

# Keywords for domain and request type classification
HACKERRANK_KEYWORDS = ["test", "assessment", "coding", "candidate", "interview", "hackerrank", "screen", "recruiter", "score"]
CLAUDE_KEYWORDS = ["model", "prompt", "api", "response", "anthropic", "claude", "team", "workspace"]
VISA_KEYWORDS = ["payment", "card", "transaction", "charge", "refund", "visa", "merchant"]

ERROR_KEYWORDS = ["error", "not working", "broken", "fail", "crash", "down", "inaccessible", "doesn't work"]
FEATURE_KEYWORDS = ["add", "feature", "request", "improve", "would be nice", "could"]

RISK_HIGH = ["fraud", "unauthorized", "hack", "breach", "stolen"]
RISK_MEDIUM = ["payment", "charged", "refund", "invoice", "billing", "password", "locked out", "reset", "suspended", "gdpr", "data deletion", "legal"]


class TicketTriageAgent:
    """Main agent for triaging and responding to support tickets."""
    
    def __init__(self, data_dir: Path):
        """Initialize agent with corpus directory."""
        self.data_dir = data_dir
        self.corpus = []
        self._load_corpus()
    
    def _load_corpus(self) -> None:
        """Load and parse corpus from data directories."""
        for domain_dir in ["hackerrank", "claude", "visa"]:
            domain_path = self.data_dir / domain_dir
            if not domain_path.exists():
                continue
            
            # Walk through all subdirectories to find product areas
            for md_file in domain_path.rglob("*.md"):
                # Skip index files
                if md_file.name == "index.md":
                    continue
                
                # Determine product area from folder structure
                relative_path = md_file.relative_to(domain_path)
                parts = relative_path.parts[:-1]
                product_area = parts[0] if parts else "general"
                
                # Read and parse markdown content
                try:
                    with open(md_file, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # Split by headers if they exist
                    sections = re.split(r'^##\s+', content, flags=re.MULTILINE)
                    
                    for section in sections:
                        if section.strip():
                            self.corpus.append({
                                "domain": domain_dir,
                                "product_area": product_area,
                                "text": section.strip(),
                                "path": str(md_file.relative_to(self.data_dir))
                            })
                except Exception as e:
                    print(f"Warning: Error reading {md_file}: {e}")
    
    def get_corpus_stats(self) -> Dict:
        """Get corpus statistics."""
        stats = {"total_chunks": len(self.corpus)}
        for domain in ["hackerrank", "claude", "visa"]:
            stats[f"{domain}_chunks"] = sum(1 for c in self.corpus if c["domain"] == domain)
        return stats
    
    @staticmethod
    def _preprocess_text(text: str) -> str:
        """Normalize and clean text."""
        return text.lower().strip()
    
    def classify_domain(self, issue: str, subject: str, company: str) -> str:
        """Classify the domain based on company field and keywords."""
        if company and company.strip():
            company_lower = company.lower().strip()
            if "hackerrank" in company_lower:
                return "hackerrank"
            elif "claude" in company_lower or "anthropic" in company_lower:
                return "claude"
            elif "visa" in company_lower:
                return "visa"
            else:
                return "unknown"
        
        # Fallback to keyword matching
        combined_text = self._preprocess_text(f"{issue} {subject}")
        
        hackerrank_score = sum(1 for kw in HACKERRANK_KEYWORDS if kw in combined_text)
        claude_score = sum(1 for kw in CLAUDE_KEYWORDS if kw in combined_text)
        visa_score = sum(1 for kw in VISA_KEYWORDS if kw in combined_text)
        
        max_score = max(hackerrank_score, claude_score, visa_score)
        if max_score == 0:
            return "unknown"
        
        # Tie-breaking: prefer claude > visa > hackerrank
        if claude_score == max_score:
            return "claude"
        elif visa_score == max_score:
            return "visa"
        elif hackerrank_score == max_score:
            return "hackerrank"
        
        return "unknown"
    
    @staticmethod
    def classify_request_type(issue: str, subject: str) -> str:
        """Classify the request type (bug, feature_request, product_issue, invalid)."""
        combined_text = TicketTriageAgent._preprocess_text(f"{issue} {subject}")
        
        if not combined_text or combined_text.strip() == "":
            return "invalid"
        
        has_error = any(e in combined_text for e in ERROR_KEYWORDS)
        has_feature = any(f in combined_text for f in FEATURE_KEYWORDS)
        
        if has_feature and not has_error:
            return "feature_request"
        elif has_error:
            return "bug"
        else:
            return "product_issue"
    
    @staticmethod
    def detect_risk(issue: str, subject: str) -> str:
        """Detect risk level (HIGH, MEDIUM, LOW)."""
        combined_text = TicketTriageAgent._preprocess_text(f"{issue} {subject}")
        
        if any(risk in combined_text for risk in RISK_HIGH):
            return "HIGH"
        elif any(risk in combined_text for risk in RISK_MEDIUM):
            return "MEDIUM"
        else:
            return "LOW"
    
    @staticmethod
    def _keyword_overlap(text1: str, text2: str) -> float:
        """Calculate keyword overlap between two texts."""
        words1 = set(text1.lower().split())
        words2 = set(text2.lower().split())
        
        if not words1 or not words2:
            return 0.0
        
        overlap = len(words1 & words2)
        return overlap / max(len(words1), len(words2))
    
    @staticmethod
    def _fuzzy_partial_ratio(text1: str, text2: str) -> float:
        """Calculate fuzzy partial ratio for string similarity."""
        text1_lower = text1.lower()
        text2_lower = text2.lower()
        
        matcher = SequenceMatcher(None, text1_lower, text2_lower)
        return matcher.ratio()
    
    def retrieve_chunks(self, issue: str, subject: str, domain: str, top_k: int = 3) -> Tuple[List[Dict], float]:
        """Retrieve most relevant chunks from corpus."""
        combined_text = self._preprocess_text(f"{issue} {subject}")
        
        # Filter by domain
        filtered_corpus = [c for c in self.corpus if c["domain"] == domain]
        
        if not filtered_corpus:
            return [], 0.0
        
        # Score and rank chunks
        scores = []
        for chunk in filtered_corpus:
            chunk_text = self._preprocess_text(chunk["text"])
            
            overlap = self._keyword_overlap(combined_text, chunk_text)
            fuzzy = self._fuzzy_partial_ratio(combined_text, chunk_text)
            
            score = overlap + 0.5 * fuzzy
            scores.append((chunk, score))
        
        # Sort by score
        scores.sort(key=lambda x: x[1], reverse=True)
        
        # Select top chunks with minimum threshold and unique paths
        threshold = 0.15
        selected = []
        seen_paths = set()
        
        for chunk, score in scores:
            if score < threshold:
                break
            if chunk["path"] not in seen_paths:
                selected.append(chunk)
                seen_paths.add(chunk["path"])
            if len(selected) >= top_k:
                break
        
        # Calculate confidence: average of top scores
        if len(scores) >= 3:
            top_scores = [s[1] for s in scores[:3]]
            confidence = sum(top_scores) / len(top_scores)
        elif scores:
            confidence = scores[0][1]
        else:
            confidence = 0.0
        
        return selected, confidence
    
    @staticmethod
    def _is_response_grounded(response: str, chunks: List[Dict]) -> bool:
        """Verify response is grounded in corpus (prevents hallucination).
        
        Returns True only if response contains substantial overlap with corpus text.
        """
        if not chunks or not response:
            return False
        
        # Get all corpus text
        corpus_text = " ".join([c["text"] for c in chunks]).lower()
        response_lower = response.lower()
        
        # Check for key phrases from corpus appearing in response
        # At least 40% of response content must be from corpus
        response_words = set(response_lower.split())
        corpus_words = set(corpus_text.split())
        
        if not response_words:
            return False
        
        overlap = len(response_words & corpus_words) / len(response_words)
        return overlap >= 0.40  # 40% threshold ensures grounding
    
    @staticmethod
    def generate_response(chunks: List[Dict], request_type: str, product_area: str) -> str:
        """Generate response based on retrieved chunks (grounded in corpus)."""
        if not chunks:
            return "Unable to find relevant information in our knowledge base. Please contact support for further assistance."
        
        # Structure response with summary and steps
        parts = []
        
        # Add summary from first chunk (first sentence)
        first_text = chunks[0]["text"].strip()
        sentences = first_text.split(".")[:1]
        if sentences:
            summary = sentences[0].strip() + "."
            if summary:
                parts.append(f"Summary: {summary}")
        
        # Add structured content from chunks
        for i, chunk in enumerate(chunks[:2], 1):
            text = chunk["text"].strip()
            # Take first 300 chars to avoid too much duplication
            if len(text) > 300:
                text = text[:300].rsplit(" ", 1)[0] + "..."
            parts.append(f"Point {i}: {text}")
        
        combined_response = "\n\n".join(parts)
        
        # Final truncate if still too long
        if len(combined_response) > 800:
            combined_response = combined_response[:800] + "..."
        
        # Verify response is grounded in corpus
        if not TicketTriageAgent._is_response_grounded(combined_response, chunks):
            return "Unable to provide a reliable answer based on available documentation. Please contact support."
        
        return combined_response
    
    @staticmethod
    def decide_status(risk: str, confidence: float, request_type: str) -> str:
        """Decide whether to reply or escalate."""
        # Force escalate invalid requests
        if request_type == "invalid":
            return "Escalated"
        
        # Escalate high-risk tickets
        if risk == "HIGH":
            return "Escalated"
        
        # Escalate if confidence too low to provide reliable answer
        if confidence < 0.15:
            return "Escalated"
        
        # For medium-risk, be more conservative (escalate unless high confidence)
        if risk == "MEDIUM" and confidence < 0.30:
            return "Escalated"
        
        # Otherwise reply if we have reasonable confidence
        return "Replied"
    
    def process_ticket(self, issue: str, subject: str, company: str) -> Dict:
        """Process a single support ticket and return result."""
        # Step 3: Domain classification
        domain = self.classify_domain(issue, subject, company)
        
        # Step 4: Request type classification
        request_type = self.classify_request_type(issue, subject)
        
        # Step 5: Risk detection
        risk = self.detect_risk(issue, subject)
        
        # Step 6: Retrieval
        chunks, confidence = self.retrieve_chunks(issue, subject, domain)
        
        # Fallback: if no chunks found and domain is unknown, try all domains
        if not chunks and domain == "unknown":
            for fallback_domain in ["hackerrank", "claude", "visa"]:
                chunks, confidence = self.retrieve_chunks(issue, subject, fallback_domain)
                if chunks:
                    domain = fallback_domain
                    break
        
        # Extract product area from chunks or use "unknown" as default
        product_area = chunks[0]["product_area"] if chunks else "unknown"
        
        # Generate response
        response = self.generate_response(chunks, request_type, product_area)
        
        # Safety check: Verify response is grounded
        # If we can't verify grounding, escalate to be safe
        is_grounded = self._is_response_grounded(response, chunks)
        if not is_grounded and chunks:
            # Response quality is poor, escalate
            confidence = 0.0
            response = "Unable to provide a reliable answer based on available documentation. Please contact support."
        
        # Step 7: Decision logic
        status = self.decide_status(risk, confidence, request_type)
        
        # Additional safety: if response suggests escalation, honor it
        if "contact support" in response.lower() and "please" in response.lower():
            # Fallback message suggests we should escalate
            if status == "Replied" and confidence < 0.20:
                status = "Escalated"
        
        # Build detailed justification
        reason_parts = []
        if request_type == "invalid":
            reason_parts.append("invalid_request")
        if risk == "HIGH":
            reason_parts.append("high_risk")
        if confidence < 0.15:
            reason_parts.append("low_confidence")
        if risk == "MEDIUM" and confidence < 0.30:
            reason_parts.append("medium_risk_low_confidence")
        if not is_grounded and chunks:
            reason_parts.append("grounding_check_failed")
        
        reason = "; ".join(reason_parts) if reason_parts else "sufficient_confidence"
        justification = f"Domain:{domain}|Type:{request_type}|Risk:{risk}|Confidence:{confidence:.2f}|Reason:{reason}"
        
        return {
            "Status": status,
            "Product_Area": product_area,
            "Response": response,
            "Justification": justification,
            "Request_Type": request_type
        }
