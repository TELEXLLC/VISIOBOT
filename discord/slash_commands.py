import discord
from discord import app_commands

class MyClient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.all())
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()

client = MyClient()

@client.tree.command(name="ping", description="Check bot latency!")
async def ping(interaction):
    await interaction.response.send_message(
        f"Pong! 🏓 Latency: {round(client.latency * 1000)}ms"
    )

client.run("YOUR_BOT_TOKEN")