import sys
import pypdf as pdf


def add_page_to_pdf(
    input_file1: str,
    input_file2: str,
    new_page_index: int = -1,   # default means that page will be added to the end of the `input_file1`
    adding_page_index: int = 0, # default means that first page of `input_file2` will be added
):
    # read the files
    pdf1_reader = pdf.PdfReader(input_file1)
    pdf2_reader = pdf.PdfReader(input_file2)

    # Create a new PdfFileWriter object which represents a blank PDF document
    pdf_writer = pdf.PdfWriter()

    # Loop through all the page numbers for the first document
    for page_num in range(len(pdf1_reader.pages)):
        if page_num == new_page_index:
            page = pdf2_reader.pages[adding_page_index]
        else:
            page = pdf1_reader.pages[page_num]
        pdf_writer.add_page(page)
    
    # if a page needs to be added to the end (which means previous for loop didn't enter if clause)
    if new_page_index == -1 or new_page_index >= len(pdf1_reader.pages):
        pdf_writer.add_page(pdf2_reader.pages[adding_page_index])

    # write output pdf into the a new file
    output_file = input_file1.replace('.pdf', '_page_added.pdf')
    with open(output_file, 'wb') as fp:
        pdf_writer.write(fp)


if __name__ == '__main__':
    assert len(sys.argv) == 5, \
        'Provide input files, start and end pages number in natural count.'

    input_file1 = sys.argv[1]
    input_file2 = sys.argv[2]
    new_page_index = int(sys.argv[3])
    adding_page_index = int(sys.argv[4])

    add_page_to_pdf(
        input_file1=input_file1,
        input_file2=input_file2,
        new_page_index=new_page_index,
        adding_page_index=adding_page_index,
    )
