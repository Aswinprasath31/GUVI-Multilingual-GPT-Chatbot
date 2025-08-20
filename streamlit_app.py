# app.py
import streamlit as st
from utils.translation import Translator
from utils.chatbot import ChatBot

st.set_page_config(page_title="GUVI Multilingual Chatbot", layout="wide")

st.title("🤖 GUVI Multilingual GPT Chatbot")
st.markdown("Talk to GUVI's AI assistant in **any Indian language**!")

translator = Translator()
chatbot = ChatBot(dataset_path="data/guvi_dataset_formatted.txt")

# Sidebar
st.sidebar.image("assets/guvi_logo.png", width=150)
selected_lang = st.sidebar.selectbox("Choose your language:", list(translator.LANGUAGE_CODES.keys()))

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

user_input = st.text_area("Your message:")

if st.button("Send"):
    if user_input.strip() == "":
        st.warning("Please enter a message.")
    else:
        english_text = translator.to_english(user_input, selected_lang)
        english_response = chatbot.get_response(english_text)
        final_response = translator.from_english(english_response, selected_lang)
        st.session_state['chat_history'].append((user_input, final_response))

if st.button("Clear Chat"):
    st.session_state['chat_history'] = []

for i, (user_msg, bot_msg) in enumerate(st.session_state['chat_history']):
    st.markdown(f"**You ({selected_lang}):** {user_msg}")
    st.markdown(f"**Bot ({selected_lang}):** {bot_msg}")
    st.markdown("---")
