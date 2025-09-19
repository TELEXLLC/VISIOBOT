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

## Quick Start: Using This Code for Your Bot

Follow these steps to get your Discord bot running using the code from this repository:

### 1. Clone the Repository

If you haven't already, open a terminal and run:
```bash
git clone https://github.com/TELEXLLC/VISIOBOT.git
```
Then enter the directory:
```bash
cd VISIOBOT
```

### 2. Install Dependencies

Install the required Python packages:
```bash
pip install -r requirements.txt
```

### 3. Configure the Bot

- Copy the example environment file and fill it in:
  ```bash
  cp .env.example .env
  ```
- Open `.env` in a text editor and enter your **Discord Bot Token**, **OpenAI API Key**, and any other required credentials.

### 4. Run the Bot

Start the bot by running:
```bash
python main.py
```

### 5. (Optional) Build an Executable

If you want to turn your bot into a standalone executable:
```bash
pip install pyinstaller
pyinstaller --onefile --windowed main.py
```
You'll find the executable in the `dist/` directory.

### 6. Customize the Code

- Open the files in your code editor (like VSCode, PyCharm, etc.).
- Make any changes or enhancements you need (e.g., commands, responses, UI tweaks).

### 7. Push Changes (if you want them in the repo)

If you want to save your changes to your own GitHub repository:
1. Commit your changes:
   ```bash
   git add .
   git commit -m "Describe your changes"
   ```
2. Push to your fork or the original repo:
   ```bash
   git push origin main
   ```
   *(Replace `main` with your branch name if needed.)*

---

**You’re ready to develop and launch your Discord bot using VISIOBOT!**

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
