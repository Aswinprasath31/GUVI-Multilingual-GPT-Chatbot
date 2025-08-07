# app.py

import streamlit as st
from modules.language_detection import detect_language
from modules.translation import Translator
from modules.chatbot import GUVIChatbot
from modules.utils import SUPPORTED_LANGUAGES, get_lang_display_name

st.set_page_config(page_title="GUVI Multilingual Chatbot", layout="wide")

# Sidebar: Info
with st.sidebar:
    st.title("🧑‍💻 GUVI Multilingual Chatbot")
    st.markdown(
        "Supports **22 Indian languages** with auto language detection.\n"
        "Powered by GPT and IndicTrans2."
    )
    st.write("---")
    st.markdown("👾 Visit [GUVI](https://www.guvi.in)")

# Load models (placeholders for session state)
if "translator" not in st.session_state:
    st.session_state["translator"] = Translator()
if "chatbot" not in st.session_state:
    st.session_state["chatbot"] = GUVIChatbot(model_name="gpt2")  # or your fine-tuned model

translator = st.session_state["translator"]
chatbot = st.session_state["chatbot"]

# UI Layout
st.header("💬 Chat with GUVI - in Your Language")
st.write("Type your question in any supported Indian language.")

col1, col2 = st.columns([2, 1])

with col1:
    user_input = st.text_area("Your Message", height=100, key="input_text")
    submit_btn = st.button("Send")

with col2:
    st.write("**Detected Language:**")
    detected_lang_code = detect_language(user_input) if user_input else "en"
    detected_lang = get_lang_display_name(detected_lang_code)
    st.markdown(f"`{detected_lang} ({detected_lang_code})`")

if submit_btn and user_input.strip():
    with st.spinner("Processing..."):

        # 1. Detect & translate input
        src_lang_code = detected_lang_code

        try:
            english_input = translator.translate_to_english(user_input, src_lang_code)
        except Exception as e:
            st.error("Translation to English failed.")
            st.stop()

        # 2. Pass to LLM in English
        try:
            response_en = chatbot.get_response(english_input)
        except Exception as e:
            st.error("Model failed to generate a response.")
            st.stop()

        # 3. Translate response back if needed
        try:
            final_reply = translator.translate_from_english(response_en, src_lang_code)
        except Exception as e:
            st.error("Translation from English failed.")
            st.stop()

        # 4. Display
        st.success("Chatbot Reply:")
        st.markdown(final_reply)
        st.caption(f"({get_lang_display_name(src_lang_code)})")

        # Show English response if needed
        with st.expander("Show English Response"):
            st.write(response_en)
else:
    st.info("Enter a message above and click **Send**.")

# Footer
st.write("---")
st.caption("Created for GUVI Final Project | Supports all major Indian languages 🌐")
