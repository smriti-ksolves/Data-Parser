import pytesseract
from pdf2image import convert_from_path
import os
import cv2
import base64
from dotenv import load_dotenv
load_dotenv()
pytesseract_path = os.getenv("PYTESSERACT_PATH")
pytesseract.pytesseract.tesseract_cmd = pytesseract_path


def file_extract(file_path,file_type,destination_path='pdfs/extracted.txt'):
    
    if file_type == "application/pdf":
    
        images = convert_from_path(file_path,
                                poppler_path = os.getenv("POPPLER_PATH") )
        for i in range(len(images)):
            images[i].save('page' + str(i) + '.jpg', 'JPEG')
            img = 'page' + str(i) + '.jpg'
            text = str(pytesseract.image_to_string(img))
            with open(f'{destination_path}','a') as f:
                f.write(text)
            os.remove(img)
    elif file_type=="text/csv":
        f = open(f'{file_path}')
        text = f.read()
        f.close()
        with open(f'{destination_path}','a') as f:
            f.write(text)
    else:
        img = cv2.imread(file_path)
        text = str(pytesseract.image_to_string(file_path))
        with open(f'{destination_path}','a') as f:
            f.write(text)
    

# pdf_extract("pdfs\SMRITI_RESUME.pdf")


def displayPDF(file):
    with open(file, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        pdf_display = F'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf">'
        return pdf_display