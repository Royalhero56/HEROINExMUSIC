import asyncio
import random
from pyrogram import Client, filters
from pyrogram.enums import ChatType
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.errors import UserNotParticipant
from pyrogram.types import ChatPermissions
from AarohiX import app
from AarohiX.utils.top_ban import admin_filter

SPAM_CHATS = {}

@app.on_message(filters.command(["utag", "uall"], prefixes=["/", "@", ".", "#"]) & admin_filter)
async def tag_all_users(_, message):
    global SPAM_CHATS
    chat_id = message.chat.id
    if len(message.text.split()) == 1:
        await message.reply_text("** ɢɪᴠᴇ sᴏᴍᴇ ᴛᴇxᴛ ᴛᴏ ᴛᴀɢ ᴀʟʟ, ʟɪᴋᴇ »** `@utag Hi Friends`")
        return

    text = message.text.split(None, 1)[1]
    if text:
        await message.reply_text("**ᴜᴛᴀɢ [ᴜɴʟɪᴍɪᴛᴇᴅ ᴛᴀɢ] sᴛᴀʀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ!**\n\n**๏ ᴛᴀɢɢɪɴɢ ᴡɪᴛʜ sʟᴇᴇᴘ ᴏғ 7 sᴇᴄ.**\n\n**➥ ᴏғғ ᴛᴀɢɢɪɴɢ ʙʏ » /stoputag**")

    SPAM_CHATS[chat_id] = True
    f = True
    while f:
        if SPAM_CHATS.get(chat_id) == False:
            await message.reply_text("**ᴜɴʟɪᴍɪᴛᴇᴅ ᴛᴀɢɢɪɴɢ sᴜᴄᴄᴇssғᴜʟʟʏ sᴛᴏᴘᴘᴇᴅ.**")
            break
        usernum = 0
        usertxt = ""
        try:
            async for m in app.get_chat_members(message.chat.id):
                if m.user.is_bot:
                    continue
                usernum+= 1
                usertxt += f"\n⊚ [{m.user.first_name}](tg://user?id={m.user.id})\n"
                if usernum == 5:
                    await app.send_message(message.chat.id, f'{text}\n{usertxt}\n\n|| ➥ ᴏғғ ᴛᴀɢɢɪɴɢ ʙʏ » /stoputag ||')
                    usernum = 0
                    usertxt = ""
                    await asyncio.sleep(7)
        except Exception as e:
            print(e)

@app.on_message(filters.command(["stopmention", "offutag", "cancelutag", "utagstop", "stopall", "cancelmention", "offmention", "mentionoff", "alloff", "cancelall", "allcancel"], prefixes=["/", "@", "#"]) & admin_filter)
async def cancelcmd(_, message):
    chat_id = message.chat.id
    if chat_id in SPAM_CHATS:
        try :
            SPAM_CHATS.remove(chat_id)
        except Exception:
            pass   
        return await message.reply_text("**ᴛᴀɢɢɪɴɢ ᴘʀᴏᴄᴇss sᴜᴄᴄᴇssғᴜʟʟʏ sᴛᴏᴘᴘᴇᴅ!**")     
                                     
    else :
        await message.reply_text("**ɴᴏ ᴘʀᴏᴄᴇss ᴏɴɢᴏɪɴɢ!**")  
        return       
