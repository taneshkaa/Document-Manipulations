# PDF Parsing

# Converting word to pdf
from docx2pdf import convert
from PyPDF2 import PdfReader

# convert("Prac.docx")
convert("Prac.docx", "Prac1.pdf")
print("converted")
# path = 'C:\work@taneshka\TM\Document_Parsing\Practice.pdf'
path = '/Users/taneshkamehta/Documents/RPA/Document_Manipulations/Document_Parsing/General_Doc_Parsing/Practice.pdf'


reader = PdfReader(path)
meta = reader.metadata
print("Total Pages: ", len(reader.pages))

# Basic Document Information
# All of the following could be None!
print("Author: ", meta.author)
print("Creator: ", meta.creator)
print("Producer: ", meta.producer)
print("Subject: ", meta.subject)
print("Title: ", meta.title)

# Extracting Content based on Page Index
page = reader.pages[0]
print(page.extract_text())
content = page.extract_text()

# Spliting Content

# if "." in content:
#     x = content.split(".")
#     print(x)

# ____________________________________________________________________________________ #

# # Converting pdf to docx
# from pdf2docx import Converter
# import os

# # # # dir_path for input reading and output files & a for loop # # #

# path_input = 'C:\work@taneshka\dev\TM\Z_Prac\Document_Parsing'
# path_output = 'C:\work@taneshka\dev\TM\Z_Prac\Document_Parsing'

# for file in os.listdir(path_input):
#     cv = Converter(path_input)
#     cv.convert(path_output'.docx', start=0, end=None)
#     cv.close()
#     print(file)
