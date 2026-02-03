from flask import Flask, request, jsonify
from flask_cors import CORS
from gpa import percentage_to_gpa, scale12_to_gpa, scale5_to_gpa, letter_grade_to_gpa
import os

app = Flask(__name__, static_url_path='', static_folder='static')
CORS(app)

@app.route('/')
def home():
    return app.send_static_file('index.html')  # Serve your front-end

@app.route('/convert', methods=['POST'])
def convert_gpa():
    data = request.json
    type_ = data.get("type")  # 'percentage', '12scale', '5scale', 'letter'
    value = data.get("value")

    try:
        if type_ == "percentage":
            gpa = percentage_to_gpa(float(value))
        elif type_ == "12scale":
            gpa = scale12_to_gpa(float(value))
        elif type_ == "5scale":
            gpa = scale5_to_gpa(float(value))
        elif type_ == "letter":
            gpa = letter_grade_to_gpa(str(value))
        else:
            return jsonify({"error": "Invalid type"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 400

    return jsonify({"gpa": gpa})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
