<div align="center">
# <img src="https://cdn.jsdelivr.net/gh/twitter/twemoji@latest/assets/72x72/1f916.png" width="30"> Discord.py Starter Kit
**A comprehensive sample of Discord bot response types for beginners..**
Learn how to communicate with users through text, rich media, and interactive components.
![Python](https://img.shields.io/badge/-Python-black?style=flat-square&logo=Python)
![discord.py](https://img.shields.io/badge/-discord.py-5865F2?style=flat-square&logo=discord&logoColor=white)
</div>
---
## Table of Contents
- [Message Types](#-message-types-included)
- [Project Structure](#-project-structure)
- [Setup & Installation](#%EF%B8%8F-setup--installation)
- [How to Use](#-how-to-use-these-samples)
- [Security](#-security)
---
## Message Types Included
| **Feature** | **Description** |
| :--- | :--- |
| **Plain Text** | Standard, unformatted messages. |
| **Embed** | Structured, rich-text message block, which can include; colored borders, images, titles, and fields. |
| **Component** | Interactive elements like buttons, menus, and text inputs. |
| **Modal** | Pop-up form that allows bots to collect text input from users. |
| **Ephemeral** | Messages that only the user who triggered the command can see. |
---
## Project Structure
Each message type is split into **two files** to help you learn:

| File | Purpose |
| :--- | :--- |
| `bot.py` | Plain code |
| `guided_bot.py` | Guided code with documentation and labels |
| `.env` | Private Config: Keeps your Bot Token & secrets hidden from the main file |
| `.gitignore` | Tells Git which files to ignore |
| `requirements.txt` | Dependencies Library: All required packages & their specific versions |
---
## Setup & Installation
### Prerequisites
- [Python 3.8+](https://www.python.org/downloads/)
- A [Discord Bot Token](https://discord.com/developers/applications)
### 1. Clone the Repository
```bash
git clone https://github.com/your-username/discord-bot-starter.git
cd discord-bot-starter
```
### 2. Install Requirements
```bash
pip install -r requirements.txt
```
### 3. Configure Your Secrets
Create a file named `.env` in the root directory and add your bot token:
```env
DISCORD_TOKEN=your_discord_bot_token
```
### 4. Run the Bot
```bash
python bot.py
```
> You should see your bot come online in your Discord server!
---
## How to Use These Samples
1. **Read** the `guided_bot.py` file first to understand the logic.
2. **Test** the command in your Discord server to see the visual result.
3. **Build** — once you're comfortable, use the `bot.py` code as a template for your own custom features!
---
## Security
> **The #1 Rule:** Never share your `.env` file or your Bot Token.
- The `.env` file is automatically ignored by Git (via `.gitignore`) to prevent accidental leaks.
- If you ever accidentally expose your token (screen share, screenshot, etc.), go to the **[Discord Developer Portal](https://discord.com/developers/applications)** and click **Reset Token** immediately.
---
<div align="center">
**Made by [@mqgh](https://discord.com/users/1231474833213362176)**
</div>
