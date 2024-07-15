import pickle
import os
from pyrogram import Client, filters
from pyrogram.types import Message

# Path to the pickle file
NOTES_FILE = "notes.pkl"

# Load existing notes if the pickle file exists
if os.path.exists(NOTES_FILE):
    with open(NOTES_FILE, "rb") as f:
        notes_db = pickle.load(f)
else:
    notes_db = {}

@Client.on_message(filters.command(["note"], "."))
async def add_note_command(client, message):
    try:
        command_parts = message.text.split(maxsplit=1)
        if len(command_parts) < 2:
            await message.reply("Usage: .note <your note>")
            return
        
        note_text = command_parts[1]
        user_id = str(message.from_user.id)
        
        if user_id not in notes_db:
            notes_db[user_id] = []
        
        notes_db[user_id].append(note_text)
        
        # Save notes to pickle file
        with open(NOTES_FILE, "wb") as f:
            pickle.dump(notes_db, f)
        
        await message.reply("Note added successfully.")
    except Exception as e:
        await message.reply("Failed to add note. Please try again.")
        print(e)

@Client.on_message(filters.command(["mynotes"], "."))
async def list_notes_command(client, message):
    user_id = str(message.from_user.id)
    if user_id in notes_db and notes_db[user_id]:
        notes_list = "\n\n".join([f"• {note}" for note in notes_db[user_id]])
        await message.reply(f"Your Notes:\n\n{notes_list}")
    else:
        await message.reply("You have no notes.")
