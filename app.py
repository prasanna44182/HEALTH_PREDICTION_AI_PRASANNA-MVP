from flask import Flask, jsonify
from flask_cors import CORS

# Initialize the Flask app
app = Flask(__name__)

# Enable CORS to allow access from different origins
CORS(app)

# Define a test route to check if Flask is running
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Flask is running successfully!"})

# Run the Flask application with external access enabled
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4090, debug=True)
