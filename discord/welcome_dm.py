@bot.event
async def on_member_join(member):
    try:
        await member.send(
            f"👋 Welcome to {member.guild.name}!\n"
            "Try `/help` or visit our website for more info 🚀"
        )
    except Exception as e:
        print(f"Couldn't DM {member}: {e}")