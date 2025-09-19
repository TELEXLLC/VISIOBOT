import discord
from discord.ext import commands
import openai
import os
import sys
import threading
import traceback
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext, simpledialog
from dotenv import load_dotenv

# --- Load environment variables ---
load_dotenv()
DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
DEFAULT_PREFIX = "!"
SOCIAL_LINKS = {}

class VisioBotUI:
    def __init__(self, master):
        self.master = master
        master.title("VISIOBOT Music Promo Control Panel")
        master.geometry("600x600")
        master.configure(bg="#23272A")
        master.resizable(False, False)

        # Branding/logo
        try:
            self.logo_img = tk.PhotoImage(file="assets/logo.png")
            tk.Label(master, image=self.logo_img, bg="#23272A").pack(pady=8)
        except Exception:
            tk.Label(master, text="🎵 VISIOBOT", font=("Segoe UI", 24, "bold"), fg="#7289DA", bg="#23272A").pack(pady=8)

        self.token_label = tk.Label(master, text="Discord Bot Token:", fg="#ffffff", bg="#23272A")
        self.token_label.pack()
        self.token_entry = tk.Entry(master, width=60, show="*")
        self.token_entry.pack()
        self.token_entry.insert(0, DISCORD_BOT_TOKEN if DISCORD_BOT_TOKEN else "")

        self.openai_label = tk.Label(master, text="OpenAI API Key:", fg="#ffffff", bg="#23272A")
        self.openai_label.pack()
        self.openai_entry = tk.Entry(master, width=60, show="*")
        self.openai_entry.pack()
        self.openai_entry.insert(0, OPENAI_API_KEY if OPENAI_API_KEY else "")

        self.debug_channel_label = tk.Label(master, text="Debug Channel ID (optional):", fg="#ffffff", bg="#23272A")
        self.debug_channel_label.pack()
        self.debug_channel_entry = tk.Entry(master, width=60)
        self.debug_channel_entry.pack()

        # Social profile management
        prof_frame = tk.LabelFrame(master, text="Social/Profile Links", fg="#23272A", bg="#99AAB5", relief=tk.RIDGE)
        prof_frame.pack(pady=10, fill="x", padx=10)
        tk.Button(prof_frame, text="Add Link", command=self.add_profile_link).pack(side="left", padx=5)
        tk.Button(prof_frame, text="Show Links", command=self.show_profile_links).pack(side="left", padx=5)
        self.profiles_text = tk.Label(prof_frame, text="", fg="#23272A", bg="#99AAB5", anchor="w", justify="left")
        self.profiles_text.pack(pady=2, padx=5, fill="x")

        # Channel/thread scraper
        scrape_frame = tk.LabelFrame(master, text="Server Channel/Thread Scraper", fg="#23272A", bg="#99AAB5")
        scrape_frame.pack(pady=10, fill="x", padx=10)
        tk.Button(scrape_frame, text="List Channels/Threads", command=self.scrape_channels).pack(side="left", padx=6, pady=2)
        self.scrape_output = scrolledtext.ScrolledText(scrape_frame, width=65, height=5, state='disabled')
        self.scrape_output.pack(padx=5, pady=3)

        self.start_button = tk.Button(master, text="Start VISIOBOT", font=("Segoe UI", 14, "bold"),
                                      bg="#7289DA", fg="#ffffff", command=self.start_bot)
        self.start_button.pack(pady=15)

        tk.Label(master, text="VISIOBOT Log:", fg="#ffffff", bg="#23272A").pack()
        self.log = scrolledtext.ScrolledText(master, width=80, height=12, state='disabled', bg="#23272A", fg="#ffffff")
        self.log.pack(padx=10, pady=6)

        self.bot_ref = None

    def add_profile_link(self):
        name = simpledialog.askstring("Profile Name", "Enter profile or platform name (e.g. Spotify):", parent=self.master)
        url = simpledialog.askstring("Profile URL", "Enter the URL:", parent=self.master)
        if name and url:
            SOCIAL_LINKS[name] = url
            self.show_profile_links()

    def show_profile_links(self):
        if SOCIAL_LINKS:
            text = "\n".join([f"{k}: {v}" for k, v in SOCIAL_LINKS.items()])
        else:
            text = "No profiles added."
        self.profiles_text.config(text=text)

    def scrape_channels(self):
        if self.bot_ref and self.bot_ref.is_ready():
            output = []
            for guild in self.bot_ref.guilds:
                output.append(f"\n=== {guild.name} ({guild.id}) ===")
                for channel in guild.channels:
                    if isinstance(channel, discord.TextChannel):
                        output.append(f"  [Text] {channel.name} (ID: {channel.id})")
                        try:
                            threads = [t for t in self.bot_ref.get_all_threads() if t.parent_id == channel.id]
                            for t in threads:
                                output.append(f"    └─[Thread] {t.name} (ID: {t.id})")
                        except Exception:
                            pass
                    elif isinstance(channel, discord.VoiceChannel):
                        output.append(f"  [Voice] {channel.name} (ID: {channel.id})")
            self.scrape_output.config(state='normal')
            self.scrape_output.delete(1.0, tk.END)
            self.scrape_output.insert(tk.END, "\n".join(output))
            self.scrape_output.config(state='disabled')
        else:
            messagebox.showinfo("Bot not ready", "Please start the bot and wait until it is online.")

    def log_message(self, msg):
        self.log.configure(state='normal')
        self.log.insert(tk.END, msg + "\n")
        self.log.see(tk.END)
        self.log.configure(state='disabled')

    def start_bot(self):
        token = self.token_entry.get()
        openai_key = self.openai_entry.get()
        debug_id = self.debug_channel_entry.get()
        if not token or not openai_key:
            messagebox.showerror("Missing Info", "Enter Discord Bot Token and OpenAI API Key.")
            return
        self.start_button.config(state='disabled')
        threading.Thread(target=run_bot, args=(token, openai_key, debug_id, self), daemon=True).start()
        self.log_message("VISIOBOT starting...")

