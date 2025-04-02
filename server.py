import requests
import time
from flask import Flask, request, jsonify

app = Flask(__name__)

# GitHub Raw URL for keys.txt
KEYS_FILE_URL = "https://raw.githubusercontent.com/loltestiunggerhrf/yesss/main/keys.txt?nocache=" + str(time.time())

# Function to fetch keys from GitHub
def fetch_keys():
    try:
        response = requests.get(KEYS_FILE_URL, headers={"Cache-Control": "no-cache"})
        response.raise_for_status()
        return response.text.splitlines()
    except requests.RequestException as e:
        print(f"Error fetching keys: {e}")
        return []

# API Route to validate keys
@app.route('/validate_key', methods=['GET'])
def validate_key():
    user_key = request.args.get("key")
    valid_keys = fetch_keys()

    if user_key in valid_keys:
        return jsonify({"message": "Key is valid!", "status": "success"})
    else:
        return jsonify({"message": "Invalid key!", "status": "error"})

# API Route to check current valid keys (for debugging)
@app.route('/get_keys', methods=['GET'])
def get_keys():
    return jsonify(fetch_keys())

# Run the Flask server
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
