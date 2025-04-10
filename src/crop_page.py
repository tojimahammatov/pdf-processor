import sys
import PyPDF2 as pdf

from typing import List
from PyPDF2.generic import RectangleObject


def crop_page(
    input_file: str,
    page_number: int,
    crop_bbox: List[float],
):
    # read pdf file
    with open(input_file, 'rb') as fp:
        pdf_reader = pdf.PdfFileReader(fp)

    # create a writer for black pdf
    pdf_writer = pdf.PdfFileWriter()

    # get page by (page index - 1)
    page = pdf_reader.pages[page_number - 1]
    width = page.mediabox.width
    height = page.mediabox.height

    # crop by updating cropbox property of the page
    # Rectangle Object: [x1, y1, x2, y2] => (left, bottom, right, top)
    # crops 25% from the top and 20% from the right
    top, left, bottom, right = crop_bbox
    page.cropbox = RectangleObject((width * left, height * bottom, width * top, height * right))

    for page in pdf_reader.pages:
        pdf_writer.add_page(page)

    output_file = input_file.replace('.pdf', '_cropped.pdf')
    with open(output_file, "wb") as fp:
        pdf_writer.write(fp)


if __name__ == '__main__':
    assert len(sys.argv) == 4, \
        'Provide an input file, page number to be cropped, and fractions for cropping area.'

    input_file = sys.argv[1]
    page_number = int(sys.argv[2])
    crop_bbox = sys.argv[3]
    crop_bbox = crop_bbox.split(',')
    crop_bbox = [float(p) for p in crop_bbox]

    # crop bbox is assumed to be: [top, left, bottom, right]; 
    # e.g: [0.2, 0.0, 0.0, 0.25] => crops 20% from top, 25% from right side of a page.
    crop_page(
        input_file=input_file,
        page_number=page_number,
        crop_bbox=crop_bbox,
    )
