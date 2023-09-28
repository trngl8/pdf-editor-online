from pypdf import PdfReader, PdfWriter

reader = PdfReader("var/data/example.pdf")
writer = PdfWriter()
page = reader.pages.pop(0)
writer.add_page(page)
with open("var/data/example-modified.pdf", "wb") as fp:
    writer.write(fp)
