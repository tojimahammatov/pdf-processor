import sys
import PyPDF2 as pdf


def rotate_page(
    input_file: str,
    page_number: int,
):
    # read pdf file
    with open(input_file, 'rb') as fp:
        pdf_reader = pdf.PdfFileReader(fp)

    # create a writer for black pdf
    pdf_writer = pdf.PdfFileWriter()

    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        if page_num == (page_number - 1):       # page index starts from 0
            page.rotate_clockwise(90)            # defines rotation angle and direction
        pdf_writer.add_page(page)

    output_file = input_file.replace('.pdf', '_rotated.pdf')
    with open(output_file, 'wb') as fp:
        pdf_writer.write(fp)


if __name__ == '__main__':
    assert len(sys.argv) == 3, \
        'Provide an input file and page number to be rotated.'

    input_file = sys.argv[1]
    page_number = int(sys.argv[2])

    rotate_page(
        input_file=input_file,
        page_number=page_number,
    )
