from PyPDF2 import PdfFileReader, PdfFileWriter

pdf_in = open('file.pdf', 'rb')
pdf_reader = PdfFileReader(pdf_in)
pdf_writer = PdfFileWriter()
for pagenum in range(pdf_reader.numPages):
    page = pdf_reader.getPage(pagenum)
    page.rotateClockwise(90)    # defines rotation angle and direction
    pdf_writer.addPage(page)
pdf_out = open('file_rotated.pdf', 'wb')
pdf_writer.write(pdf_out)
pdf_out.close()
pdf_in.close()
