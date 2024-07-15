import datetime
import pickle
import os
from pyrogram import Client, filters
from pyrogram.types import Message
from config import API_ID, API_HASH, SUDO_USERS

# Path to the pickle file
PICKLE_FILE = "reminders.pkl"

# Load existing reminders if the pickle file exists
if os.path.exists(PICKLE_FILE):
    with open(PICKLE_FILE, "rb") as f:
        reminders_db = pickle.load(f)
else:
    reminders_db = {}

@Client.on_message(filters.command(["setreminder"], ".") & filters.private)
async def set_reminder(client: Client, msg: Message):
    try:
        parts = msg.text.split(maxsplit=2)
        time_str = parts[1]
        reminder_text = parts[2]
        
        user_id = str(msg.from_user.id)
        if user_id not in reminders_db:
            reminders_db[user_id] = []
        
        reminders_db[user_id].append({"time": time_str, "reminder": reminder_text})
        
        # Save reminders to pickle file
        with open(PICKLE_FILE, "wb") as f:
            pickle.dump(reminders_db, f)

        await msg.reply(f"Reminder set for {time_str}: {reminder_text}")
    except Exception as e:
        await msg.reply("Usage: .setreminder <time> <reminder>")
        print(e)

@Client.on_message(filters.command(["reminders"], ".") & filters.private)
async def list_reminders(client: Client, msg: Message):
    user_id = str(msg.from_user.id)
    if user_id in reminders_db and reminders_db[user_id]:
        reminders_list = "\n".join([f"{reminder['time']} - {reminder['reminder']}" for reminder in reminders_db[user_id]])
        await msg.reply(f"Your reminders:\n\n{reminders_list}")
    else:
        await msg.reply("You have no reminders set.")
