from PyPDF2 import PdfFileWriter, PdfFileReader

inputpdf = PdfFileReader(open("payment.pdf", "rb"))

for i in range(inputpdf.numPages):
    output = PdfFileWriter()
    output.addPage(inputpdf.getPage(i))
    with open("document-page-%s.pdf" % (i+1), "wb") as outputStream:
        output.write(outputStream)
    # to split only first page, stop, continue otherwise
    break
