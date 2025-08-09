# utils/chatbot.py
from transformers import pipeline

class ChatBot:
    def __init__(self):
        print("Loading chatbot model...")
        # Replace with your fine-tuned GUVI GPT model hosted on HF
        self.model_name = "gpt2"
        self.generator = pipeline("text-generation", model=self.model_name, max_length=256, device=-1)

    def get_response(self, text):
        output = self.generator(text, max_length=200, do_sample=True, temperature=0.7)
        return output[0]['generated_text']
