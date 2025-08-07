from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

class Translator:
    def __init__(self):
        model_name = "ai4bharat/indictrans2-en-indic"
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    def translate_to_english(self, text, src_lang):
        input_text = f"{src_lang}>>eng<<{text}"
        inputs = self.tokenizer(input_text, return_tensors="pt")
        output = self.model.generate(**inputs)
        return self.tokenizer.decode(output[0], skip_special_tokens=True)

    def translate_from_english(self, text, tgt_lang):
        input_text = f"eng>>{tgt_lang}<<{text}"
        inputs = self.tokenizer(input_text, return_tensors="pt")
        output = self.model.generate(**inputs)
        return self.tokenizer.decode(output[0], skip_special_tokens=True)
