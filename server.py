import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

KEYS_FILE_URL = "https://raw.githubusercontent.com/loltestiunggerhrf/yesss/main/keys.txt"

def fetch_keys():
    try:
        response = requests.get(KEYS_FILE_URL)
        response.raise_for_status()
        return response.text.splitlines()
    except requests.RequestException as e:
        print(f"Error fetching keys: {e}")
        return []

@app.route("/", methods=["GET"])
def home():
    return "API is working! Use /validate_key?key=YOUR_KEY to validate."

@app.route('/validate_key', methods=['GET'])
def validate_key():
    script_key = request.args.get('key')
    valid_keys = fetch_keys()

    if script_key in valid_keys:
        return jsonify({"status": "success", "message": "Key is valid!"})
    else:
        return jsonify({"status": "error", "message": "Invalid key!"})

if __name__ == "__main__":
    app.run(debug=True)
