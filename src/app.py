import os
from werkzeug.utils import secure_filename
from flask import Flask, render_template, request
from .cnn import predict_digit
from keras.models import load_model
import cv2
import numpy as np


app = Flask(__name__)
app.config['files'] = os.path.join(os.path.dirname(__file__), 'files')


@app.get("/")
def show_homepage():
    return render_template("upload_image.html")


@app.post("/predict")
def predict_image():
    image = request.files['image']

    filepath = save_image(image)

    # prediction = predict_digit(filepath)

    # delete_image(filepath)

    # Load the model
    model_path = os.path.join(os.path.dirname(__file__), 'cnn','cnn_model.h5')
    model = load_model(model_path)

    # Read the image
    img = cv2.imread(filepath)
    gray = np.dot(img[..., :3], [0.299, 0.587, 0.114])

    # reshape the image
    gray = gray.reshape(1, 28, 28, 1)
    # normalize image
    gray /= 255

    prediction = model.predict(gray.reshape(1, 28, 28, 1))

    return {
        "message": "success",
        "predicted_number": float(prediction.argmax())
    }

    #return prediction


def save_image(image) -> str:
    filename = secure_filename(image.filename)
    filepath = os.path.join(app.config['files'], filename)
    image.save(filepath)

    return filepath


def delete_image(filepath):
    os.remove(filepath)
