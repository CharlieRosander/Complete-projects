import PyPDF2

# 1 inch = 72 points
# 1 inch = 25.4 mm
POINTS_TO_MM = 0.3527777777777778

with open('test.pdf', 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    page = pdf_reader.pages[0]
    page_size = page.mediabox.upper_right

    width = float(page_size[0])
    length = float(page_size[1])

    print(f"Page size: {page_size} points")
    print(f"Page width in mm: {float(page_size[0]) * POINTS_TO_MM}")
    print(f"Page length in mm: {float(page_size[1]) * POINTS_TO_MM}")

# Program written by Charlie & Jimi bros