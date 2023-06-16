
from PIL import Image
import pytesseract
import streamlit as st
import os
from pdf2image import convert_from_path
from PIL import Image


def main():
    st.title("Thai OCR Online")
    st.write("support image files jpg, png, jpeg, pdf")
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg", "pdf"])
    if uploaded_file is not None:
        temp_img_path = os.path.join("images", uploaded_file.name)
        file_type = uploaded_file.name.split(".")[-1]
        with open((temp_img_path), "wb") as f:
            f.write(uploaded_file.getbuffer())
            
        st.write(f"file type detect : {file_type}")
        if file_type in ["jpg", "png", "jpeg"]:
            with st.spinner("Transcribing Image .."):
                img = Image.open(temp_img_path)
                text = pytesseract.image_to_string(img, lang='tha')
                st.write(text)
        
        elif file_type in ["pdf"]:
            with st.spinner("Transcribing PDF .."):
                # Example usage
                images = convert_from_path(temp_img_path)

                for i in range(len(images)):
                    st.write(f"Page {i} :")
                    text = pytesseract.image_to_string(images[i], lang='tha')
                    st.success(text)
                

if __name__ == "__main__":
    main()