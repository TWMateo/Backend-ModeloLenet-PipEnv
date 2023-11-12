import os
from werkzeug.utils import secure_filename
from flask import Flask, render_template, request
from .cnn import predict_digit


app = Flask(__name__)
app.config['files'] = os.path.join(os.path.dirname(__file__), 'files')


@app.get("/")
def show_homepage():
    return render_template("upload_image.html")


@app.post("/predict")
def predict_image():
    image = request.files['image']

    filepath = save_image(image)

    prediction = predict_digit(filepath)

    delete_image(filepath)

    return prediction


def save_image(image) -> str:
    filename = secure_filename(image.filename)
    filepath = os.path.join(app.config['files'], filename)
    image.save(filepath)

    return filepath


def delete_image(filepath):
    os.remove(filepath)
