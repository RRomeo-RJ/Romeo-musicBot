from datetime import datetime

from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS, MUSIC_BOT_NAME, PING_IMG_URL
from helper import get_command
from Romeo import app
from Romeo.core.call import rj
from Romeo.utils import bot_sys_stats
from Romeo.utils.decorators.language import language
import random
from Romeo.data import DE, DH, TE, TH 


@app.on_message(
    filters.command(["dareeng", "de"], ["/", "!"])
    & ~BANNED_USERS
)
@language
async def truth(client, message: Message, _):
    user = message.from_user.id
    userr = await client.get_users(message.from_user.id)
    mention = f"[{userr.first_name}](tg://user?id={userr.id})"
    await message.reply_text(f"{mention} {random.choice(DE)}")


@app.on_message(
    filters.command(["darehin", "dh"], ["/", "!"])
    & ~BANNED_USERS
)
@language
async def truth(client, message: Message, _):
    user = message.from_user.id
    userr = await client.get_users(message.from_user.id)
    mention = f"[{userr.first_name}](tg://user?id={userr.id})"
    await message.reply_text(f"{mention} {random.choice(DH)}")

@app.on_message(
    filters.command(["trutheng", "te"], ["/", "!"])
    & ~BANNED_USERS
)
@language
async def truth(client, message: Message, _):
    user = message.from_user.id
    userr = await client.get_users(message.from_user.id)
    mention = f"[{userr.first_name}](tg://user?id={userr.id})"
    await message.reply_text(f"{mention} {random.choice(TE)}")

@app.on_message(
    filters.command(["truthhin", "th"], ["/", "!"])
    & ~BANNED_USERS
)
@language
async def truth(client, message: Message, _):
    user = message.from_user.id
    userr = await client.get_users(message.from_user.id)
    mention = f"[{userr.first_name}](tg://user?id={userr.id})"
    await message.reply_text(f"{mention} {random.choice(TH)}")
