from PIL import Image
from flask import Flask, request 
from test_model import image_classification
from flask_cors import CORS

app = Flask(__name__)
CORS (app)

@app.route('/', methods=['GET'])
def welcome():
    return "X-Ray project for Flask API!"

@app.route('/image', methods=['POST'])
def main():
    image = request.files['file']
    model_path = 'four_classes.pt'
    image_data = Image.open(image.stream)

    clasification_image = image_classification(model_path = model_path, image = image_data)

    return clasification_image

@app.route('/iscovid', methods=['POST'])
def iscovid_check():
    image = request.files['file']
    model_path = 'is_covid.pt'
    image_data = Image.open(image.stream)

    clasification_image = image_classification(model_path=model_path, image = image_data)

    return clasification_image

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)