from flask import Flask, request
from test_model import image_classification

app = Flask(__name__)

@app.route('/image', methods=['POST'])  
def main():
    image = request.files['file']
    clasification_image = image_classification(image = image.stream)
    
    return clasification_image

if __name__ == "__main__":
    app.run(debug=True, port=8080)

