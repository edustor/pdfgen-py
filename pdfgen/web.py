from flask import Flask
from flask import send_file, abort
from tempfile import NamedTemporaryFile
from pdfgen import pdf
app = Flask(__name__)


@app.route("/")
@app.route("/<int:page_count>")
def root(page_count=1):
    if page_count > 100:
        abort(400, "Too many pages requested")

    file = NamedTemporaryFile()
    pdf.make_pdf(page_count, file)
    file.seek(0)
    return send_file(file, "application/pdf")
