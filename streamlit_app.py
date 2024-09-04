import streamlit as st
from getimg_api import generate_image
from config import API_KEY

st.title("Text-to-Image Generator")

prompt = st.text_input("Enter your text prompt:", "")

if st.button("Generate Image"):
    try:
        image = generate_image(prompt, API_KEY)
        st.image(image)
    except Exception as e:
        st.error(str(e))
