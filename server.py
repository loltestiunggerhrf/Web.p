from flask import Flask, request, jsonify

app = Flask(__name__)

# Example key store (in a real app, you might want to use a database)
valid_keys = ["PASTEKEYHERE", "EXAMPLEKEY123", "ANOTHERKEY456"]

@app.route('/validate_key', methods=['GET'])
def validate_key():
    # Get key from the URL parameter
    script_key = request.args.get('key')

    if script_key in valid_keys:
        return jsonify({"status": "success", "message": "Key is valid!"})
    else:
        return jsonify({"status": "error", "message": "Invalid key!"})

if __name__ == "__main__":
    app.run(debug=True)
