
from PIL import Image
import pytesseract
import streamlit as st
import cv2
import os

def transcribe_image(image_path):
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img, lang='tha')
    return text


def main():
    st.title("Thai OCR Online")

    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])
    temp_img_path = os.path.join("images", uploaded_file.name)
    if uploaded_file is not None:
        with open((temp_img_path), "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        img = Image.open(temp_img_path)
        text = pytesseract.image_to_string(img, lang='tha')
        st.write(text)

if __name__ == "__main__":
    main()