from fastapi import FastAPI
from discord import Client

app = FastAPI()
discord_client = Client()

@app.get("/guild/{guild_id}")
async def get_guild_info(guild_id: str):
    guild = discord_client.get_guild(guild_id)
    return {
        "name": guild.name,
        "member_count": guild.member_count,
        "id": guild.id,
    }