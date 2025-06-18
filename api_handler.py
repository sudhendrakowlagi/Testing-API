import requests

def call_api():
    url = "https://api.example.com/endpoint"  # You will replace this later
    params = {
        "key": "value"  # Update as needed
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": str(e)}
