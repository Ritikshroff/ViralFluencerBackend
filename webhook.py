from flask import Blueprint, request, jsonify
import logging

webhook_bp = Blueprint('webhook', __name__)

# Handle webhook verification for Facebook
@webhook_bp.route('/webhook', methods=['GET'])
def verify_webhook():
    verify_token = request.args.get('hub.verify_token')
    challenge = request.args.get('hub.challenge')

    # Your custom verify token here
    if verify_token == 'your_custom_verify_token':
        return challenge, 200
    return 'Invalid verify token', 403

# Handle webhook events from Facebook
@webhook_bp.route('/webhook', methods=['POST'])
def handle_webhook():
    data = request.get_json()
    logging.info(f"Received data: {data}")
    # Process the data here (e.g., store in DB or take actions)
    return jsonify({"status": "received"}), 200
