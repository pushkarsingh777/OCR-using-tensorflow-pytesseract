import streamlit as st
from model import extract_text_from_image
from PIL import Image
import os

st.title("OCR App")
st.write("Upload an image to extract text")

uploaded_file = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg", "webp"])

if uploaded_file is not None:
   
    with open("temp_image.jpg", "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

    text = extract_text_from_image("temp_image.jpg")

    st.subheader("Extracted Text:")
    st.text_area("Result", text, height=300)

    os.remove("temp_image.jpg")
