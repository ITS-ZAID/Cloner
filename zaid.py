import os
import re
import asyncio
import time
from pyrogram import *
from pyrogram.types import *

os.system("apt install git curl python3-pip ffmpeg -y")


API_ID = "6435225"
API_HASH = "4e984ea35f854762dcde906dce426c2d"
TOKEN = [i.strip() for i in os.environ.get("TOKEN").split(' ')]

ZAID = Client("ZPyro", api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN)

for phone in TOKEN:
    try:
        client = Client(":memory:", API_ID, API_HASH, bot_token=phone, plugins={"root": "handlers"})
        client.start()
    except Exception as e:
        print(f"**ERROR:** `{str(e)}`\nPress /start to Start again.")

idle()
