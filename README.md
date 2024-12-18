# [roblox-state-notify-bot]([https://www.github.com/Qarchue/roblox-state-notify-bot](https://github.com/Qarchue/roblox-state-notify-bot))

<p align="center">
    <a href="https://github.com/Qarchue/roblox-state-notify-bot/blob/master/LICENSE"><img src="https://img.shields.io/github/license/qarchue/roblox-state-notify-bot"></a>
    <a href="https://github.com/Qarchue/roblox-state-notify-bot"><img src="https://img.shields.io/github/repo-size/Qarchue/roblox-state-notify-bot"></a>
    <a href="https://github.com/Qarchue/roblox-state-notify-bot"><img src="https://img.shields.io/github/languages/top/Qarchue/roblox-state-notify-bot"></a>
    <a href="https://github.com/Qarchue/roblox-state-notify-bot/stargazers"><img src="https://img.shields.io/github/stars/Qarchue/roblox-state-notify-bot?style=socia"></a>
    <a href="https://discord.gg/w5CeZh3rNu"><img src="https://img.shields.io/discord/905865794683015208?style=flat-square&logo=Discord&logoColor=white&label=support&color=5865F2"></a>
</p>

**English** | [中文](https://github.com/Qarchue/roblox-state-notify-bot/blob/main/README_tw.md)

> Feel free to use any or all of the code in your own bot.

Some players do not notify their friends when they come online, leading to missed opportunities to play together. To solve this problem, I developed a tool using **Python 3** to monitor their status changes and send real-time notifications.

This is a simple project that can monitor the status changes of specified players and notify you through Discord. You can also provide a Roblox Cookie to query more detailed information, such as when a player joins or leaves a game.

The bot also supports multilingual settings, allowing users to choose different languages for notifications based on their preferences. You can customize the language content by modifying or adding JSON files in the `language` folder.

_This document will guide you through creating a Discord bot and using its features._


###### Assisted by ChatGPT

---
# Supported Operating Systems

| OS |	Support|Tested|
| ------------- | ------- | ------- |
| Windows 11    |✅|✅|
| Windows 10    |✅|✅|
| Other Windows |❓| ❌|
| Linux         |❓| ❌|
| MacOS         |❓| ❌|


## Features

- [x] Notify through Discord when players come online, go offline, join, or leave a game.
- [x] Support Cookie verification to check if a player has joined or left a game.
- [x] Customizable language settings, supporting multilingual notifications.
- [x] Dynamically manage subscribed players, allowing adding or removing subscriptions through simple commands.

---

## Command Features

| **Command Name** | **Description** |
|------------------|-----------------|
| `/sublist`       | View the current list of subscribed players, showing all Roblox players you have subscribed to. |
| `/sub`           | Subscribe or unsubscribe specific players. You can subscribe or unsubscribe multiple players at once by separating their names or IDs with spaces. If you enter the name of a player you are already subscribed to, they will be unsubscribed. |
| `/setting`       | Change language settings or update the Cookie. You can choose to change the language or provide a new Cookie. If neither is provided, it will display the current settings. |

---

## Default Language

Currently, the `language` folder contains the following three default language files, which administrators can use directly or modify as needed:

| **Language Code** | **Language Name**    |
|-------------------|----------------------|
| `zh-tw`           | Traditional Chinese  |
| `en-us`           | English              |
| `lzh`             | Classical Chinese    |

The default language is set to `zh-tw`. If a user does not customize their language, this default language will be used.

---

## JSON Configuration Instructions

Below is the JSON file that needs to be created, along with an example of its content:

### 1. `settings.json`
**Location**: `configuration/settings.json`  
This file is used to configure the bot's Token and default language.  
Example content:
```json
{
    "TOKEN": "Your Discord Bot Token",
    "Default_language": "zh-tw"
}
```
- `TOKEN`: Enter the Bot Token you obtained from the Discord Developer Platform.
- `Default_language`: Enter the name of the default language file you want (e.g., zh-tw).

---

## Install Dependencies

Make sure Python 3.8 or a newer version is installed, then run the following command to install dependencies:

```sh
pip install -r requirements.txt
```

The `requirements.txt` file contains all the Python packages required to run this bot.

---

## Start the Bot

Run the following command to start the bot:

```sh
python bot.py
```

---

## Notes

### 1. Roblox Cookie Information
Providing a valid `.ROBLOSECURITY` Cookie enables advanced features to query player game status. If the player's privacy settings allow, the bot will display detailed game information; otherwise, it will only show the player's status changes.

### 2. Discord Permissions
Make sure the bot has the following basic permissions:
- Send Messages
- Embed Links
- Use Application Commands

### 3. Language Settings
The bot supports multilingual notifications. The default language determines the bot's command names and descriptions, but each user can set their own notification language. This way, when the bot notifies that user, it will use their specified language. Administrators can also modify or add languages by editing the JSON files in the `language` folder.

---

## Contributions

The inspiration and some code snippets for this project are from [here](https://github.com/jackssrt/robloxnotif/blob/master/README.md?plain=1).

Written by Qarchue during class. Your contributions can help make this bot even better!

---

## License

This project is licensed under the MIT License. For more details, please see the LICENSE file.

---
