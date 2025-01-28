import requests
from flask import jsonify

def get_instagram_profile(access_token):
    url = f"https://graph.instagram.com/me?fields=id,username,followers_count,media_count&access_token={access_token}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return jsonify(data), 200
    else:
        return jsonify({"error": "Failed to fetch Instagram data"}), 500

def get_media_insights(media_id, access_token):
    url = f"https://graph.instagram.com/{media_id}/insights?metric=engagement,impressions,reach&access_token={access_token}"
    response = requests.get(url)
    
    if response.status_code == 200:
        insights = response.json()
        return jsonify(insights), 200
    else:
        return jsonify({"error": "Failed to fetch media insights"}), 500
