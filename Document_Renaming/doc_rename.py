# import os
# import pandas as pd

# xls_file = 'Doc_data.xlsx'
# df = pd.read_excel(xls_file)

# olf = df['Old File Name'].values.tolist()
# nfl = df['New File Name'].values.tolist()

# for idx, n in enumerate(olf):
#     old_file = os.path.join('C:\work@taneshka\dev\TM\Z_Prac\Document_Rename\Docs"%s"' %str(olf[idx]))
#     new_file = os.path.join('C:\work@taneshka\dev\TM\Z_Prac\Document_Rename\Docs"%s"' %str(nfl[idx]))
#     os.rename(old_file, new_file)
#     print("File name updated!")
#     print("\n")

import os

# folder_path = r'C:\work@taneshka\dev\TM\Z_Prac\Document_Rename\Docs'
folder_path = r'/Users/taneshkamehta/Documents/RPA/Document_Manipulations/Document_Renaming/Documents'

# Rename files with custom pattern
for index, filename in enumerate(os.listdir(folder_path)):
   if filename.lower().endswith(('.pdf', '.docx', '.txt')):  # Supported extensions
       old_path = os.path.join(folder_path, filename)
       # Define new name, e.g., Document_1.pdf (Can customise it too)
       file_extension = os.path.splitext(filename)[1]
       new_filename = f'Document_{index + 1}{file_extension}'
       new_path = os.path.join(folder_path, new_filename)
       os.rename(old_path, new_path)
       print(f'Renamed: {filename} ➜ {new_filename}')