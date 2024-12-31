from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for cross-origin requests (React to Flask)

# MongoDB connection
client = MongoClient("mongodb+srv://Ritik:ritik123@cluster0.btkvbre.mongodb.net/")  # Replace with your MongoDB Atlas URI
db = client["contact_db"]  # Replace with your desired database name
collection = db["contacts"]  # Replace with your desired collection name

# Route to handle form submissions
@app.route('/submit-form', methods=['POST'])
def submit_form():
    try:
        data = request.json  # Get the JSON data from the request
        # Insert data into MongoDB
        collection.insert_one(data)
        return jsonify({"message": "Form submitted successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Health check route
@app.route('/')
def health_check():
    return "Flask backend is running!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)

