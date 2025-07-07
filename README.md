# 📄 Document Manipulation Automation

This project automates common document operations using Python, designed for RPA use cases,

## 🚀 Features

1. **Document Conversion**
   - Converts files from one format to another (e.g., `.docx` to `.pdf`, `.pdf` to `.txt`)
2. **Document Parsing**
   - Extracts text from:
     - General documents like `.txt`, `.docx`
     - OCR-based parsing from scanned PDFs or image-based PDFs
3. **Document Path Handling**
   - Automates dynamic path fetching and management across folders
4. **Document Renaming**
   - Bulk rename documents based on defined rules (prefix, suffix, timestamp, pattern, requirement)
5. **New Directory Creation**
   - Creates new folder/bulk folders dynamically for organized document storage

---

## 🛠️ Tech Stack

- Python 3.9+
- Libraries:
  - `os`, `shutil`, `pathlib`
  - `docx`, `PyPDF2`, `pdf2image`, `pytesseract`
  - `openpyxl`, `pandas` (for Excel if needed)
  - `easyocr`, `tesseract` *(optional for OCR)*
