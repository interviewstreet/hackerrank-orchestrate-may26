from sentence_transformers import SentenceTransformer
from pathlib import Path
from typing import TypedDict, NotRequired, Literal
import numpy as np
import os

# data struct
class Data(TypedDict):
    title: str
    body: str
    id: str # filepath

# quert struct
class Query(TypedDict):
    issue: str
    company: Literal["hackerrank", "claude", "visa"]
    subject: NotRequired[str]

# class to create embeddings and ticket issue, company and if exist subject
class Embeddings:
    def __init__(self, model_name="all-MiniLM-L6-v2") -> None:
        self.model = SentenceTransformer(model_name)
        self.embeddings = None
        self.data = None
        self.data_embeddings_map = {}
        self.embeddings_path = Path("index/index.npy")

    # function the generate embeddings from a text
    def generate_embeddings(self, text: str):
        # chech if there is a text
        if text.strip() == "":
            raise ValueError("Generating embeddings requires text")
        embeddings = self.model.encode([text])
        return embeddings[0]

    # build embeddings for the data if not exist
    # data -> []{title: title of the document, body: rest of the document body}
    def build_embeddings(self, data: list[Data]):
        self.data = data
        # text to be encoded
        texts = []
        for d in data:
            self.data_embeddings_map[d["id"]] = d
            texts.append(f"{d['title']} {d['body']}")
        # create embeddigns for the whole documents passed
        self.embeddings = self.model.encode(texts, show_progress_bar=True)
        # create the embeddings file
        Path("./index").mkdir(exist_ok=True)
        with self.embeddings_path.open(mode="wb") as f:
            np.save(f, self.embeddings)
        return self.embeddings

    # load or create embeddings for data files
    def load_or_create_embeddings(self, data: list[Data]):
        self.data = data
        if os.path.exists(self.embeddings_path):
            # create the docmap
            for d in self.data:
                self.data_embeddings_map[d["id"]] = d
            with self.embeddings_path.open(mode="rb") as f:
                self.embeddings = np.load(f)
            if len(self.embeddings) == len(self.data):
                return self.embeddings
        return self.build_embeddings(data)

    # match with support tickets
    def match_support_ticket(self, query: Query, limit: int = 10) -> list[tuple[float, Data]]:
        # check if there are data
        if self.data is None:
            raise ValueError("No data to map")
        # check if embeddings exist
        if self.embeddings is None:
            raise ValueError("No embeddings are loaded!")
        # create embedding from the query
        query_text = f"{query["issue"]} {query['company']} {query.get('subject')}"
        query_embedding = self.generate_embeddings(query_text)
        
        # list to store similarities
        similarities = []
        # calculate the cosine similarty between the query embedding and the each data embedding
        for i in range(self.embeddings.shape[0]):
            score = cosine_similarity(query_embedding, self.embeddings[i])
            similarities.append((score, self.data[i]))
        # sort the similarities and return the result
        return sorted(similarities, key=lambda el: el[0], reverse=True)[:limit]

# function to calc cosine similarity between two vectors
def cosine_similarity(vec1, vec2):
    dot_product = np.dot(vec1, vec2)
    norm1 = np.linalg.norm(vec1)
    norm2 = np.linalg.norm(vec2)
    if norm1 == 0 or norm2 == 0:
        return 0.0
    return dot_product / (norm1 * norm2)
