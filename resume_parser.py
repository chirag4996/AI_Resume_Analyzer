#from PyPDF2 import PdfReader

#def extract_text(uploaded_file):
 #   reader = PdfReader(uploaded_file)

  #  text=""

   # for page in reader.pages:
    #    page_text = page.extract_text()

     #   if page_text:
      #      text += page_text
            
            
    #return text


from PyPDF2 import PdfReader
import re

def extract_text(uploaded_file):
    reader = PdfReader(uploaded_file)

    text=""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text
    return text

def extract_email(text):
    email= re.findall(r'[\w\.-]+@[\w\.-]+\.\w+',text)
    if email:
        return email[0]

    return"Not Found"

def extract_phone(text):
    phone = re.findall(r'\+?\d[\d\s\-]{8,}\d',text)

    if phone:
        return phone[0]

    return"Not Found"

def extract_name(text):
    lines = text.split("\n")

    for line in lines:
        if len(line.split()) <= 4:
            return line

    return"Not Found"