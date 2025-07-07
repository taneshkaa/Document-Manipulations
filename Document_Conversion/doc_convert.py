# PDF to WOrd File

from pdf2docx import Converter
import os.path
import pandas as pd

xls_file = 'doc_data.xlsx'
df = pd.read_excel(xls_file)

# File Name - shows the current file path and name
fl = df['File Name'].values.tolist()
# Output coulumns sets the new file name along with file type conversion(if no extention has been given it will simply sav file with name)
fl_out = df['Output'].values.tolist()

for idx, n in enumerate(fl):

    pdf_file = fl[idx]
    docx_file = fl_out[idx]

    cv = Converter(pdf_file)
    cv.convert(docx_file)
    cv.close()

# _____________________________________________________________________ #

# # Word to PDF 

# from docx2pdf import convert
# convert("output.docx", "Practice.pdf")    

# # Image to PDF

# from PIL import Image

# image = Image.open("input_image.jpg")
# pdf_path = "output1.pdf"

# # Convert RGB and save as PDF
# image.convert("RGB").save(pdf_path)


# # PDF to Text File
# import fitz  # PyMuPDF

# doc = fitz.open("Practice.pdf")
# text = ""

# for page in doc:
#     text += page.get_text()

# with open("output.txt", "w", encoding="utf-8") as f:
#     f.write(text)

# doc.close()