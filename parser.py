from PyPDF2 import PdfReader
from docx import Document


def extract_text_from_pdf(file):
    reader = PdfReader(file)
    text = ""

    for page in reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted

    return text.lower()



def extract_text_from_docx(file):
    doc = Document(file)

    text = ""

    for para in doc.paragraphs:
        text += para.text + " "

    return text.lower()