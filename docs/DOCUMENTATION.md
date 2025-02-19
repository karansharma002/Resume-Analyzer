# AI-Powered Resume Analyzer Documentation

## 📌 Project Overview
AI-Powered Resume Analyzer is a smart tool that analyzes resumes and evaluates an applicant's skills, experience, and ATS compatibility. It is useful for both recruiters and job seekers to build a strong resume.

## 🚀 Features
- **Resume Text Extraction** – Extracts text from PDF and DOCX formats.
- **Skill & Soft Skills Detection** – Identifies technical and soft skills from resumes.
- **Resume Scoring** – AI-based scoring system evaluates resumes.
- **ATS Compatibility Check** – Determines the resume's ATS-friendliness percentage.
- **AI-Based Suggestions** – Provides resume improvement tips.
- **Grammar Check** – Detects language mistakes.

## 💚 Code Structure
```
resume-analyzer/
│── app.py            # Main Streamlit application (UI + integration)
│── extractors.py     # Handles text extraction from PDF/DOCX
│── scoring.py        # Resume scoring logic
│── suggestions.py    # AI-based recommendations for resume improvements
│── grammar_check.py  # Grammar & spell checking
│── requirements.txt  # Dependencies
└── README.md         # Project overview & usage guide
```

## 👅 Installation Guide
1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/resume-analyzer.git
   cd resume-analyzer
   ```
2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the Application**
   ```bash
   streamlit run app.py
   ```

## 📝 Usage Guide
1. **Open the App** – Once the Streamlit server starts, the browser will open automatically.
2. **Upload a Resume** – Upload a resume in PDF or DOCX format.
3. **View Results** – See extracted text, detected skills, resume score, ATS score, AI suggestions, and grammar checks.

## 🛠️ Contribution Guide
1. **Fork the Repository** and clone it to your local system.
2. **Add New Features** or fix bugs.
3. **Raise a Pull Request** for review.

## 🐝 License & Credits
- **License** – MIT License
- **Credits** – This project utilizes open-source libraries such as Streamlit, pdfplumber, docx2txt, spaCy, and language_tool_python.

If you have any issues or feature requests, please post them in the GitHub issues section. 🚀

