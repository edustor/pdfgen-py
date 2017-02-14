from flask import Flask
from flask import send_file
from tempfile import NamedTemporaryFile
from pdfgen import pdf
app = Flask(__name__)


@app.route("/")
@app.route("/<int:page_count>")
def root(page_count=1):
    file = NamedTemporaryFile()
    pdf.make_pdf(page_count, file)
    file.seek(0)
    return send_file(file, "application/pdf")
