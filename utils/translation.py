# utils/translation.py
from transformers import pipeline
from langdetect import detect

LANGUAGE_CODES = {
    "Hindi": "hin_Deva",
    "Tamil": "tam_Taml",
    "Telugu": "tel_Telu",
    "Bengali": "ben_Beng",
    "Malayalam": "mal_Mlym",
    "Kannada": "kan_Knda",
    "Gujarati": "guj_Gujr",
    "Punjabi": "pan_Guru",
    "Marathi": "mar_Deva",
    "Odia": "ory_Orya",
    "Assamese": "asm_Beng",
    "Urdu": "urd_Arab",
    "English": "eng_Latn"
}

class Translator:
    def __init__(self):
        self.model_en_to_indic = "ai4bharat/indictrans2-en-indic-1B"
        self.model_indic_to_en = "ai4bharat/indictrans2-indic-en-1B"
        print("Loading translation models...")
        self.translator_to_indic = pipeline("translation", model=self.model_en_to_indic, device=-1, trust_remote_code=True)
        self.translator_to_english = pipeline("translation", model=self.model_indic_to_en, device=-1, trust_remote_code=True)

    def detect_language(self, text):
        try:
            return detect(text)
        except:
            return "en"

    def to_english(self, text, source_lang):
        if source_lang == "English":
            return text
        return self.translator_to_english(
            text,
            src_lang=LANGUAGE_CODES[source_lang],
            tgt_lang="eng_Latn"
        )[0]['translation_text']

    def from_english(self, text, target_lang):
        if target_lang == "English":
            return text
        return self.translator_to_indic(
            text,
            src_lang="eng_Latn",
            tgt_lang=LANGUAGE_CODES[target_lang]
        )[0]['translation_text']
