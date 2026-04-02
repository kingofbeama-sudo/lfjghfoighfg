from flask import Flask, request, jsonify
import threading
import time
import os

app = Flask(__name__)
data_store = {"digit_amount": 0}

# This function waits 10 seconds then subtracts 1
def remove_count_after_delay():
    time.sleep(10)
    if data_store["digit_amount"] > 0:
        data_store["digit_amount"] -= 1
        print("10 seconds passed: subtracted 1")

@app.route('/')
def home():
    return f"Current Count: {data_store['digit_amount']}"

@app.route('/get', methods=['GET'])
def get_digit():
    return jsonify(data_store)

@app.route('/execute', methods=['GET'])
def execute_count():
    # 1. Add 1 to the count
    data_store["digit_amount"] += 1
    
    # 2. Start a background timer to remove it later
    # This allows the API to respond immediately while the timer runs
    threading.Thread(target=remove_count_after_delay).start()
    
    return jsonify({
        "status": "executed", 
        "current_total": data_store["digit_amount"],
        "note": "This +1 will expire in 10 seconds"
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
