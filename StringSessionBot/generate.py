<<<<<<< HEAD
import Config
from LegendSS.Data import Data
=======
from Stringss.Data import Data
from Stringss.generate import ERROR_MESSAGE, generate_session
>>>>>>> 4c2a2ebd7331c35e9afbce1d9cf0d82854682ef9
from pyrogram import Client, filters
from pyrogram1 import Client as Client1
from telethon.sync import TelegramClient
from asyncio.exceptions import TimeoutError
from telethon.sessions import StringSession
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from telethon.tl.functions.channels import JoinChannelRequest, LeaveChannelRequest
from pyrogram.errors import (
    ApiIdInvalid, PhoneCodeExpired, PhoneCodeInvalid, PhoneNumberInvalid,
    PasswordHashInvalid, SessionPasswordNeeded
)
from telethon.errors import (
    ApiIdInvalidError, PhoneCodeExpiredError, PhoneCodeInvalidError,
    PhoneNumberInvalidError, PasswordHashInvalidError,
    SessionPasswordNeededError
)
from pyrogram1.errors import (
    ApiIdInvalid as ApiIdInvalid1, PhoneCodeExpired as PhoneCodeExpired1,
    PhoneCodeInvalid as PhoneCodeInvalid1,
    PhoneNumberInvalid as PhoneNumberInvalid1,
    PasswordHashInvalid as PasswordHashInvalid1,
    SessionPasswordNeeded as SessionPasswordNeeded1
)

gen_buttons = [
    [
        InlineKeyboardButton("⚜️ Pyrogram V1 ⚜️", callback_data="pyrogram1"),
        InlineKeyboardButton("✨Pyrogram V2 ✨", callback_data="pyrogram"),
    ],
    [
        InlineKeyboardButton("❤️ Telethon ♥️", callback_data="telethon"),
    ],
]


@Client.on_message(filters.private & ~filters.forwarded & filters.command("generate"))
async def main(_, msg):
    await msg.reply(
        "Please choose the python library you want to generate string session for",
        reply_markup=InlineKeyboardMarkup(gen_buttons),
    )
