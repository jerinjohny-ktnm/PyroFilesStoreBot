# (c) @AbirHasan2005

import os

class Config(object):
	API_ID = int(os.environ.get("API_ID"))
	API_HASH = os.environ.get("API_HASH")
	BOT_TOKEN = os.environ.get("BOT_TOKEN")
	BOT_USERNAME = os.environ.get("BOT_USERNAME")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL"))
	BOT_OWNER = int(os.environ.get("BOT_OWNER"))
	DATABASE_URL = os.environ.get("DATABASE_URL")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
	LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL"))
	ABOUT_BOT_TEXT = f"""
**This is Permanent Files Store Bot!**

```Send me any file I will save it in my Database. Also works for channel. Add me to channel as Admin with Edit Permission, I will add Save Uploaded File in Channel & add Sharable Button Link.```

🤖 **My Name:** [Store It](https://t.me/{BOT_USERNAME})

📝 **Language:** [Python3](https://www.python.org)

📚 **Library:** [Pyrogram](https://docs.pyrogram.org)

📡 **Hosted on:** [DigitalOcean](https://digitalocean.com)

🧑🏻‍💻 **Developer:** [Jerin](https://t.me/imjerin)
"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 **Developer:** @imjerin

Developer is Super Noob. Just Learning from Official Docs.

**Also remember that developer will Delete Adult Contents from Database. So better don't Store Those Kind of Things.**

"""
	HOME_TEXT = """
Hi, [{}](tg://user?id={})\n\n**Store It** Bot is a permanent file store bot.

```Send me any file I will give you a permanent Shareable Link. I Support Channel Also! Check 𝗔𝗯𝗼𝘂𝘁 𝗕𝗼𝘁 Button.```
"""
