# Don't Remove Credit @CodeFlix_Bots, @rohit_1888
# Ask Doubt on telegram @CodeflixSupport
#
# Copyright (C) 2025 by Codeflix-Bots@Github, < https://github.com/Codeflix-Bots >.
#
# This file is part of < https://github.com/Codeflix-Bots/FileStore > project,
# and is released under the MIT License.
# Please see < https://github.com/Codeflix-Bots/FileStore/blob/master/LICENSE >
#
# All rights reserved.
#

import os
from os import environ,getenv
import logging
from logging.handlers import RotatingFileHandler

#rohit_1888 on Tg
#--------------------------------------------
#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "8154426339:")
APP_ID = int(os.environ.get("APP_ID", "24798261")) #Your API ID from my.telegram.org
API_HASH = os.environ.get("API_HASH", "fef280037f5759eccc540c6d7a279a14") #Your API Hash from my.telegram.org
#--------------------------------------------

CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002540604882")) #Your db channel Id
OWNER = os.environ.get("OWNER", "HKOWNER0") # Owner username without @
OWNER_ID = int(os.environ.get("OWNER_ID", "6155478725")) # Owner id
#--------------------------------------------
PORT = os.environ.get("PORT", "8001")
#--------------------------------------------
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://rajeshpro123321:Vs9n8R90yUtCIyu4@clonestore1.w51yrrp.mongodb.net/?retryWrites=true&w=majority&appName=clonestore1")
DB_NAME = os.environ.get("DATABASE_NAME", "clonestore1")
#--------------------------------------------
FSUB_LINK_EXPIRY = int(os.getenv("FSUB_LINK_EXPIRY", "0"))  # 0 means no expiry
BAN_SUPPORT = os.environ.get("BAN_SUPPORT", "https://t.me/HKOWNER0")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "200"))
#--------------------------------------------
START_PIC = os.environ.get("START_PIC", "https://envs.sh/eAF.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://envs.sh/eAF.jpg")

#--------------------------------------------
SHORTLINK_URL = os.environ.get("SHORTLINK_URL", "ATGLinks.com")
SHORTLINK_API = os.environ.get("SHORTLINK_API", "49e836a49e2662195606e80119e468680ae90edf")
VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE', 86400)) # Add time in seconds
TUT_VID = os.environ.get("TUT_VID","https://t.me/hwdownload/3")
SHORT_MSG = "<b>⌯ Here is Your Download Link, Must Watch Tutorial Before Clicking On Download...</b>"

SHORTENER_PIC = os.environ.get("SHORTENER_PIC", "https://envs.sh/eAF.jpg")
#--------------------------------------------

#--------------------------------------------
HELP_TXT = "<b><blockquote>ᴛʜɪs ɪs ᴀɴ ғɪʟᴇ ᴛᴏ ʟɪɴᴋ ʙᴏᴛ ᴡᴏʀᴋ ғᴏʀ @HKOWNER0\n\n❏ ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅs\n├/start : sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ\n├/about : ᴏᴜʀ Iɴғᴏʀᴍᴀᴛɪᴏɴ\n└/help : ʜᴇʟᴘ ʀᴇʟᴀᴛᴇᴅ ʙᴏᴛ\n\n sɪᴍᴘʟʏ ᴄʟɪᴄᴋ ᴏɴ ʟɪɴᴋ ᴀɴᴅ sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ ᴊᴏɪɴ ʙᴏᴛʜ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ ᴛʜᴀᴛs ɪᴛ.....!\n\n ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ <a href=https://t.me/Hkowner0>HK</a></blockquote></b>"
ABOUT_TXT = "<b><blockquote>◈ ᴄʀᴇᴀᴛᴏʀ: <a href=https://t.me/HKOWNER0>HK</a>\n◈ ꜰᴏᴜɴᴅᴇʀ ᴏꜰ : <a href=https://t.me/+HF8TKtMMySw5MjY1>𝗛𝗞 𝗢𝗙𝗙𝗜𝗖𝗜𝗔𝗟™</a>\n◈ ᴅᴇᴠᴇʟᴏᴘᴇʀ : <a href=https://t.me/HKOWNER0>HK</a></blockquote></b>"
#--------------------------------------------
#--------------------------------------------
START_MSG = os.environ.get("START_MESSAGE", "<b>HELLO!! {first}\n\n I Am 𝗛𝗞 𝗢𝗙𝗙𝗜𝗖𝗜𝗔𝗟™ 😊store bot You will get here Study Material by links🔗 which will be provided in channels✅⭐️..</blockquote></b>")
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "👋Hello {first}\n\n<b>🪴You need to join in my both below mention channels😊 to get lectures📽️\n\n🎀Kindly Please join Channels\n\n📍And Click on try again or go on post link again\n\nThankyou💕🪴\n\n📍𝗛𝗞 𝗢𝗙𝗙𝗜𝗖𝗜𝗔𝗟™~.</b>")

