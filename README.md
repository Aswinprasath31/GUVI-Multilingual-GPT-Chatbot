# GUVI Multilingual GPT Chatbot

A smart multilingual chatbot that supports Indian languages using Hugging Face's translation and language models. It automatically detects the language of the user input, translates it to English, generates a response using a GPT model, and translates it back to the original language.

Built using **Streamlit**, **Hugging Face Transformers**, and **Torch**.

---

##  Features

-  **Auto Language Detection** (22+ Indian languages)
-  **Two-way Translation** using IndicTrans2
-  **GPT-based Conversational Model**
-  Built with **Streamlit**
-  Easy Deployment on Streamlit Cloud

---

##  Project Structure

```
guvi-multilingual-gpt-chatbot/
│
├── app.py                      # Streamlit app
├── requirements.txt            # Python dependencies
├── modules/                    # Modular components
│   ├── language_detection.py   # Language detection logic
│   ├── translation.py          # Translation class
│   ├── chatbot.py              # Chatbot class using GPT model
│   └── utils.py                # Helper functions & supported languages
```

---

##  Installation & Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Aswinprasath31/guvi-multilingual-gpt-chatbot.git
   cd guvi-multilingual-gpt-chatbot
   ```

2. **Create Virtual Environment (Optional)**
   ```bash
   python -m venv venv
   source venv/bin/activate   # or venv\Scripts\activate on Windows
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Streamlit App**
   ```bash
   streamlit run app.py
   ```

---

##  Model Info

-  GPT model used: `gpt2` (or fine-tuned version)
-  Translation model: [`ai4bharat/indictrans2-en-indic`](https://huggingface.co/ai4bharat/indictrans2-en-indic)

---

##  Deploy on Streamlit Cloud

1. Push code to **GitHub** (see below).
2. Go to [https://streamlit.io/cloud](https://streamlit.io/cloud).
3. Click **"New App"**, connect GitHub repo, and set `app.py` as the entry point.
4. Done 

---

##  Git Upload Instructions

1. **Initialize Git & Commit Files**
   ```bash
   git init
   git add .
   git commit -m "Initial commit - GUVI Multilingual Chatbot"
   ```

2. **Create GitHub Repo**

   - Go to [https://github.com/new](https://github.com/new)
   - Name it: `guvi-multilingual-gpt-chatbot`
   - Keep it public

3. **Connect Local Repo to GitHub**
   ```bash
   git remote add origin https://github.com/Aswinprasath31/guvi-multilingual-gpt-chatbot.git
   git branch -M main
   git push -u origin main
   ```

---

##  License

This project is for educational purposes as part of the **GUVI Final Project** submission.

---

##  Created By

**Aswin Prasath**  
Final Project – GUVI AI/ML / NLP  
LinkedIn: www.linkedin.com/in/aswinprasathv 
GitHub: https://github.com/Aswinprasath31