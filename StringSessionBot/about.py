import subprocess
import importlib

# Install required packages
subprocess.check_call(["pip", "install", "-r", "requirements.txt"])
from pyStringss.Data import Data

# Import other necessary modules
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup


@Client.on_message(filters.private & filters.incoming & filters.command("about"))
async def about(bot, msg):
    await bot.send_message(
        msg.chat.id,
        Data.ABOUT,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(Data.home_buttons),
    )

