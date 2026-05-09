from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from VIVAANXMUSIC import app
from config import BOT_USERNAME

repo_caption = """**
🚀 ᴄʟᴏɴᴇ ᴀɴᴅ ᴅᴇᴘʟᴏʏ – BETA BOT 𝐍ᴇᴛᴡᴏʀᴋ  🚀

➤ ᴅᴇᴘʟᴏʏ ᴇᴀsɪʟʏ ᴏɴ ʜᴇʀᴏᴋᴜ ᴡɪᴛʜᴏᴜᴛ ᴇʀʀᴏʀꜱ  
➤ ɴᴏ ʜᴇʀᴏᴋᴜ ʙᴀɴ ɪꜱꜱᴜᴇ  
➤ ɴᴏ ɪᴅ ʙᴀɴ ɪꜱꜱᴜᴇ  
➤ ᴜɴʟɪᴍɪᴛᴇᴅ ᴅʏɴᴏꜱ  
➤ ʀᴜɴ 24/7 ʟᴀɢ ꜰʀᴇᴇ

ɪꜰ ʏᴏᴜ ꜰᴀᴄᴇ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ, ꜱᴇɴᴅ ꜱꜱ ɪɴ ꜱᴜᴘᴘᴏʀᴛ
**"""

@app.on_message(filters.command("repo"))
async def show_repo(_, msg):
    buttons = [
        [InlineKeyboardButton("➕ ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ ✨", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [
            InlineKeyboardButton("👑 ᴏᴡɴᴇʀ", url="https://t.me/ll_DEVIL_SHIV_ll"),
            InlineKeyboardButton("💬 ꜱᴜᴘᴘᴏʀᴛ", url="https://t.me/betabot_hub")
        ],
        [
            InlineKeyboardButton("🛠️ ꜱᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ", url="https://t.me/betabot_support"),
        ]
    ]

    reply_markup = InlineKeyboardMarkup(buttons)

    try:  
        await msg.reply_photo(
            photo="https://files.catbox.moe/ubyk6k.jpg",
            caption=repo_caption,
            reply_markup=reply_markup
        )
    except:
        pass
