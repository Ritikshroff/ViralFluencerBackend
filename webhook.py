from flask import Blueprint, request, jsonify

webhook_bp = Blueprint("webhook", __name__)

# Replace this with your actual token
VERIFY_TOKEN = "IGAAXojLdxcnBBZAFBkSFA2ZAnBNMG5lVk9yWGR6QlN2d3ZADbmF3M1RoV1YxMjUwNDBkTXFJVXJJWXFKaGVBdWRRUkVTcXVySkZANVXVGRmFRNzFTVl9Rd1hHT3JZAWXlCSVpzUThSM1JiTmNwVk0yRC0xNXZARMHRwMmFmLU16VEU2MAZDZD"

@webhook_bp.route("/webhook", methods=["GET"])
def verify_webhook():
    """Handles the GET request for Facebook webhook verification"""
    verify_token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    print(f"Received verify_token: {verify_token}")  # Debugging
    print(f"Expected verify_token: {VERIFY_TOKEN}")  # Debugging

    if verify_token == VERIFY_TOKEN:
        return challenge, 200
    return "Invalid verify token", 403

@webhook_bp.route("/webhook", methods=["POST"])
def handle_webhook():
    """Handles incoming messages from Facebook"""
    data = request.get_json()
    print("Received webhook data:", data)

    # Respond to Facebook
    return jsonify({"status": "success"}), 200
