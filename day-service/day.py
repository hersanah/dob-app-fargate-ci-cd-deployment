from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime


app = Flask(__name__)

cors = CORS(app, resources={r"/*": {"origins": "*"}})


days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


@app.route('/day', methods=['GET'])
def get_day():
    dob = request.args.get('dob')
    if not dob:
        return "DOB is required", 400


    date = datetime.strptime(dob, '%Y-%m-%d')
    day = days[date.weekday()]


    return f"You were born on a {day}."


@app.route('/health', methods=['GET'])
def health_check():
    status = {"status": "healthy"}
    return jsonify(status), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)