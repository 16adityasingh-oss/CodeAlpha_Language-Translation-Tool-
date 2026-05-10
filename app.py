# Translator.py

# Run this once in terminal:
# pip install streamlit groq python-dotenv

import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv

# ----------------------------
# LOAD ENV VARIABLES
# ----------------------------

load_dotenv()

# ----------------------------
# GROQ CLIENT
# ----------------------------

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# ----------------------------
# PAGE CONFIG
# ----------------------------

st.set_page_config(
    page_title="AI Language Translator",
    page_icon="🌍"
)

st.title("🌍 AI Language Translation Tool")

# ----------------------------
# LANGUAGE OPTIONS
# ----------------------------

languages = [
    "English",
    "Hindi",
    "French",
    "Spanish",
    "German",
    "Arabic",
    "Chinese",
    "Japanese",
    "Korean",
    "Russian",
    "Urdu"
]

# ----------------------------
# USER INPUT
# ----------------------------

text = st.text_area("Enter Text")

col1, col2 = st.columns(2)

with col1:
    source_lang = st.selectbox("Source Language", languages)

with col2:
    target_lang = st.selectbox("Target Language", languages)

# ----------------------------
# TRANSLATE BUTTON
# ----------------------------

if st.button("Translate"):

    if text.strip() == "":
        st.warning("Please enter some text.")

    else:

        prompt = f"""
        Translate the following text from {source_lang} to {target_lang}.

        Only return the translated text.
        Do not add explanations.

        Text:
        {text}
        """

        try:

            chat_completion = client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                model="llama-3.3-70b-versatile"
            )

            translated_text = chat_completion.choices[0].message.content

            st.subheader("Translated Text")
            st.success(translated_text)

            st.code(translated_text)

        except Exception as e:
            st.error(f"Error: {e}")