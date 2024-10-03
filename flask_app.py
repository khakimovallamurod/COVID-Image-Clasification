from ultralytics import YOLO # type: ignore
from flask import Flask, send_file # type: ignore
import matplotlib.pyplot as plt # type: ignore
import numpy as np # type: ignore
import cv2 # type: ignore
import os

# Load the YOLO model
model = YOLO("yolov8n-cls.yaml")

app = Flask(__name__)

@app.route('/image/<type>/<path>', methods=['GET'])
def image_classification(type, path: str):
    image_path = f"dataset/train/{type}/{path}"
    print(image_path)
    results = model(image_path)

    image = results[0].orig_img
    # for pred in results[0]:
    #     print(pred)
    temp_image_path = "temp_image.png"
    cv2.imwrite(temp_image_path, image)
    
    return send_file(temp_image_path, mimetype='image/png') 

if __name__ == '__main__':
    app.run(debug=True, port=7080)
