import streamlit as st
from pathlib import Path
import os
import cv2
import pandas as pd
from extraction_data import file_extract, displayPDF
from question_generator import Generator
st.set_page_config(page_title="Data Parser",layout="wide",page_icon="images.png")


col1, col2 = st.columns(2)

col1.header("Data Parser")

text = st.empty()
uploaded_files = col1.file_uploader('Upload your files',
 accept_multiple_files=True, type=['pdf','jpg','png','jpeg','csv'])
quest_input = col2.text_area("Enter your Question",height=200)

for file in uploaded_files:
    save_folder = 'pdfs'
    save_path = Path(save_folder, file.name)
    with open(save_path, mode='wb') as w:
        w.write(file.getvalue())
    path = os.path.join(save_folder,file.name)
    file_type = file.type
    
    if file_type=="application/pdf":
        pdf_display = displayPDF(save_path)
        st.markdown(pdf_display, unsafe_allow_html=True)
    elif file_type=="text/csv":
        df = pd.read_csv(path)
        col1.table(df)
    else:
        imag = cv2.imread(path)
        col1.image(imag)
    destination_path = f"pdfs/{file.name[:-4]}.txt"
    file_extract(file_path=path,file_type=file_type,destination_path=destination_path)
    if quest_input:
        message = Generator(quest_input ,destination_path)
        col2.text_area("Output",value=message["message"],height=400)
    else:
        col2.warning("Please enter a question")
    os.remove(destination_path)
    os.remove(path)