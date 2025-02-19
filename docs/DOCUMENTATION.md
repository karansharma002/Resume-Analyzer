# AI-Powered Resume Analyzer Documentation

## 📌 Project Overview
The AI-Powered Resume Analyzer is an intelligent tool designed to analyze resumes and evaluate an applicant's skills, experience, and ATS (Applicant Tracking System) compatibility. It is beneficial for both recruiters and job seekers to create a strong resume.

## 🚀 Features
- **Resume Text Extraction** – Extracts text from PDF and DOCX formats.
- **Skill & Soft Skills Detection** – Identifies technical and soft skills from resumes.
- **Resume Scoring** – AI-powered scoring system to evaluate resumes.
- **ATS Compatibility Check** – Provides a percentage score indicating ATS friendliness.
- **AI-Based Suggestions** – Offers recommendations to improve the resume.
- **Grammar Check** – Detects language mistakes and grammatical errors.

## 📥 Installation Guide
1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/resume-analyzer.git
   cd resume-analyzer
   ```
   
2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   **Additional Requirements:**
    ```bash
    Java is required for language-tool-python (Grammar Check).
    Spacy models: Run python -m spacy download en_core_web_sm after installation.
    ```

3. **Run the Application**
   ```bash
   streamlit run app.py
   ```

## 📝 Usage Guide
1. **Open the Application** – Once the Streamlit server starts, it will open in your browser.
2. **Upload a Resume** – Upload a resume in PDF or DOCX format.
3. **View Results** – See extracted text, detected skills, resume score, ATS score, AI suggestions, and grammar checks.

## 🏗 Code Structure
```
resume-analyzer/
│── app.py  # Main Streamlit application
│── extractors.py  # Functions for text extraction (PDF/DOCX)
│── scoring.py  # Resume scoring logic
│── suggestions.py  # AI-based recommendations
│── requirements.txt  # Dependencies
└── README.md  # Project overview
```

## 🤝 Contribution Guide
1. **Fork the Repository** and clone it to your local system.
2. **Add New Features** or fix bugs.
3. **Raise a Pull Request** for review and approval.

## 📜 License & Credits
- **License** – MIT License
- **Credits** – This project utilizes open-source tools such as Streamlit, pdfplumber, docx2txt, spaCy, and language_tool_python.

If you encounter any issues or have feature requests, please post them in the GitHub issues section. 🚀
