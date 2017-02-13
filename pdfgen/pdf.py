from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm


def make_pdf(page_count, output_file):
    """
    :param page_count: Count of page to generate
    :param output_file: Output file object
    """
    c = canvas.Canvas(output_file, A4)

    _make_grid(c)

    c.showPage()
    c.save()


def _make_grid(c, x_cells=40, y_cells=56, cell_side=5 * mm):
    c.setLineWidth(0.1)

    page_width, page_height = A4

    x_margin = (page_width - (x_cells * cell_side)) / 2
    y_margin = (page_height - (y_cells * cell_side)) / 2

    x_min, x_max = x_margin, page_width - x_margin
    y_min, y_max = y_margin, page_height - y_margin

    for xi in range(x_cells + 1):
        x = x_margin + xi * cell_side
        c.line(x, y_min, x, y_max)

    for yi in range(y_cells + 1):
        y = y_margin + yi * cell_side
        c.line(x_min, y, x_max, y)
