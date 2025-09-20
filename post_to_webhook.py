import requests

# The URL of your FastAPI endpoint running on your server
API_URL = "http://localhost:8000/discord/webhook"

def send_message(content):
    payload = {"content": content}
    response = requests.post(API_URL, json=payload)
    if response.ok:
        print("Message sent:", response.json())
    else:
        print("Error:", response.status_code, response.text)

if __name__ == "__main__":
    # Example usage
    send_message("Hello from post_to_webhook.py!")
