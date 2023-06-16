
from PIL import Image
import pytesseract
import streamlit as st
import os
import PyPDF2
from PIL import Image

def convert_pdf_to_images(pdf_path):
    images = []
    
    with open(pdf_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num] 
            page_data = page.extract_text()
            print(None)
            
            # Skip empty pages
            if not page_data:
                continue
            
            # Set a suitable DPI value for the image quality
            dpi = 300
            scale_factor = dpi / 72.0
            page_scale = (scale_factor, scale_factor)
            
            # Convert the PDF page to an image
            image = page.extract_images()[0]["image"]
            width, height = image["width"], image["height"]
            
            pil_image = Image.frombytes("RGB", (width, height), image["data"])
            pil_image = pil_image.resize((int(width*scale_factor), int(height*scale_factor)), Image.ANTIALIAS)
            
            images.append(pil_image)
    
    return images



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
                output_images = convert_pdf_to_images(temp_img_path)

                # Save the images
                for i, img in enumerate(output_images):
                    st.write(f"Page {i} :")
                    text = pytesseract.image_to_string(img, lang='tha')
                    st.write(text)
                
                

if __name__ == "__main__":
    main()