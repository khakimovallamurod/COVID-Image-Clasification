from flask import Flask, send_file, render_template, request, redirect
from test_model import image_clasification
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads/'
RESULT_FOLDER = 'static/result/'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['RESULT_FOLDER'] = RESULT_FOLDER

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return redirect(request.url)
    
    file = request.files['image']
    if file.filename == '':
        return redirect(request.url)
   
    if file and allowed_file(file.filename):
        filename = file.filename
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        result_image_pth = os.path.join(app.config['RESULT_FOLDER'], filename)
        file.save(filepath)
        image_clasification(image_path = filepath, output_image = result_image_pth)

        return send_file(result_image_pth, mimetype='image/png') 
    
    return 'Ruxsat etilmagan fayl turi'

if __name__ == '__main__':
    app.run(debug=True, port=5000)

