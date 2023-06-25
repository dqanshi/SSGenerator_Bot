from pyrogram import Client, filters


@app.on_message(filters.command("getlink"))
def get_link(client, message):
    # Check if the message has a parameter
    if len(message.command) < 2:
        message.reply_text("Please provide a chat ID.")
        return

    # Get the chat ID from the command
    chat_id = message.command[1]

    try:
        # Get information about the chat
        chat = client.get_chat(chat_id)

        invite_link = client.export_chat_invite_link(chat_id)
        if invite_link.invite_link:
            message.reply_text(f"Invite link for chat {chat.title}: {invite_link.invite_link}")
        else:
            invite_link = client.create_chat_invite_link(chat_id)
            message.reply_text(f"Invite link created for chat {chat.title}: {invite_link.link}")

    except Exception as e:
        message.reply_text(f"Error: {e}")
