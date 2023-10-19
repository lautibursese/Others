from PyPDF2 import PdfMerger, PdfFileReader

import os

#var = os.getcwd*( )       # For extracting from another folder

merger = PdfMerger()

for items in os.listdir():
    if items.endswith('.pdf'):
        merger.append(items)

merger.write("Final_PDF.pdf")

merger = PdfMerger()

with open(originalFile, 'rb') as fin:
    merger.append(PdfFileReader(fin))

os.remove(originalFile)

merger.close()
