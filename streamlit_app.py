# app.py
import streamlit as st
from transformers import pipeline

# -------------------------
# CONFIG
# -------------------------
st.set_page_config(page_title="GUVI Multilingual Chatbot", layout="wide")
st.title("🤖 GUVI Multilingual GPT Chatbot")
st.markdown("Talk to GUVI's AI assistant in **any Indian language**!")

# -------------------------
# Load Models (cached on Hugging Face CPU)
# -------------------------
@st.cache_resource
def load_translation_pipelines():
    to_en = pipeline("translation", model="Helsinki-NLP/opus-mt-mul-en")   # many-to-English
    from_en = pipeline("translation", model="Helsinki-NLP/opus-mt-en-mul") # English-to-many
    return to_en, from_en

@st.cache_resource
def load_chatbot_pipeline():
    return pipeline("text-generation", model="microsoft/DialoGPT-medium")

to_en, from_en = load_translation_pipelines()
chatbot = load_chatbot_pipeline()

# -------------------------
# Sidebar
# -------------------------
LANGUAGE_CODES = {
    "Tamil": "ta",
    "Hindi": "hi",
    "Telugu": "te",
    "Malayalam": "ml",
    "Kannada": "kn",
    "Gujarati": "gu",
    "Bengali": "bn",
    "Marathi": "mr",
    "English": "en"
}
st.sidebar.image("assets/guvi_logo.png", width=150)
selected_lang = st.sidebar.selectbox("Choose your language:", list(LANGUAGE_CODES.keys()))

# -------------------------
# Session State
# -------------------------
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# -------------------------
# Chat Input
# -------------------------
user_input = st.text_area("Your message:")

if st.button("Send"):
    if user_input.strip() == "":
        st.warning("Please enter a message.")
    else:
        # Step 1: Translate user message to English
        if selected_lang != "English":
            english_text = to_en(user_input)[0]['translation_text']
        else:
            english_text = user_input

        # Step 2: Get chatbot response in English
        english_response = chatbot(english_text, max_length=200, pad_token_id=50256)[0]['generated_text']

        # Step 3: Translate back to user language
        if selected_lang != "English":
            final_response = from_en(english_response)[0]['translation_text']
        else:
            final_response = english_response

        # Save history
        st.session_state['chat_history'].append((user_input, final_response))

if st.button("Clear Chat"):
    st.session_state['chat_history'] = []

# -------------------------
# Display chat history
# -------------------------
for i, (user_msg, bot_msg) in enumerate(st.session_state['chat_history']):
    st.markdown(f"**You ({selected_lang}):** {user_msg}")
    st.markdown(f"**Bot ({selected_lang}):** {bot_msg}")
    st.markdown("---")
