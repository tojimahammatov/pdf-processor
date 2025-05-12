import sys
import pypdf as pdf


def merge_files(
    input_file1: str,
    input_file2: str,
):
    # create a new PdfWriter object which represents a blank PDF document
    pdf_writer = pdf.PdfWriter()

    # loop through files to be merged
    for file in [input_file1, input_file2]:
        pdf_writer.append(file)

    # save merged pdf into the a new pdf file
    output_file = input_file1.replace('.pdf', '_merged.pdf')
    with open(output_file, 'wb') as fp:
        pdf_writer.write(fp)


if __name__ == '__main__':
    assert len(sys.argv) == 3, \
        'Provide two input files to be merged.'

    input_file1 = sys.argv[1]
    input_file2 = sys.argv[2]

    merge_files(
        input_file1=input_file1,
        input_file2=input_file2,
    )
