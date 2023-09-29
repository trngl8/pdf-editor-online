import os
from pypdf import PdfReader, PdfWriter

directory = "var/data/"
ext = ".pdf"
filename = input("Enter filename: ")
filepath = directory + filename + ext
if not os.path.isfile(filepath):
    raise FileNotFoundError("File not found")
reader = PdfReader(filepath)
writer = PdfWriter()
page = reader.pages[0]
writer.add_page(page)
with open(directory + filename + '.modified' + ext, "wb") as fp:
    writer.write(fp)
print(f"Modified result in {filename + '.modified' + ext}")
