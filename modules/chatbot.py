from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

class GUVIChatbot:
    def __init__(self, model_name="gpt2"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)

    def get_response(self, input_text):
        inputs = self.tokenizer.encode(input_text + self.tokenizer.eos_token, return_tensors="pt")
        outputs = self.model.generate(inputs, max_length=100, pad_token_id=self.tokenizer.eos_token_id)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)
