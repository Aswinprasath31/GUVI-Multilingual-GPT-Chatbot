# utils/chatbot.py
import os
import pandas as pd
from sentence_transformers import SentenceTransformer, util

class ChatBot:
    def __init__(self, dataset_path="data/guvi_dataset_formatted.txt"):
        # Load embedding model
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        
        # Load dataset
        self.qa_pairs = self._load_dataset(dataset_path)
        
        # Precompute embeddings
        self.corpus_embeddings = self.model.encode(
            [q for q, _ in self.qa_pairs], convert_to_tensor=True
        )

    def _load_dataset(self, dataset_path):
        qa_pairs = []
        with open(dataset_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        for line in lines:
            if "<|user|>" in line and "<|assistant|>" in line:
                q = line.split("<|user|>")[1].split("<|assistant|>")[0].strip()
                a = line.split("<|assistant|>")[1].strip()
                qa_pairs.append((q, a))
        return qa_pairs

    def get_response(self, query: str) -> str:
        # Encode user query
        query_embedding = self.model.encode(query, convert_to_tensor=True)
        
        # Find closest match
        hits = util.semantic_search(query_embedding, self.corpus_embeddings, top_k=1)
        best_idx = hits[0][0]['corpus_id']
        best_score = hits[0][0]['score']

        if best_score > 0.65:  # th_
