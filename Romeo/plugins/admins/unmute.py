from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS
from Romeo.utils.romeomusic.rj import command
from Romeo import app
from Romeo.core.call import rj
from Romeo.utils.database import is_muted, mute_off
from Romeo.utils.decorators import AdminRightsCheck


@app.on_message(
    filters.command(["unmute", "cunmute"])
    & filters.group
    & ~BANNED_USERS
)
@AdminRightsCheck
async def unmute_admin(Client, message: Message, _, chat_id):
    if not len(message.command) == 1 or message.reply_to_message:
        return await message.reply_text("**❌ 𝐄𝐫𝐫𝐨𝐫, 𝐖𝐫𝐨𝐧𝐠 𝐔𝐬𝐚𝐠𝐞 𝐎𝐟 𝐂𝐨𝐦𝐦𝐚𝐧𝐝❗...**")
    if not await is_muted(chat_id):
        return await message.reply_text("**🔊 𝐀𝐥𝐫𝐞𝐚𝐝𝐲 𝐏𝐥𝐚𝐲𝐢𝐧𝐠 ✨ ...**")
    await mute_off(chat_id)
    await rj.unmute_stream(chat_id)
    await message.reply_text(
        "**🔊 𝐔𝐧𝐦𝐮𝐭𝐞𝐝 🌷 ...**".format(message.from_user.mention)
    )
