import re, os, time
id_pattern = re.compile(r'^.\d+$') 

class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "27419615")
    API_HASH  = os.environ.get("API_HASH", "2f4b181296f0a2615a85471a1c72df44")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 

    # database config
    DATABASE_NAME = os.environ.get("DB_NAME","rohitl3031")     
    DATABASE_URL = os.environ.get("DB_URL","mongodb+srv://rohitl3031:CNHkZh4Nkgv0mUuJ@cluster0.cgmci.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
 
    # other configs
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "https://graph.org/file/569a3939dd41d05e861d4-9e20ec32e90cf14ab9.jpg")
    ADMIN       = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '1534632634').split()]
    FORCE_SUB   = os.environ.get("FORCE_SUB", "-1002608091887") 
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "1002093375923"))
    
    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", "True"))


class Txt(object):
    # part of text configuration
        
    START_TXT = """<b>›› ʜᴇʏ!!, {} ~ </b>

<b>➤ ᴡʜᴀᴛ ɪ ᴅᴏ:
ᴀᴅᴠᴀɴᴄᴇᴅ ꜰɪʟᴇ ʀᴇɴᴀᴍɪɴɢ ᴍᴀᴅᴇ ꜱɪᴍᴘʟᴇ & ꜱᴛʀᴇꜱꜱ-ꜰʀᴇᴇ.
ᴄᴜꜱᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟꜱ + ᴄᴀᴘᴛɪᴏɴꜱ ᴀʀᴇ ꜱᴜᴘᴘᴏʀᴛᴇᴅ.</b>

‣ ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : <a href="t.me/CodeifyBots">ᴄᴏᴅᴇɪғʏ ʙᴏᴛs</a></b>
<b>──────────────────</b>"""
    
    FILE_NAME_TXT = """<b><u>SETUP AUTO RENAME FORMAT</u></b>

Use These Keywords To Setup Custom File Name

✓ episode :- To Replace Episode Number
✓ quality :- To Replace Video Resolution

<b>Example :</b> <code> /autorename Naruto Shippuden S02 - EPepisode - quality  [Dual Audio] - @Madflix_Bots </code>

<b>Your Current Auto Rename Format :</b> <code>{format_template}</code> """
    
    ABOUT_TXT = f"""<b>╭───────────────⍟</b>
├<b>🤖 My Name</b> : {}
├<b>🖥️ Developer</b> : <a href=https://t.me/CodeifyBots>Codeify Bots</a> 
├<b>👨‍💻 Programer</b> : <a href=https://t.me/TgContactxBot>Veg3ta Sama </a>
├<b>📕 Library</b> : <a href=https://github.com/pyrogram>Pyrogram</a>
├<b>✏️ Language</b> : <a href=https://www.python.org>Python 3</a>
├<b>💾 Database</b> : <a href=https://cloud.mongodb.com>Mongo DB</a>
├<b>📊 Build Version</b> : <a href=https://t.me/Otaku_Atlas>Rename v1.0.0</a></b>     
<b>╰───────────────⍟</b>"""

    
    THUMBNAIL_TXT = """<b><u>🖼️  HOW TO SET THUMBNAIL</u></b>
    
⦿ You Can Add Custom Thumbnail Simply By Sending A Photo To Me....
    
⦿ /viewthumb - Use This Command To See Your Thumbnail
⦿ /delthumb - Use This Command To Delete Your Thumbnail"""

    CAPTION_TXT = """<b><u>📝  HOW TO SET CAPTION</u></b>
    
⦿ /set_caption - Use This Command To Set Your Caption
⦿ /see_caption - Use This Command To See Your Caption
⦿ /del_caption - Use This Command To Delete Your Caption"""

    PROGRESS_BAR = """\n
<b>📁 Size</b> : {1} | {2}
<b>⏳️ Done</b> : {0}%
<b>🚀 Speed</b> : {3}/s
<b>⏰️ ETA</b> : {4} """
    
    
    DONATE_TXT = """<b>🥲 Thanks For Showing Interest In Donation! ❤️</b>
    
If You Like My Bots & Projects, You Can 🎁 Donate Me Any Amount From 10 Rs Upto Your Choice.
    
<b>🛍 UPI ID:</b> <code>adding soon...</code> """
    
    HELP_TXT = """<b>Hey</b> {}
    
Here Is The Help For My Commands."""





# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Developer @JishuDeveloper

