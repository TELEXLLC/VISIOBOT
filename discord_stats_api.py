import os
import threading
import discord
from fastapi import FastAPI
from dotenv import load_dotenv
load_dotenv()
DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
app = FastAPI()
client = discord.Client(intents=discord.Intents.all())
@app.get("/server-info")
async def server_info():
    await client.wait_until_ready()
    guilds = []
    for guild in client.guilds:
        guilds.append({
            "id": guild.id,
            "name": guild.name,
            "member_count": guild.member_count,
            "icon_url": str(guild.icon.url) if guild.icon else None,
        })
    return {"guilds": guilds}
def start_bot():
    client.run(DISCORD_BOT_TOKEN)
if not client.is_ready():
    threading.Thread(target=start_bot, daemon=True).start()