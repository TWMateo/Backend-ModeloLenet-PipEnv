import os
import cv2
import numpy as np
from keras.models import load_model


def predict_digit(img) -> dict:
    # Load the model
    model_path = os.path.join(os.path.dirname(__file__), 'cnn_model.h5')
    model = load_model(model_path)

    # Read the image
    img = cv2.imread(img)
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
