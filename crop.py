from PyPDF2 import PdfWriter, PdfReader
from PyPDF2.generic import RectangleObject

reader = PdfReader("pages.pdf")
writer = PdfWriter()

# crop page 1
page1 = reader.pages[0]
width = page1.mediabox.width
height = page1.mediabox.height
# Rectangle Object: [x1, y1, x2, y2] => (bottom, left, top, right)
page1.cropbox = RectangleObject((0, 0, width, height * 3 / 4))      # crops 25% from top

# crop page 6
page6 = reader.pages[5]
width = page6.mediabox.width
height = page6.mediabox.height
page6.cropbox = RectangleObject((0, height / 5, width, height))     # crops 20% from bottom

for page in reader.pages:
    writer.add_page(page)

with open("pages-cropped.pdf", "wb") as fp:
    writer.write(fp)
