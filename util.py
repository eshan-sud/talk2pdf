# util.py

import PyPDF2
import requests
from io import BytesIO

def extract_text_from_pdf(pdf_file):
    ''' Extracts text from a pdf file '''
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page_number in range(len(reader.pages)):
        text += reader.pages[page_number].extract_text()
    return text

def extract_text_from_url(url):
    ''' Extracts text from a web URL '''
    response = requests.get(url)
    pdf_file = BytesIO(response.content)
    return extract_text_from_pdf(pdf_file)

def display_loading_animation():
    pass
