# util.py

import pdfplumber
import requests
from io import BytesIO

def extract_text_from_pdf(pdf_file):
    ''' Extracts text from a PDF file '''
    text = ""
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text
    return text.strip()

def extract_text_from_url(url):
    ''' Extracts text from a web URL '''
    try:
        response = requests.get(url)
        response.raise_for_status()
        pdf_file = BytesIO(response.content)
        return extract_text_from_pdf(pdf_file)
    except requests.exceptions.RequestException as e:
        return f"Error fetching the PDF from URL: {e}"
