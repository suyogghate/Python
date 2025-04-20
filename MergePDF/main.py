from PyPDF2 import PdfMerger
import os

merger = PdfMerger()
# merger = PdfWriter()
files = [file for file in os.listdir() if file.endswith(".pdf")]
# files = ["dummy1.pdf", "dummy2.pdf"]

for pdf in files:
    merger.append(pdf)

merger.write("merged.pdf")
merger.close()