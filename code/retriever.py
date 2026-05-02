from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class Retriever:
    def __init__(self, chunks):
        self.chunks = chunks
        self.texts = [c["text"] for c in chunks]

        # 🔹 Better TF-IDF configuration
        self.vectorizer = TfidfVectorizer(
            stop_words="english",
            max_df=0.9,
            min_df=2,
            ngram_range=(1, 2)
        )

        # Fit once
        self.vectors = self.vectorizer.fit_transform(self.texts)

    def search(self, query, company, top_k=5):
        query = query.lower().strip()

        # 🔹 Filter by company
        filtered_idx = [
            i for i, c in enumerate(self.chunks)
            if c["company"] == company
        ]

        if not filtered_idx:
            return []

        filtered_vectors = self.vectors[filtered_idx]

        # 🔹 Transform query
        query_vec = self.vectorizer.transform([query])

        # 🔹 Compute similarity
        scores = cosine_similarity(query_vec, filtered_vectors)[0]

        # 🔥 Keyword boost
        keywords = set(query.split())
        boosted_scores = []

        for i, score in enumerate(scores):
            text = self.chunks[filtered_idx[i]]["text"]

            match_count = sum(1 for k in keywords if k in text)

            boosted = score + 0.05 * match_count
            boosted_scores.append(boosted)

        # 🔹 Sort top results
        top_indices = sorted(
            range(len(boosted_scores)),
            key=lambda i: boosted_scores[i],
            reverse=True
        )[:top_k]

        results = []
        for idx in top_indices:
            original_idx = filtered_idx[idx]

            results.append({
                "text": self.chunks[original_idx]["text"],
                "score": float(boosted_scores[idx]),
                "source": self.chunks[original_idx].get("source", "")
            })

        # 🔥 Intent filtering (VERY IMPORTANT)
        results = self.intent_filter(results, query)

        return results

    def intent_filter(self, results, query):
        query_words = set(query.split())

        strong_results = []

        for r in results:
            text = r["text"]

            match_count = sum(1 for w in query_words if w in text)

            # Require at least 2 keyword matches
            if match_count >= 2:
                strong_results.append(r)

        # fallback if filtering too strict
        return strong_results if strong_results else results