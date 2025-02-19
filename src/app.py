# app.py - Main Streamlit application
import streamlit as st
from scoring.py import calculate_resume_score
from extractors.py import extract_text_from_pdf, extract_text_from_docx
from suggestions.py import generate_suggestions

def main():
    st.title("AI-Powered Resume Analyzer")
    uploaded_file = st.file_uploader("Upload Resume (PDF/DOCX)", type=["pdf", "docx"])
    
    if uploaded_file:
        file_extension = uploaded_file.name.split(".")[-1].lower()
        if file_extension == "pdf":
            extracted_text = extract_text_from_pdf(uploaded_file)
        else:
            extracted_text = extract_text_from_docx(uploaded_file)
        
        st.subheader("Extracted Text:")
        st.text(extracted_text)
        
        score = calculate_resume_score(extracted_text)
        st.subheader("Resume Score:")
        st.write(f"Your resume score is: {score}/100")
        
        suggestions = generate_suggestions(extracted_text)
        if suggestions:
            st.subheader("AI Suggestions:")
            for suggestion in suggestions:
                st.write(f"- {suggestion}")

if __name__ == "__main__":
    main()
