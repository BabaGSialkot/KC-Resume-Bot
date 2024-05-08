import streamlit as st
from PIL import Image
import pytesseract

# Function to extract text from image
def extract_text_from_image(image):
    try:
        # Convert the image to text
        text = pytesseract.image_to_string(image)
    except Exception as e:
        text = f"Failed to extract text due to an error: {str(e)}"
    return text

def main():
    st.title("Resume Modifier for Data Science")

    

    # Resume upload
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Resume', use_column_width=True)
        
        # Extract text from image
        resume_text = extract_text_from_image(image)
        st.text_area("Extracted Text from Resume", resume_text, height=150)

    # Prompt generation (static since the role is fixed as 'Data Scientist' for this example)
    if st.button("Generate Modification Prompt for Data Science"):
        if uploaded_file:
            prompt = f"Modify the following resume to better fit the job category 'Data Scientist': {resume_text}"
            st.text_area("Modification Prompt", prompt, height=150)
        else:
            st.error("Please upload a resume to generate the prompt.")

if __name__ == "__main__":
    main()
