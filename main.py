from urllib import request

import pandas as pd
from flask import Flask, render_template, request
import os

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("base.html")


@app.route('/upload', methods=['POST'])
def upload():
    if 'csvFile' not in request.files:
        return "No file part"
    file = request.files['csvFile']
    if file.filename == '':
        return "No selected file"
    file.save('uploads/' + file.filename)
    file = "uploads/" + file.filename
    rca_creator(file)
    return render_template("base.html")


def rca_creator(filepath: str) -> None:
    if filepath.endswith('.csv') and os.path.exists(filepath):
        df = pd.read_csv(filepath)
        print(df)


if __name__ == '__main__':
    app.run(debug=True)
