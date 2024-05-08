import streamlit as st
from PIL import Image
import pytesseract

# Function to extract text from an image
def extract_text_from_image(image):
    # Convert the image to text
    text = pytesseract.image_to_string(image)
    return text

# Function to generate a modification prompt based on the job category and the extracted resume content
def generate_prompt(resume_text, job_category):
    prompt = f"Modify the following resume to better fit the job category '{job_category}': {resume_text}"
    return prompt

def main():
    st.title("Resume Modifier")

    # Resume upload
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Resume', use_column_width=True)
        
        # Extract text from image
        resume_text = extract_text_from_image(image)
        st.text_area("Extracted Text from Resume", resume_text, height=150)

        # Job category input
        job_category = st.selectbox("Select Job Category", ["Software Development", "Human Resources", "Marketing", "Sales", "Data Science"])
        
        if st.button("Generate Modification Prompt"):
            # Generate modification prompt
            prompt = generate_prompt(resume_text, job_category)
            st.text_area("Modification Prompt", prompt, height=150)

if __name__ == "__main__":
    main()
