# import requests
# from flask import jsonify

# def get_instagram_profile(access_token):
#     url = f"https://graph.instagram.com/me?fields=id,username,followers_count,media_count&access_token={access_token}"
#     response = requests.get(url)
    
#     if response.status_code == 200:
#         data = response.json()
#         return jsonify(data), 200
#     else:
#         return jsonify({"error": "Failed to fetch Instagram data"}), 500

# def get_media_insights(media_id, access_token):
#     url = f"https://graph.instagram.com/{media_id}/insights?metric=engagement,impressions,reach&access_token={access_token}"
#     response = requests.get(url)
    
#     if response.status_code == 200:
#         insights = response.json()
#         return jsonify(insights), 200
#     else:
#         return jsonify({"error": "Failed to fetch media insights"}), 500


import requests
from flask import jsonify
from config import Config


def get_instagram_access_token(auth_code):
    url = "https://api.instagram.com/oauth/access_token"
    payload = {
        'client_id': Config.INSTAGRAM_CLIENT_ID,
        'client_secret': Config.INSTAGRAM_CLIENT_SECRET,
        'grant_type': 'authorization_code',
        'redirect_uri': Config.INSTAGRAM_REDIRECT_URI,
        'code': auth_code
    }

    try:
        response = requests.post(url, data=payload)
        response_data = response.json()

        if response.status_code == 200:
            return jsonify(response_data)  # Return access token
        else:
            return jsonify({'error': 'Failed to get access token', 'details': response_data}), response.status_code
    except Exception as e:
        return jsonify({'error': str(e)}), 500
