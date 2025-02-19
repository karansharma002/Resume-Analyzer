import streamlit as st
from extractors import extract_text
from scoring import evaluate_resume
from suggestions import generate_suggestions
from grammar import check_grammar

def main():
    st.title("AI-Powered Resume Analyzer 🔥")
    
    uploaded_file = st.file_uploader("Upload your resume (PDF/DOCX)", type=["pdf", "docx"])
    
    if uploaded_file:
        with st.spinner('Processing...'):
            text = extract_text(uploaded_file)
            score, ats_score = evaluate_resume(text)
            suggestions = generate_suggestions(text)
            grammar_issues = check_grammar(text)

        st.subheader("📄 Extracted Text:")
        st.text_area("Resume Content:", text, height=200)

        st.subheader("🎯 Resume Score:")
        st.write(f"Overall Score: {score}/100")
        st.write(f"ATS Compatibility: {ats_score}%")

        st.subheader("💡 AI Suggestions:")
        st.write(suggestions)

        st.subheader("📝 Grammar & Formatting Issues:")
        for issue in grammar_issues:
            st.write(f"- {issue}")

if __name__ == "__main__":
    main()
