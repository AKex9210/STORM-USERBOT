import os
from pyrogram import Client, filters

# Initialize the Pyrogram Client
app = Client

# Define the trigger words for downloading self-destructing media
trigger_words = ["😋🥰", "op", "wow", "super", "😋😍"]

# Define a filter to process private messages from the user
@filters.private & filters.me
async def private_message_filter(_, __, message):
    return message

# Define the handler for processing messages containing trigger words
@app.on_message(filters.text & private_message_filter)
async def self_media_handler(client, message):
    try:
        # Check if the message is a reply
        replied = message.reply_to_message
        if not replied:
            return
        
        # Check if the replied message contains photo or video
        if not (replied.photo or replied.video):
            return
        
        # Download the media
        location = await client.download_media(replied)
        
        # Send the downloaded media as a document to saved messages
        await client.send_document("me", location)
        
        # Remove the downloaded media file
        os.remove(location)
    except Exception as e:
        # Print any errors that occur during processing
        print(f"Error: {e}")

# Run the Pyrogram Client
if __name__ == "__main__":
    app.run()
