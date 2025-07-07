import os.path
import pandas as pd

xls_file = 'doc_data.xlsx'
df = pd.read_excel(xls_file)

olf = df['File Name'].values.tolist()

# fl = "Prac.docx"
# p = os.path.abspath(fl)
# print(p)
for idx, n in enumerate(olf):
    # print(n)
    old_file = os.path.abspath(str(olf[idx]))
    print(old_file)
    # print("File name updated!")
    # print("\n")