from csv import DictReader
from io import TextIOWrapper
from dataclasses import dataclass, asdict
from flask import Flask, request, render_template
from werkzeug.datastructures import FileStorage


@dataclass
class Product:
    code: int
    name: str
    description: str


app = Flask(__name__)


@app.get("/")
def root():
    return "Hello World!"


@app.route("/upload/", methods=["GET", "POST"])
def upload_csv():
    if request.method == "GET":
        return render_template("upload-csv-file.html")

    csv_file = request.files["csv-file"]
    text_file = TextIOWrapper(
        buffer=csv_file.stream,
    )

    reader = DictReader(text_file)

    return render_template(
        "select-options-from-table.html",
        products=[
            Product(**product)
            for product in reader
        ],
    )


@app.route("/upload/confirm/", methods=["GET", "POST"], endpoint="confirm-upload")
def confirm_upload():
    if request.method == "GET":
        return "Upload something please"

    codes = request.form.getlist("product-code")
    names = request.form.getlist("product-name")
    descriptions = request.form.getlist("product-description")

    raw_products_data = {}
    for code, name, desc in zip(codes, names, descriptions):
        raw_products_data[code] = {
            "code": code,
            "name": name,
            "description": desc,
        }

    selected = request.form.getlist("product-check")
    products = []

    for selected_code in selected:
        data = raw_products_data[selected_code]
        products.append(Product(**data))

    return {
        "products": [
            asdict(product)
            for product in products
        ]
    }


if __name__ == '__main__':
    app.run(debug=True)