def run_bot(discord_token, openai_key, debug_channel_id, ui=None):
    intents = discord.Intents.all()
    bot = commands.Bot(command_prefix=DEFAULT_PREFIX, intents=intents)
    openai.api_key = openai_key

    try: debug_channel_id = int(debug_channel_id)
    except: debug_channel_id = None

    def log_debug(msg):
        print(msg)
        if ui:
            ui.log_message(msg)

    async def send_debug(msg):
        if debug_channel_id:
            channel = bot.get_channel(debug_channel_id)
            if channel:
                await channel.send(f"DEBUG: {msg}")

    @bot.event
    async def on_ready():
        msg = f"VISIOBOT is online as {bot.user}!"
        log_debug(msg)
        if ui:
            ui.bot_ref = bot
        await send_debug(msg)

    @bot.command()
    async def add_profile(ctx, name: str, link: str):
        SOCIAL_LINKS[name] = link
        await ctx.send(f"Added profile '{name}' with link: {link}")
        await ctx.send(social_links_str())

    @bot.command()
    async def show_profiles(ctx):
        await ctx.send(social_links_str())

    def social_links_str():
        if not SOCIAL_LINKS:
            return "No profiles added."
        return "\n".join([f"{k}: {v}" for k, v in SOCIAL_LINKS.items()])

    @bot.command()
    async def ai_post(ctx, *, topic):
        prompt = f"Write an engaging Discord post to promote music or an artist about: {topic}. Include a call to action."
        try:
            resp = openai.Completion.create(
                engine="text-davinci-003", prompt=prompt, max_tokens=100
            )
            post = resp.choices[0].text.strip()
            await ctx.send(post + "\n\n" + social_links_str())
        except Exception as e:
            await ctx.send("AI post generation failed.")
            await debug_error(e, ctx)

    @bot.command()
    async def ai_debug(ctx, *, question):
        prompt = f"You are a Discord bot assistant. User has this issue: {question}. Provide recommendations, debugging steps, or helpful insights."
        try:
            resp = openai.Completion.create(
                engine="text-davinci-003", prompt=prompt, max_tokens=150
            )
            answer = resp.choices[0].text.strip()
            await ctx.send(answer)
        except Exception as e:
            await ctx.send("AI debugging failed.")
            await debug_error(e, ctx)

    @bot.command()
    async def promo(ctx, *, message):
        await ctx.send(message + "\n\n" + social_links_str())

    @bot.command()
    async def dm_all(ctx, *, message):
        count = 0
        for member in ctx.guild.members:
            if not member.bot:
                try:
                    await member.send(message + "\n\n" + social_links_str())
                    count += 1
                except Exception:
                    continue
        await ctx.send(f"Sent DMs to {count} users.")

    @bot.command()
    async def post_thread(ctx, thread_id: int, *, message):
        thread = bot.get_channel(thread_id)
        if thread:
            await thread.send(message + "\n\n" + social_links_str())
            await ctx.send("Posted in thread.")
        else:
            await ctx.send("Thread not found.")

    @bot.command()
    async def list_channels(ctx):
        output = []
        for guild in bot.guilds:
            output.append(f"\n=== {guild.name} ({guild.id}) ===")
            for channel in guild.channels:
                if isinstance(channel, discord.TextChannel):
                    output.append(f"  [Text] {channel.name} (ID: {channel.id})")
                    threads = [t for t in bot.get_all_threads() if t.parent_id == channel.id]
                    for t in threads:
                        output.append(f"    └─[Thread] {t.name} (ID: {t.id})")
                elif isinstance(channel, discord.VoiceChannel):
                    output.append(f"  [Voice] {channel.name} (ID: {channel.id})")
        await ctx.send("```\n" + "\n".join(output) + "\n```")

    async def debug_error(error, ctx):
        tb = "".join(traceback.format_exception(type(error), error, error.__traceback__))
        await send_debug(f"Error: {error}\nTraceback:\n{tb}")
        if ctx:
            await ctx.send(f"Error occurred and was reported to debug log.")

    @bot.event
    async def on_command_error(ctx, error):
        await debug_error(error, ctx)

    try:
        bot.run(discord_token)
    except Exception as e:
        if ui:
            ui.log_message("Bot failed to start: " + str(e))
        else:
            print("Bot failed to start:", e)

def main():
    root = tk.Tk()
    style = ttk.Style()
    style.theme_use('clam')
    root.tk_setPalette(background='#23272A', foreground='#ffffff', activeBackground='#99AAB5')
    app = VisioBotUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()