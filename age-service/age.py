from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime


app = Flask(__name__)

cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/age', methods=['GET'])
def get_age():
    dob = request.args.get('dob')
    if not dob:
        return "DOB is required", 400


    birthdate = datetime.strptime(dob, '%Y-%m-%d')
    today = datetime.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))


    return f"Your age is {age} years. Working workflow!", 200


@app.route('/health', methods=['GET'])
def health_check():
    status = {"status": "healthy"}
    return jsonify(status), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)