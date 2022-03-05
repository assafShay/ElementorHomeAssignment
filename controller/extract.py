import requests
import base64
from config import API_KEY

def get_url_analysis_report(id):
    url = f"https://www.virustotal.com/api/v3/urls/{id}"

    headers = {
        "Accept": "application/json",
        "X-Apikey": API_KEY
    }

    response = requests.request("GET", url, headers=headers)

    return response.json()

