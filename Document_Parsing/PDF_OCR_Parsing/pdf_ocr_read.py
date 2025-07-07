# Complete Document Extraction

from pdf2image import convert_from_path
import easyocr
import pandas as pd
import os

xls_file = 'doc_data.xlsx'
df = pd.read_excel(xls_file)

olf = df['File Name'].values.tolist()

for idx, n in enumerate(olf):
    pdf_path = str(olf[idx])
    poppler_path = r'C:\poppler-24.08.0\Library\bin'
    output_excel = "%s.xlsx" %str(olf[idx])
    # Convert PDF to images
    pages = convert_from_path(pdf_path, poppler_path=poppler_path)
    # Initialize OCR reader
    reader = easyocr.Reader(['en'])  # Add 'hi' if needed
    # Store results
    data = []
    for i, page in enumerate(pages):
        image_path = f"_page_{i+1}.png"
        page.save(image_path, "PNG")
        print(f"Processing page {i+1}...")
        result = reader.readtext(image_path, detail=0)  # Returns list of text lines
        for line in result:
            data.append({'Page': i + 1, 'Text': line})
    # Save to Excel
    df = pd.DataFrame(data)
    df.to_excel(output_excel, index=False)
    print(f"✅ OCR complete. Text saved to: {output_excel}")


 
## ---- Name and Address ---- ##

# import easyocr
# import re
# import pandas as pd
# # 1. Load the image
# image_path = "C:\work@taneshka\dev\TM\Z_Prac\WL_Extractions\pdf_ocr\page_1.png"
# reader = easyocr.Reader(['en'])
# # 2. OCR the image
# results = reader.readtext(image_path, detail=0)
# text = "\n".join(results)
# # 3. Extract name
# name_match = re.search(r'\bto\s+([A-Z][a-z]+\s[A-Z][a-z]+)', text)
# name = name_match.group(1) if name_match else "Not found"
# # 4. Extract address (line after name)
# address_match = re.search(name + r'\s*\n(.+)', text)
# address = address_match.group(1) if address_match else "Not found"
# # 5. Create DataFrame
# df = pd.DataFrame([{
#    'Name': name,
#    'Address': address
# }])
# # 6. Save to Excel
# df.to_excel("extracted_info.xlsx", index=False)
# print("✅ Name and address saved to 'extracted_info.xlsx'")