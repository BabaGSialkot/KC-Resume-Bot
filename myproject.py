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

# Function to generate a modification prompt based on the job category and the extracted resume content
def generate_prompt(resume_text, job_category):
    prompt = f"Modify the following resume to better fit the job category '{job_category}': {resume_text}"
    return prompt

def main():
    # Set a background image
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url("https://example.com/background.jpg");
            background-size: cover;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    st.title("Interactive Resume Modifier")

    # Resume upload
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        try:
            image = Image.open(uploaded_file)
            st.image(image, caption='Uploaded Resume', use_column_width=True)
            
            # Extract text from image
            resume_text = extract_text_from_image(image)
            st.text_area("Extracted Text from Resume", resume_text, height=150)
        except Exception as e:
            st.error("Please upload a valid image file.")

    # Job category input
    job_categories = [
        "Software Developer", "System Analyst", "IT Project Manager", "Network Engineer",
        "Database Administrator", "Cybersecurity Specialist", "Data Scientist", "AI Engineer",
        "DevOps Engineer", "Product Manager", "UI/UX Designer", "Technical Support"
    ]
    job_category = st.selectbox("Select Job Category", job_categories)
    
    if st.button("Generate Modification Prompt"):
        # Generate modification prompt
        if uploaded_file and 'resume_text' in locals():
            prompt = generate_prompt(resume_text, job_category)
            st.text_area("Modification Prompt", prompt, height=150)
        else:
            st.error("Please upload a resume and extract the text to generate a prompt.")

if __name__ == "__main__":
    main()
