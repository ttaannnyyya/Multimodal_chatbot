# app.py

import streamlit as st
from PIL import Image
from utils import process_text_input, process_image_input
from google.generativeai import GenerativeModel

# Initialize the Gemini model
model = GenerativeModel("gemini-1.5-flash")

# Streamlit page settings
st.set_page_config(page_title="Multimodal Chatbot", layout="centered")
st.title("🧠📷 Multimodal Chatbot with Gemini")

# Session State for chat
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# User input form
with st.form(key="chat_form"):
    user_text = st.text_input("Enter your message:", key="user_text")
    uploaded_image = st.file_uploader("Upload an image (optional)", type=["png", "jpg", "jpeg"])
    submitted = st.form_submit_button("Send")

if submitted:
    if user_text:
        response_text = process_text_input(user_text, model)
        st.session_state.chat_history.append(("You", user_text))
        st.session_state.chat_history.append(("Bot", response_text))

    if uploaded_image:
        image = Image.open(uploaded_image)
        response_img = process_image_input(image, model)
        st.session_state.chat_history.append(("You (image)", image))
        st.session_state.chat_history.append(("Bot", response_img))

# Display chat history
for speaker, content in st.session_state.chat_history:
    if speaker.startswith("You") and isinstance(content, Image.Image):
        st.markdown(f"**{speaker}:**")
        st.image(content, width=300)
    else:
        st.markdown(f"**{speaker}:** {content}")
