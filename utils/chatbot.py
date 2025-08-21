# utils/chatbot.py
import os
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

class ChatBot:
    def __init__(self, model_name="gpt2", dataset_path="data/guvi_dataset_formatted.txt", device=None):
        # Load GPT-2 model + tokenizer
        self.tokenizer = GPT2Tokenizer.from_pretrained(model_name)
        self.model = GPT2LMHeadModel.from_pretrained(model_name)

        # Ensure pad token
        if self.tokenizer.pad_token is None:
            self.tokenizer.pad_token = self.tokenizer.eos_token

        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(self.device)

        # Load dataset into memory
        self.qa_pairs = self._load_dataset(dataset_path)

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

    def get_response(self, query: str, max_new_tokens=100) -> str:
        # Construct prompt from dataset + query
        # Few-shot style: include some examples
        prompt = ""
        for q, a in self.qa_pairs[:3]:  # take 3 samples for context
            prompt += f"User: {q}\nAssistant: {a}\n"
        prompt += f"User: {query}\nAssistant:"

        # Encode
        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.device)

        # Generate
        output_ids = self.model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            pad_token_id=self.tokenizer.eos_token_id,
            do_sample=True,
            top_p=0.9,
            temperature=0.7
        )

        output = self.tokenizer.decode(output_ids[0], skip_special_tokens=True)

        # Extract only assistant part
        if "Assistant:" in output:
            response = output.split("Assistant:")[-1].strip()
        else:
            response = output.strip()

        return response
