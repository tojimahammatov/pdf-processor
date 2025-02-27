import sys
import PyPDF2 as pdf


def extract_pages(
    input_file: str,
    start_page: int,
    end_page: int,
):
    # create reader for input pdf file
    with open(input_file, 'rb') as fp:
        inputpdf = pdf.PdfFileReader(fp)

    # create output pdf
    outputpdf = pdf.PdfFileWriter()

    # page count starts from 0 index
    if start_page <= 0:
        start_page = 0
    else:
        start_page -= 1
    
    if end_page >= len(inputpdf.pages):
        end_page = len(inputpdf.pages) - 1
    
    # Since range is used to iterate, end_page doesn't need to be decremented by one.
    # Because range doesn't include end index in iteration.
    for i in range(start_page, end_page, 1):
        outputpdf.add_page(inputpdf.pages[i])

    # save output pdf into file
    output_file = input_file.replace('.pdf', f'_{start_page}-{end_page}_pages.pdf')
    with open(output_file, 'wb') as fp:
        outputpdf.write(fp)


if __name__ == '__main__':
    assert len(sys.argv) == 4, \
        'Provide input file, start and end pages number in natural count.'

    input_file = sys.argv[1]
    start_page = int(sys.argv[2])
    end_page = int(sys.argv[3])

    extract_pages(
        input_file=input_file,
        start_page=start_page,
        end_page=end_page,
    )
