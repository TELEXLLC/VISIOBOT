from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
import os

app = FastAPI()

# Set your Discord webhook URL as an environment variable for security
DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

class WebhookPayload(BaseModel):
    content: str

@app.post("/discord/webhook")
def discord_webhook(payload: WebhookPayload):
    if not DISCORD_WEBHOOK_URL:
        raise HTTPException(status_code=500, detail="DISCORD_WEBHOOK_URL not set in environment.")
    data = {"content": payload.content}
    resp = requests.post(DISCORD_WEBHOOK_URL, json=data)
    if resp.status_code == 204:
        return {"status": "Message sent to Discord webhook."}
    else:
        raise HTTPException(status_code=resp.status_code, detail=resp.text)
