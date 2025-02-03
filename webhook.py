from flask import Blueprint, request, jsonify

webhook_bp = Blueprint("webhook", __name__)

# Replace this with your actual token
VERIFY_TOKEN = "IGAAXPKaG1zuVBZAE16UUhTNVc4MENQMmFUdGQwWVMxSUpFYk13ZAERITmdEM05sbGlJQm93b0t3eENHOVdIY3ZAUbThUanRyRWsxN0JJYzU1dVZA6ODNmS3JHaGZAXazUzeU1mdDhMdXBSWnQ2enhWeFF0ZAF9sSHJuazBmQWR3c3dJRQZDZD"

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
