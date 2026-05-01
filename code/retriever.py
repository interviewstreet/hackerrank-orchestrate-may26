from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class Retriever:
    def __init__(self, docs):
        self.docs = docs
        self.vectorizer = TfidfVectorizer()
        self.doc_vectors = self.vectorizer.fit_transform(docs)

    def search(self, query, k=1):
        q_vec = self.vectorizer.transform([query])
        sims = cosine_similarity(q_vec, self.doc_vectors)[0]

        top_indices = sims.argsort()[-k:][::-1]
        return [(self.docs[i], sims[i]) for i in top_indices]