CMD_TXT = """<blockquote><b>» ᴀᴅᴍɪɴ ᴄᴏᴍᴍᴀɴᴅs:</b></blockquote>

<b>›› /dlt_time :</b> sᴇᴛ ᴀᴜᴛᴏ ᴅᴇʟᴇᴛᴇ ᴛɪᴍᴇ
<b>›› /check_dlt_time :</b> ᴄʜᴇᴄᴋ ᴄᴜʀʀᴇɴᴛ ᴅᴇʟᴇᴛᴇ ᴛɪᴍᴇ
<b>›› /dbroadcast :</b> ʙʀᴏᴀᴅᴄᴀsᴛ ᴅᴏᴄᴜᴍᴇɴᴛ / ᴠɪᴅᴇᴏ
<b>›› /ban :</b> ʙᴀɴ ᴀ ᴜꜱᴇʀ
<b>›› /unban :</b> ᴜɴʙᴀɴ ᴀ ᴜꜱᴇʀ
<b>›› /banlist :</b> ɢᴇᴛ ʟɪsᴛ ᴏꜰ ʙᴀɴɴᴇᴅ ᴜꜱᴇʀs
<b>›› /addchnl :</b> ᴀᴅᴅ ꜰᴏʀᴄᴇ sᴜʙ ᴄʜᴀɴɴᴇʟ
<b>›› /delchnl :</b> ʀᴇᴍᴏᴠᴇ ꜰᴏʀᴄᴇ sᴜʙ ᴄʜᴀɴɴᴇʟ
<b>›› /listchnl :</b> ᴠɪᴇᴡ ᴀᴅᴅᴇᴅ ᴄʜᴀɴɴᴇʟs
<b>›› /fsub_mode :</b> ᴛᴏɢɢʟᴇ ꜰᴏʀᴄᴇ sᴜʙ ᴍᴏᴅᴇ
<b>›› /pbroadcast :</b> sᴇɴᴅ ᴘʜᴏᴛᴏ ᴛᴏ ᴀʟʟ ᴜꜱᴇʀs
<b>›› /add_admin :</b> ᴀᴅᴅ ᴀɴ ᴀᴅᴍɪɴ
<b>›› /deladmin :</b> ʀᴇᴍᴏᴠᴇ ᴀɴ ᴀᴅᴍɪɴ
<b>›› /admins :</b> ɢᴇᴛ ʟɪsᴛ ᴏꜰ ᴀᴅᴍɪɴs
<b>›› /addpremium :</b> ᴀᴅᴅ ᴀ ᴘʀᴇᴍɪᴜᴍ ᴜꜱᴇʀ
<b>›› /premium_users :</b> ʟɪsᴛ ᴀʟʟ ᴘʀᴇᴍɪᴜᴍ ᴜꜱᴇʀs
<b>›› /remove_premium :</b> ʀᴇᴍᴏᴠᴇ ᴘʀᴇᴍɪᴜᴍ ꜰʀᴏᴍ ᴀ ᴜꜱᴇʀ
<b>›› /myplan :</b> ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴘʀᴇᴍɪᴜᴍ sᴛᴀᴛᴜs
<b>›› /count :</b> ᴄᴏᴜɴᴛ verifications
"""
#--------------------------------------------
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None) #set your Custom Caption here, Keep None for Disable Custom Caption
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "True") == "True" else False #set True if you want to prevent users from forwarding files from bot
#--------------------------------------------
#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'
#--------------------------------------------
BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly Dm here if u have any problem @HKOWNER0"

#==========================(BUY PREMIUM)====================#

OWNER_TAG = os.environ.get("OWNER_TAG", "@HKOWNER0")
UPI_ID = os.environ.get("UPI_ID", "Contact me With Your Plan :- @HKOWNER0")
QR_PIC = os.environ.get("QR_PIC", "https://envs.sh/eAF.jpg")
SCREENSHOT_URL = os.environ.get("SCREENSHOT_URL", f"t.me/HKOWNER0")
#--------------------------------------------
#Time and its price
#7 Days
PRICE1 = os.environ.get("PRICE1", "10 rs")
#1 Month
PRICE2 = os.environ.get("PRICE2", "30 rs")
#3 Month
PRICE3 = os.environ.get("PRICE3", "80 rs")
#6 Month
PRICE4 = os.environ.get("PRICE4", "150 rs")
#1 Year
PRICE5 = os.environ.get("PRICE5", "300 rs")

#===================(END)========================#

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   
