import tempfile

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4


def make_pdf(page_count, output_file):
    """
    :param page_count: Count of page to generate
    :param output_file: Output file object
    """
    c = canvas.Canvas(output_file, A4)

    c.drawString(100, 100, "Hello world")

    c.showPage()
    c.save()