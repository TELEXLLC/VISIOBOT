# VISIOBOT

A professional Discord Music Promotion Bot with OpenAI-powered post writing, debugging, and advanced channel/thread scraping.  
**Includes a full-featured UI for easy control and configuration!**

---

## Features

- Professional Tkinter UI (with modern logo and color scheme)
- OpenAI-powered post writing and debugging assistant
- Post and DM with social/profile links
- Channel/thread scraper (for IDs and management)
- Error reporting/logging in UI and Discord
- Ready for EXE conversion (via PyInstaller)
- Secure config via `.env` file

---

## Security Notice

**Never share your Discord bot token or OpenAI API key publicly.**  
Your `.env` file is included for local use and is `.gitignore`'d for your safety.  
If you have shared your token, RESET IT IMMEDIATELY in the Discord Developer Portal.

---

## Installation

1. Clone the repo, then:
   ```
   pip install -r requirements.txt
   ```
2. Copy `.env.example` to `.env` and add your real tokens/keys.
3. Run the bot:
   ```
   python main.py
   ```
4. (Optional) Build EXE with PyInstaller:
   ```
   pip install pyinstaller
   pyinstaller --onefile --windowed main.py
   ```

---

## Folder Structure

- `main.py` - main app (bot + UI)
- `requirements.txt`
- `README.md`
- `.env.example` - (NOT committed - for your tokens/keys)
- `assets/` - logo and images
- `docs/` - documentation
- `input/` - for future data, CSVs, etc.
- `output/` - logs, exports, etc.

---

## Usage

- Launch the app, fill in your tokens and debug channel (if desired)
- Add social/profile links
- Use the UI or Discord commands:
  - `!add_profile NAME URL`
  - `!show_profiles`
  - `!ai_post your topic`
  - `!ai_debug your debug question`
  - `!promo message`
  - `!dm_all message`
  - `!post_thread THREAD_ID message`
  - `!list_channels`

---

## Placeholders

- `assets/logo.svg`: Brand logo (edit as you wish)
- `input/`, `output/`, `docs/`: For future expansion

---

## Contact

For help, see `docs/placeholder.md` or open an issue.
