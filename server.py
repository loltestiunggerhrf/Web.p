import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# URL of your GitHub raw keys file
KEYS_FILE_URL = "https://raw.githubusercontent.com/loltestiunggerhrf/yesss/main/keys.txt"

# Function to fetch keys from GitHub
def fetch_keys():
    try:
        response = requests.get(KEYS_FILE_URL)
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.text.splitlines()  # Split keys by line and return as list
    except requests.RequestException as e:
        print(f"Error fetching keys: {e}")
        return []

@app.route('/validate_key', methods=['GET'])
def validate_key():
    # Get the key from the URL parameter
    script_key = request.args.get('key')

    # Fetch keys from the GitHub repo
    valid_keys = fetch_keys()

    # Check if the provided key is valid
    if script_key in valid_keys:
        return jsonify({"status": "success", "message": "Key is valid!"})
    else:
        return jsonify({"status": "error", "message": "Invalid key!"})

if __name__ == "__main__":
    app.run(debug=True)
