from pyrogram.types import Message
from pyrogram.enums import ChatType

from FallenMusic import app
from FallenMusic.Helpers.getid import get_file_id


@app.on_message(filters.command(["id", "stickerid", "stkid", "stckrid", f"id@{BOT_USERNAME}"]))
async def showid(_, message: Message):
    try:
        await message.delete()
    except:
        pass
    chat_type = message.chat.type

    if chat_type == ChatType.PRIVATE:
        user_id = message.chat.id
        await message.reply_text(f"`{user_id}`")

    elif chat_type in [ChatType.GROUP, ChatType.SUPERGROUP]:
        _id = ""
        _id += "**ᴄʜᴀᴛ ɪᴅ :** " f"`{message.chat.id}`\n"
        if message.reply_to_message:
            _id += (
                "**ʀᴇᴩʟɪᴇᴅ ᴜsᴇʀ ɪᴅ :** "
                f"`{message.reply_to_message.from_user.id}`\n"
            )
            file_info = get_file_id(message.reply_to_message)
        else:
            _id += "**ᴜsᴇʀ ɪᴅ :** " f"`{message.from_user.id}`\n"
            file_info = get_file_id(message)
        if file_info:
            _id += (
                f"<b>{file_info.message_type}</b>: "
                f"<code>{file_info.file_id}</code>\n"
            )
        await message.reply_text(_id)
