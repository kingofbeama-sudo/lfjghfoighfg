from flask import Flask, request, jsonify
import os

app = Flask(__name__)
data_store = {"digit_amount": 0}

@app.route('/')
def home():
    return "API is active! View at /get, update at /update?value=123"

@app.route('/get', methods=['GET'])
def get_digit():
    return jsonify(data_store)

@app.route('/update', methods=['GET'])
def update_digit():
    new_value = request.args.get('value')
    if new_value and new_value.isdigit():
        data_store["digit_amount"] = int(new_value)
        return jsonify({"status": "success", "value": data_store["digit_amount"]})
    return jsonify({"error": "Invalid input"}), 400

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
