# import requests
# from flask import Blueprint, request, jsonify
# from config import INSTAGRAM_CLIENT_ID, INSTAGRAM_CLIENT_SECRET, INSTAGRAM_REDIRECT_URI

# auth_bp = Blueprint("auth", __name__)

# @auth_bp.route("/auth/instagram", methods=["POST"])
# def instagram_auth():
#     try:
#         # Get data from request
#         data = request.get_json()
#         if not data or "code" not in data:
#             return jsonify({"error": "Authorization code missing"}), 400

#         code = data["code"]

#         # Instagram Token Exchange API
#         token_url = "https://api.instagram.com/oauth/access_token"
#         payload = {
#             "client_id": INSTAGRAM_CLIENT_ID,
#             "client_secret": INSTAGRAM_CLIENT_SECRET,
#             "grant_type": "authorization_code",
#             "redirect_uri": INSTAGRAM_REDIRECT_URI,
#             "code": code
#         }
#         headers = {"Content-Type": "application/x-www-form-urlencoded"}

#         # Send POST request
#         response = requests.post(token_url, data=payload, headers=headers)
#         token_data = response.json()

#         # Debugging logs
#         print("Response Status Code:", response.status_code)
#         print("Response JSON:", token_data)

#         # Check response
#         if response.status_code == 200 and "access_token" in token_data:
#             return jsonify(token_data)
#         else:
#             return jsonify({"error": token_data.get("error_message", "Unknown error")}), response.status_code

#     except Exception as e:
#         return jsonify({"error": str(e)}), 500


from flask import Blueprint, request
from instagram_api import get_instagram_access_token

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/get-instagram-token', methods=['POST'])
def get_token():
    auth_code = request.json.get('code')

    if not auth_code:
        return {"error": "Authorization code is required"}, 400

    return get_instagram_access_token(auth_code)

