from pypdf import PdfReader, PdfWriter

reader = PdfReader("var/data/example.pdf")
writer = PdfWriter()
number_of_pages = len(reader.pages)
page = reader.pages[0]

writer.add_page(reader.pages[0])
with open("var/data/example-modified.pdf", "wb") as fp:
    writer.write(fp)
