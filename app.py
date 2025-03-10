from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
import os
import bcrypt
import jwt
import datetime
import secrets
# from instagram_api import get_instagram_profile, get_media_insights
from webhook import webhook_bp
import logging
from auth import auth_bp
from flask import Blueprint, request
from instagram_api import get_instagram_access_token
print(secrets.token_hex(32))  # Generates a 64-character hexadecimal string
jwt_secret_key = "your_actual_secret_key"
print(type(jwt_secret_key))  # Should be <class 'str'>



app = Flask(__name__)
CORS(app)  # Enable CORS for cross-origin requests (React to Flask)

# MongoDB connection
client = MongoClient("mongodb+srv://Ritik:ritik123@cluster0.btkvbre.mongodb.net/")  # Replace with your MongoDB Atlas URI
db = client["contact_db"]  # Replace with your desired database name
collection = db["contacts"]  # Replace with your desired collection name
influencers_collection = db["influencers"]  # Collection for influencer signups
brand_collection = db["brand"]  # Collection for brand signups
agency_collection = db["agency"]  # Collection for agency signups
partner_collection = db["partner"]  # Collection for partner signups

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

@app.route('/login', methods=['POST'])
def login():
    try:
        login_data = request.json  # Get the JSON data from the request
        email = login_data.get('email')
        password = login_data.get('password')

        # Validate input
        if not email or not password:
            return jsonify({"error": "Email and password are required"}), 400

        # Check if the user exists in influencers collection
        user = influencers_collection.find_one({"email": email})
        if not user:
            user = brand_collection.find_one({"email" : email})
        if not user:
            user = agency_collection.find_one({"email" : email})
        if not user:
            user = partner_collection.find_one({"email" : email})
            
        if not user:
            return jsonify({"error": "User not found"}), 404

        # Compare hashed password
        if not bcrypt.checkpw(password.encode('utf-8'), user['password']):
            return jsonify({"error": "Invalid credentials"}), 401

        # Generate JWT token (optional)
        token = jwt.encode(
            {"user_id": str(user["_id"]), "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)},
            jwt_secret_key,  # Replace with your actual secret key
            algorithm="HS256"
        )

        return jsonify({"message": "Login successful!", "token": token}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Route to handle influencer signups
@app.route('/signup/influencer', methods=['POST'])
def signup_influencer():
    try:
        influencer_data = request.json  # Get the JSON data from the request
        
                # Hash the password
        if 'password' in influencer_data:
            influencer_data['password'] = bcrypt.hashpw(
                influencer_data['password'].encode('utf-8'), bcrypt.gensalt()
            )
            
        # Insert data into the influencers collection
        influencers_collection.insert_one(influencer_data)
        return jsonify({"message": "Influencer signup successful!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
# Route to handle Brand signups
@app.route('/signup/brand', methods=['POST'])
def signup_brand():
    try:
        brand_data = request.json  # Get the JSON data from the request
                        # Hash the password
        if 'password' in brand_data:
            brand_data['password'] = bcrypt.hashpw(
                brand_data['password'].encode('utf-8'), bcrypt.gensalt()
            )
        # Insert data into the influencers collection
        brand_collection.insert_one(brand_data)
        return jsonify({"message": "Brand signup successful!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
# Route to handle agency signups
@app.route('/signup/agency', methods=['POST'])
def signup_agency():
    try:
        agency_data = request.json  # Get the JSON data from the request
        # Insert data into the influencers collection
                                # Hash the password
        if 'password' in agency_data:
            agency_data['password'] = bcrypt.hashpw(
                agency_data['password'].encode('utf-8'), bcrypt.gensalt()
            )
        agency_collection.insert_one(agency_data)
        return jsonify({"message": "agency signup successful!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
# Route to handle agency signups
@app.route('/signup/partner', methods=['POST'])
def signup_partner():
    try:
        partner_data = request.json  # Get the JSON data from the request
                                # Hash the password
        if 'password' in partner_data:
            partner_data['password'] = bcrypt.hashpw(
                partner_data['password'].encode('utf-8'), bcrypt.gensalt()
            )
        # Insert data into the influencers collection
        partner_collection.insert_one(partner_data)
        return jsonify({"message": "partner signup successful!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    # Use the Instagram API functions in routes
# @app.route('/get-instagram-profile', methods=['GET'])
# def get_instagram_profile_route():
#     access_token = request.args.get('access_token')
#     return get_instagram_profile(access_token)

# @app.route('/get-media-insights', methods=['GET'])
# def get_media_insights_route():
    media_id = request.args.get('media_id')
    access_token = request.args.get('access_token')
    return get_media_insights(media_id, access_token)

# Registering the webhook blueprint
app.register_blueprint(webhook_bp)
app.register_blueprint(auth_bp)
# Enable logging
# logging.basicConfig(level=logging.DEBUG)


auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/get-instagram-token', methods=['POST'])
def get_token():
    auth_code = request.json.get('code')

    if not auth_code:
        return {"error": "Authorization code is required"}, 400

    return get_instagram_access_token(auth_code)

# Health check route
@app.route('/')
def health_check():
    return "Flask backend is running!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)

