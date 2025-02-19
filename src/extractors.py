import pdfplumber
import docx2txt
import io

def extract_text(file):
    if file.type == "application/pdf":
        with pdfplumber.open(io.BytesIO(file.read())) as pdf:
            text = "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])
    elif file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        text = docx2txt.process(io.BytesIO(file.read()))
    else:
        text = ""
    return text.strip()
