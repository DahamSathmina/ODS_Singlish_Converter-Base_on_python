from flask import Flask, render_template, request, jsonify
from converter import convert_to_sinhala

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('preloader.html')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    data = request.get_json()
    singlish_text = data.get('text', '')
    sinhala_text = convert_to_sinhala(singlish_text)
    return jsonify({'result': sinhala_text})

if __name__ == '__main__':
    app.run(debug=True)
