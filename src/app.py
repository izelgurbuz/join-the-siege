from flask import Flask, request, jsonify
from src.classifier import classify_file
from src.utils import allowed_file

app = Flask(__name__)

@app.route('/classify_file', methods=['POST'])
def classify_file_route():
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if not allowed_file(file.filename):
        return jsonify({"error": f"File type not allowed"}), 400

    try:
        file_class = classify_file(file)
        return jsonify({"file_class": file_class}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
