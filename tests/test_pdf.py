import sh
from pdfgen import pdf


def test_pdf_generation():
    sh.mkdir("-p", "test_results")
    with open("test_results/test.pdf", "wb") as file:
        make_pdf = pdf.make_pdf(1, file)
