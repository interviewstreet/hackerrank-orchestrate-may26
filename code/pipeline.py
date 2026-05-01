import csv
from pathlib import Path
from typing import Dict, List

from classifier import Classifier, ClassificationResult
from decision import Decision, DecisionEngine
from generator import Generator
from retrieval import RetrievalEngine, RetrievalHit
from utils import (
    append_run_log,
    build_ticket_id,
    ensure_directory,
    resolve_log_path,
    workspace_root,
)


OUTPUT_COLUMNS = ["status", "product_area", "response", "justification", "request_type"]


class TriagePipeline:
    def __init__(self, data_dir: Path) -> None:
        self.retrieval = RetrievalEngine(data_dir)
        self.classifier = Classifier()
        self.decision = DecisionEngine()
        self.generator = Generator()

    def process_row(self, row: Dict[str, str]) -> Dict[str, str]:
        classification = self.classifier.classify(row)
        hits = self.retrieval.search(
            ticket_text=classification.ticket_text,
            company=classification.company,
        )
        decision = self.decision.decide(
            ticket_text=classification.ticket_text,
            classification=classification,
            hits=hits,
        )
        product_area = self.classifier.product_area(
            classification=classification,
            hits=hits,
        )
        response = self.generator.generate_response(
            ticket_text=classification.ticket_text,
            decision=decision,
            hits=hits,
            product_area=product_area,
        )
        justification = self.generator.generate_justification(
            decision=decision,
            hits=hits,
            product_area=product_area,
        )
        return {
            "status": decision.status,
            "product_area": product_area,
            "response": response,
            "justification": justification,
            "request_type": classification.request_type,
        }

    def log_ticket(
        self,
        log_path: Path,
        row_index: int,
        row: Dict[str, str],
        classification: ClassificationResult,
        hits: List[RetrievalHit],
        decision: Decision,
        response: str,
        product_area: str,
    ) -> None:
        retrieved = ", ".join(hit.doc.path for hit in hits) if hits else "none"
        lines = [
            f"[TICKET] id={build_ticket_id(row, row_index)}",
            f"subject={classification.subject or '(empty)'}",
            f"company={classification.company}",
            f"request_type={classification.request_type}",
            f"product_area={product_area}",
            f"confidence={decision.confidence:.3f}",
            f"decision={decision.status}",
            f"reason={decision.reason_code}",
            f"retrieved_docs={retrieved}",
            f"response={response}",
            "",
        ]
        append_run_log(log_path, "\n".join(lines))


def run_pipeline(tickets_path: Path, data_dir: Path, output_path: Path, log_path: Path) -> None:
    root = workspace_root()
    safe_log_path = resolve_log_path(log_path, root)
    ensure_directory(output_path.parent)
    ensure_directory(safe_log_path.parent)

    pipeline = TriagePipeline(data_dir)
    with tickets_path.open("r", newline="", encoding="utf-8") as input_file:
        rows = list(csv.DictReader(input_file))

    with output_path.open("w", newline="", encoding="utf-8") as output_file:
        writer = csv.DictWriter(output_file, fieldnames=OUTPUT_COLUMNS)
        writer.writeheader()
        for row_index, row in enumerate(rows, start=1):
            classification = pipeline.classifier.classify(row)
            hits = pipeline.retrieval.search(classification.ticket_text, classification.company)
            decision = pipeline.decision.decide(classification.ticket_text, classification, hits)
            product_area = pipeline.classifier.product_area(classification, hits)
            response = pipeline.generator.generate_response(
                classification.ticket_text,
                decision,
                hits,
                product_area,
            )
            justification = pipeline.generator.generate_justification(decision, hits, product_area)
            writer.writerow(
                {
                    "status": decision.status,
                    "product_area": product_area,
                    "response": response,
                    "justification": justification,
                    "request_type": classification.request_type,
                }
            )
            pipeline.log_ticket(
                log_path=safe_log_path,
                row_index=row_index,
                row=row,
                classification=classification,
                hits=hits,
                decision=decision,
                response=response,
                product_area=product_area,
            )
