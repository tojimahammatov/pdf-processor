import sys
import PyPDF2 as pdf


def merge_files(
    input_file1: str,
    input_file2: str,
):
    # read the files that you have opened
    with open(input_file1, 'rb') as fp:
        pdf1_reader = pdf.PdfFileReader(fp)

    with open(input_file2, 'rb') as fp:
        pdf2_reader = pdf.PdfFileReader(fp)

    # create a new PdfFileWriter object which represents a blank PDF document
    pdf_writer = pdf.PdfFileWriter()

    # loop through all the pages of the first document
    for page in pdf1_reader.pages:
        pdf_writer.add_page(page)

    # loop through all the pages of the second document
    for page in pdf2_reader.pages:
        pdf_writer.add_page(page)

    # write merged pdf into the a new document
    output_file = input_file1.replace('.pdf', '') + '_' + input_file2.replace('.pdf', '') + '_merged.pdf'
    with open(output_file, 'wb') as fp:
        pdf_writer.write(output_file)


if __name__ == '__main__':
    assert len(sys.argv) == 3, \
        'Provide two input files to be merged.'

    input_file1 = sys.argv[1]
    input_file2 = sys.argv[2]

    merge_files(
        input_file1=input_file1,
        input_file2=input_file2,
    )
