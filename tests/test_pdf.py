import sh
from pdfgen import pdf


def test_pdf_generation():
    sh.mkdir("-p", "test_results")
    with open("test_results/test.pdf", "wb") as file:
        pdf.make_pdf(50, file)

if __name__ == '__main__':
    test_pdf_generation()
