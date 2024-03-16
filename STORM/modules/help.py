from config import SUDO_USERS, HELP_PIC

from pyrogram import Client, filters
from pyrogram.types import Message

hl = "."

FIRST_TEXT = f"""
✨ **ʙᴏᴛ ʜᴇʟᴘ** ✨

**[ꜱᴛᴏʀᴍ ᴜꜱᴇʀʙᴏᴛ](https://t.me/Kexx_XD) ʜᴇʟᴘ ᴍᴇɴᴜ** 🥀

**ʜᴇʟᴘ ᴍᴇɴᴜ ᴘᴏᴡᴇʀᴇᴅ ʙʏ [ꜱᴛᴏʀᴍ](https://github.com/VARC9210/STORM-USERBOT)** ✨

**ᴄʜᴀɴɴᴇʟ: [ꜱᴛᴏʀᴍ ᴛᴇᴄʜ 🇮🇳](https://t.me/STORM_TECHH)**
**ꜱᴜᴘᴘᴏʀᴛ: [ꜱᴛᴏʀᴍ ᴄʜᴀᴛᴢ 🇮🇳](https://t.me/STORM_CHATZ)**

**» ᴇxᴛʀᴀ ᴄᴏᴍᴍᴀɴᴅꜱ:** `{hl}help extra`  
**» ꜱᴘᴀᴍ ᴄᴏᴍᴍᴀɴᴅꜱ:** `{hl}help spam` 
**» ᴅᴍ ᴄᴏᴍᴍᴀɴᴅꜱ:** `{hl}help dm`
**» ʟᴏᴠᴇ ᴄᴏᴍᴍᴀɴᴅꜱ:** `{hl}help love`
**» ꜰᴜɴ ᴄᴏᴍᴍᴀɴᴅꜱ:** `{hl}help fun`
**» ɴᴇᴡꜱ ᴄᴏᴍᴍᴀɴᴅꜱ:** `{hl}help news`
**» ᴄᴏɴᴠᴇʀᴛ ᴄᴏᴍᴍᴀɴᴅꜱ:** `{hl}help convert`
**» ɪɴꜰᴏ ᴄᴏᴍᴍᴀɴᴅꜱ:** `{hl}help info`
**» ᴄʀᴇᴀᴛᴇ ᴄᴏᴍᴍᴀɴᴅꜱ:** `{hl}help create`
"""

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["help"], ["."]))
async def help(xspam: Client, msg: Message):
       if ".jpg" in HELP_PIC or ".png" in HELP_PIC:
              await xspam.send_photo(msg.chat.id, HELP_PIC, caption=FIRST_TEXT)
       if ".mp4" in HELP_PIC or ".MP4," in HELP_PIC:
              await xspam.send_video(msg.chat.   id, HELP_PIC, caption=FIRST_TEXT)
