"""Streamlit application entry point for AI Study Assistant."""

import streamlit as st
from services.pdf_reader import extract_text_from_pdf
from services.gemini_client import GeminiClient


# Configure the Streamlit page appearance.
st.set_page_config(page_title="AI Study Assistant", layout="wide")

# App title and description.
st.title("AI Study Assistant")
st.write(
    "Upload a PDF file and click Analyze PDF to generate a summary, key concepts, "
    "and exam questions."
)

# File uploader widget allows the user to select a PDF file.
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

# If a file is already uploaded, reset the file pointer to ensure reading starts at the beginning.
if uploaded_file is not None:
    uploaded_file.seek(0)

# Button to trigger PDF analysis.
analyze = st.button("Analyze PDF")

if analyze:
    # Validate that a PDF was uploaded before processing.
    if uploaded_file is None:
        st.warning("Please upload a PDF file before clicking Analyze PDF.")
    else:
        # Show a spinner while the app processes the PDF and the model request.
        with st.spinner("Analyzing PDF..."):
            try:
                uploaded_file.seek(0)
                document_text = extract_text_from_pdf(uploaded_file)
            except Exception as error:
                # If PDF reading fails, show an error and stop further processing.
                st.error(f"Failed to read PDF: {error}")
                document_text = ""

            if not document_text.strip():
                # Handle the case where extracted text is empty.
                st.error("No text could be extracted from the uploaded PDF.")
            else:
                try:
                    # Initialize the Gemini client using the environment API key.
                    client = GeminiClient()
                except ValueError as error:
                    st.error(str(error))
                    client = None

                if client:
                    # Generate all study materials from the extracted PDF text.
                    summary = client.generate_summary(document_text)
                    key_concepts = client.generate_key_concepts(document_text)
                    exam_questions = client.generate_exam_questions(document_text)

                    # Display results in three separate tabs.
                    tabs = st.tabs(["Summary", "Key Concepts", "Exam Questions"])

                    with tabs[0]:
                        st.subheader("Summary")
                        st.write(summary or "No summary generated.")

                    with tabs[1]:
                        st.subheader("Key Concepts")
                        st.write(key_concepts or "No key concepts generated.")

                    with tabs[2]:
                        st.subheader("Exam Questions")
                        st.write(exam_questions or "No exam questions generated.")
