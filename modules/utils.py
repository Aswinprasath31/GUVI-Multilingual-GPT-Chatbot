SUPPORTED_LANGUAGES = {
    "as": "Assamese",
    "bn": "Bengali",
    "bodo": "Bodo", 
    "doi": "Dogri", 
    "en": "English",
    "gu": "Gujarati",
    "hi": "Hindi", 
    "kn": "Kannada",
    "ks": "Kashmiri", 
    "kok": "Konkani", 
    "mai": "Maithili",
    "ml": "Malayalam", 
    "mni": "Manipuri", 
    "mr": "Marathi",
    "ne": "Nepali",
    "or": "Odia",
    "pa": "Punjabi", 
    "sa": "Sanskrit", 
    "sat": "Santali", 
    "sd": "Sindhi", 
    "ta": "Tamil",
    "te": "Telugu", 
    "ur": "Urdu" 
}

def get_lang_display_name(lang_code):
    return SUPPORTED_LANGUAGES.get(lang_code, "Unknown")
