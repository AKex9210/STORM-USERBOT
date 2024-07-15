import datetime
import pickle
import os
from pyrogram import filters
from pyrogram.types import Message

# Path to the pickle file
PICKLE_FILE = "reminders.pkl"

# Load existing reminders if the pickle file exists
if os.path.exists(PICKLE_FILE):
    with open(PICKLE_FILE, "rb") as f:
        reminders_db = pickle.load(f)
else:
    reminders_db = {}

@app.on_message(filters.command(["setreminder"], "."))
async def set_reminder_command(client, message):
    try:
        command_parts = message.text.split(maxsplit=2)
        if len(command_parts) < 3:
            raise ValueError("Usage: .setreminder <time> <text>")
        
        time_str = command_parts[1] + " " + command_parts[2]  # Combine time and text
        reminder_text = command_parts[3] if len(command_parts) > 3 else ""  # Get reminder text
        
        # Parse time string into datetime object
        reminder_time = datetime.datetime.strptime(time_str, "%I:%M %p")
        
        user_id = str(message.from_user.id)
        if user_id not in reminders_db:
            reminders_db[user_id] = []
        
        reminders_db[user_id].append({"time": reminder_time, "reminder": reminder_text})
        
        # Save reminders to pickle file
        with open(PICKLE_FILE, "wb") as f:
            pickle.dump(reminders_db, f)

        await message.reply(f"Reminder set for {reminder_time.strftime('%I:%M %p')} - {reminder_text}")
    except ValueError as ve:
        await message.reply(f"Error: {ve}")
    except Exception as e:
        await message.reply("An unexpected error occurred.")
        print(e)


@Client.on_message(filters.command(["reminders"], ".") & filters.private)
async def list_reminders(client: Client, msg: Message):
    try:
        user_id = str(msg.from_user.id)
        if user_id in reminders_db and reminders_db[user_id]:
            reminders_list = "\n".join([f"{reminder['time']} - {reminder['reminder']}" for reminder in reminders_db[user_id]])
            await msg.reply(f"Your reminders:\n\n{reminders_list}")
        else:
            await msg.reply("You have no reminders set.")
    except Exception as e:
        await msg.reply("An unexpected error occurred.")
        print(e)
