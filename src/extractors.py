# extractors.py - Extract text from PDF and DOCX
import pdfplumber
import docx2txt

def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = "".join([page.extract_text() or "" for page in pdf.pages])
    return text

def extract_text_from_docx(docx_path):
    return docx2txt.process(docx_path)