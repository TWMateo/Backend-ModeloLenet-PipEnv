import os
from werkzeug.utils import secure_filename
from flask import Flask, render_template, request
from keras.models import load_model
import cv2
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app,origins="*")
app.config['files'] = os.path.join(os.path.dirname(__file__), 'files')


@app.get("/")
def show_homepage():
    return 'Modelo Lenet - Backend'


@app.post("/predict")
def predict_image():
    image = request.files['image']

    filepath = save_image(image)

    model_path = os.path.join(os.path.dirname(__file__), 'cnn','cnn_model.h5')
    model = load_model(model_path)

    img = cv2.imread(filepath)
    gray = np.dot(img[..., :3], [0.299, 0.587, 0.114])

    gray = gray.reshape(1, 28, 28, 1)
    gray /= 255

    prediction = model.predict(gray.reshape(1, 28, 28, 1))

    return {
        "message": "ok",
        "prediccion": float(prediction.argmax())
    }



def save_image(image) -> str:
    filename = secure_filename(image.filename)
    filepath = os.path.join(app.config['files'], filename)
    image.save(filepath)

    return filepath


def delete_image(filepath):
    os.remove(filepath)
