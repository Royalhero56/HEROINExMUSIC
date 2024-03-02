from pyrogram import Client, filters
import requests
import random
import os
import re
import asyncio
import time
from AarohiX import app

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@app.on_message(
    filters.command("owner")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/fbb992b2477e3ecd09fc0.jpg",
        caption=f"""🍁𝐂𝐋𝐈𝐂𝐊🥰𝐁𝐄𝐋𝐎𝐖💝𝐁𝐔𝐓𝐓𝐎𝐍✨𝐓𝐎🙊𝐃𝐌❤️𝐎𝐖𝐍𝐄𝐑🍁""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌹 𝐋𝐔𝐂𝐊𝐘 𝐑𝐀𝐉𝐀 🌹", url=f"https://t.me/itz_Lucky_Raja")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command(GBANNED_COMMAND)
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/fbb992b2477e3ecd09fc0.jpg",
        caption=f"""**◈ 𝐓𝙷𝙸𝚂 𝐂𝙾𝙼𝙼𝙰𝙽𝙳 𝐈𝚂 𝐎𝙽𝙻𝚈 𝐅𝙾𝚁 𝐒𝚄𝙳𝙾 𝐔𝚂𝙴𝚁𝚂 𝐁𝙰𝙱𝚈..**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "•─╼⃝𖠁𝐎𝐔𝐑 𝐆𝐑𝐎𝐔𝐏𖠁⃝╾─•", url=f"https://t.me/+WDNH4yTCWe5jOTI1")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command(GBANNED_COMMAND)
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/fbb992b2477e3ecd09fc0.jpg",
        caption=f"""**◈ 𝐓𝙷𝙸𝚂 𝐂𝙾𝙼𝙼𝙰𝙽𝙳 𝐈𝚂 𝐎𝙽𝙻𝚈 𝐅𝙾𝚁 𝐒𝚄𝙳𝙾 𝐔𝚂𝙴𝚁𝚂 𝐁𝙰𝙱𝚈..**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "•─╼⃝𖠁𝐎𝐔𝐑 𝐆𝐑𝐎𝐔𝐏 𖠁⃝╾─•", url=f"https://t.me/+WDNH4yTCWe5jOTI1")
                ]
            ]
        ),
    )
    
@app.on_message(
    filters.command("owner")
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/fbb992b2477e3ecd09fc0.jpg",
        caption=f"""🍁𝐂𝐋𝐈𝐂𝐊🥰𝐁𝐄𝐋𝐎𝐖💝𝐁𝐔𝐓𝐓𝐎𝐍✨𝐓𝐎🙊𝐃𝐌❤️𝐎𝐖𝐍𝐄𝐑🍁""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌹 𝐋𝐔𝐂𝐊𝐘 𝐑𝐀𝐉𝐀 🌹", url=f"https://t.me/itz_Lucky_Raja")
                ]
            ]
        ),
    )






@app.on_message(
    filters.command("repo")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/fbb992b2477e3ecd09fc0.jpg",
        caption=f"""🍁𝐂𝐋𝐈𝐂𝐊🥰𝐁𝐄𝐋𝐎𝐖💝𝐁𝐔𝐓𝐓𝐎𝐍✨𝐓𝐎🙊𝐆𝐄𝐓🌱𝐑𝐄𝐏𝐎🍁""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌱ƨσʋяcɛ🌱", url=f"https://t.me/ZiddiXBot")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command("source")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/fbb992b2477e3ecd09fc0.jpg",
        caption=f"""🍁𝐂𝐋𝐈𝐂𝐊🥰𝐁𝐄𝐋𝐎𝐖💝𝐁𝐔𝐓𝐓𝐎𝐍✨𝐓𝐎🙊𝐆𝐄𝐓🌱𝐑𝐄𝐏𝐎🍁""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌱ƨσʋяcɛ🌱", url=f"https://t.me/ZiddiXBot")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command("repo")
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/fbb992b2477e3ecd09fc0.jpg",
        caption=f"""🍁𝐂𝐋𝐈𝐂𝐊🥰𝐁𝐄𝐋𝐎𝐖💝𝐁𝐔𝐓𝐓𝐎𝐍✨𝐓𝐎🙊𝐆𝐄𝐓🌱𝐑𝐄𝐏𝐎🍁""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌱ƨσʋяcɛ🌱", url=f"https://t.me/ZiddiXBot")
                ]
            ]
        ),
    )

#Must Learn 

@app.on_message(
    filters.command(PLAY_COMMAND)
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/fbb992b2477e3ecd09fc0.jpg",
        caption=f"""**◈ 𝐓𝙷𝙸𝚂 𝐂𝙾𝙼𝙼𝙰𝙽𝙳 𝐔𝚂𝙴 𝐈𝙽 𝐎𝙽𝙻𝚈 𝐆𝚁𝙾𝚄𝙿𝚂 𝐁𝙰𝙱𝚈 **\n**◈ 𝐆𝙾 𝐓𝙾 𝐆𝚁𝙾𝚄𝙿𝚂/𝐀𝙳𝙳 𝐌𝙴 𝐈𝙽 𝐆𝚁𝙾𝚄𝙿𝚂 𝐀𝙽𝙳 𝐔𝚂𝙴 /play 𝐂𝙾𝙼𝙼𝙰𝙽𝙳.**\n**◈ 𝐓𝙷𝙰𝙽𝙺 𝐔𝙷 𝐁𝙰𝙱𝚈.**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "•─╼⃝𖠁𝐎𝐔𝐑 𝐆𝐑𝐎𝐔𝐏 𖠁⃝╾─•", url=f"https://t.me/+WDNH4yTCWe5jOTI1")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command(GSTATS_COMMAND)
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/fbb992b2477e3ecd09fc0.jpg",
        caption=f"""**◈ 𝐓𝙷𝙸𝚂 𝐂𝙾𝙼𝙼𝙰𝙽𝙳 𝐔𝚂𝙴 𝐈𝙽 𝐎𝙽𝙻𝚈 𝐆𝚁𝙾𝚄𝙿𝚂 𝐁𝙰𝙱𝚈 **\n**◈ 𝐆𝙾 𝐓𝙾 𝐆𝚁𝙾𝚄𝙿𝚂/𝐀𝙳𝙳 𝐌𝙴 𝐈𝙽 𝐆𝚁𝙾𝚄𝙿𝚂 𝐀𝙽𝙳 𝐔𝚂𝙴 /gstats 𝐂𝙾𝙼𝙼𝙰𝙽𝙳.**\n**◈ 𝐓𝙷𝙰𝙽𝙺 𝐔𝙷 𝐁𝙰𝙱𝚈.**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "•─╼⃝𖠁𝐎𝐔𝐑 𝐆𝐑𝐎𝐔𝐏 𖠁⃝╾─•", url=f"https://t.me/+WDNH4yTCWe5jOTI1")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command(PAUSE_COMMAND)
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/fbb992b2477e3ecd09fc0.jpg",
        caption=f"""**◈ 𝐓𝙷𝙸𝚂 𝐂𝙾𝙼𝙼𝙰𝙽𝙳 𝐔𝚂𝙴 𝐈𝙽 𝐎𝙽𝙻𝚈 𝐆𝚁𝙾𝚄𝙿𝚂 𝐁𝙰𝙱𝚈 **\n**◈ 𝐆𝙾 𝐓𝙾 𝐆𝚁𝙾𝚄𝙿𝚂/𝐀𝙳𝙳 𝐌𝙴 𝐈𝙽 𝐆𝚁𝙾𝚄𝙿𝚂 𝐀𝙽𝙳 𝐔𝚂𝙴 /pause 𝐂𝙾𝙼𝙼𝙰𝙽𝙳.**\n**◈ 𝐓𝙷𝙰𝙽𝙺 𝐔𝙷 𝐁𝙰𝙱𝚈.**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "•─╼⃝𖠁𝐎𝐔𝐑 𝐆𝐑𝐎𝐔𝐏 𖠁⃝╾─•", url=f"https://t.me/+WDNH4yTCWe5jOTI1")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command(REBOOT_COMMAND)
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/fbb992b2477e3ecd09fc0.jpg",
        caption=f"""**◈ 𝐓𝙷𝙸𝚂 𝐂𝙾𝙼𝙼𝙰𝙽𝙳 𝐔𝚂𝙴 𝐈𝙽 𝐎𝙽𝙻𝚈 𝐆𝚁𝙾𝚄𝙿𝚂 𝐁𝙰𝙱𝚈 **\n**◈ 𝐆𝙾 𝐓𝙾 𝐆𝚁𝙾𝚄𝙿𝚂/𝐀𝙳𝙳 𝐌𝙴 𝐈𝙽 𝐆𝚁𝙾𝚄𝙿𝚂 𝐀𝙽𝙳 𝐔𝚂𝙴 /reboot 𝐂𝙾𝙼𝙼𝙰𝙽𝙳.**\n**◈ 𝐓𝙷𝙰𝙽𝙺 𝐔𝙷 𝐁𝙰𝙱𝚈.**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "•─╼⃝𖠁𝐎𝐔𝐑 𝐆𝐑𝐎𝐔𝐏 𖠁⃝╾─•", url=f"https://t.me/+WDNH4yTCWe5jOTI1")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command(STOP_COMMAND)
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/fbb992b2477e3ecd09fc0.jpg",
        caption=f"""**◈ 𝐓𝙷𝙸𝚂 𝐂𝙾𝙼𝙼𝙰𝙽𝙳 𝐔𝚂𝙴 𝐈𝙽 𝐎𝙽𝙻𝚈 𝐆𝚁𝙾𝚄𝙿𝚂 𝐁𝙰𝙱𝚈 **\n**◈ 𝐆𝙾 𝐓𝙾 𝐆𝚁𝙾𝚄𝙿𝚂/𝐀𝙳𝙳 𝐌𝙴 𝐈𝙽 𝐆𝚁𝙾𝚄𝙿𝚂 𝐀𝙽𝙳 𝐔𝚂𝙴 /stop 𝐂𝙾𝙼𝙼𝙰𝙽𝙳.**\n**◈ 𝐓𝙷𝙰𝙽𝙺 𝐔𝙷 𝐁𝙰𝙱𝚈.**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "•─╼⃝𖠁𝐎𝐔𝐑 𝐆𝐑𝐎𝐔𝐏 𖠁⃝╾─•", url=f"https://t.me/+WDNH4yTCWe5jOTI1")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command(SKIP_COMMAND)
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/fbb992b2477e3ecd09fc0.jpg",
        caption=f"""**◈ 𝐓𝙷𝙸𝚂 𝐂𝙾𝙼𝙼𝙰𝙽𝙳 𝐔𝚂𝙴 𝐈𝙽 𝐎𝙽𝙻𝚈 𝐆𝚁𝙾𝚄𝙿𝚂 𝐁𝙰𝙱𝚈 **\n**◈ 𝐆𝙾 𝐓𝙾 𝐆𝚁𝙾𝚄𝙿𝚂/𝐀𝙳𝙳 𝐌𝙴 𝐈𝙽 𝐆𝚁𝙾𝚄𝙿𝚂 𝐀𝙽𝙳 𝐔𝚂𝙴 /skip 𝐂𝙾𝙼𝙼𝙰𝙽𝙳.**\n**◈ 𝐓𝙷𝙰𝙽𝙺 𝐔𝙷 𝐁𝙰𝙱𝚈.**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "•─╼⃝𖠁𝐎𝐔𝐑 𝐆𝐑𝐎𝐔𝐏 𖠁⃝╾─•", url=f"https://t.me/+WDNH4yTCWe5jOTI1")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command(ACTIVEVIDEO_COMMAND)
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/fbb992b2477e3ecd09fc0.jpg",
        caption=f"""**◈ 𝐓𝙷𝙸𝚂 𝐂𝙾𝙼𝙼𝙰𝙽𝙳 𝐈𝚂 𝐎𝙽𝙻𝚈 𝐅𝙾𝚁 𝐒𝚄𝙳𝙾 𝐔𝚂𝙴𝚁𝚂 𝐁𝙰𝙱𝚈..**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "•─╼⃝𖠁𝐎𝐔𝐑 𝐆𝐑𝐎𝐔𝐏 𖠁⃝╾─•", url=f"https://t.me/+WDNH4yTCWe5jOTI1")
                ]
            ]
        ),
    )



@app.on_message(
    filters.command(ACTIVEVC_COMMAND)
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/fbb992b2477e3ecd09fc0.jpg",
        caption=f"""**◈ 𝐓𝙷𝙸𝚂 𝐂𝙾𝙼𝙼𝙰𝙽𝙳 𝐈𝚂 𝐎𝙽𝙻𝚈 𝐅𝙾𝚁 𝐒𝚄𝙳𝙾 𝐔𝚂𝙴𝚁𝚂 𝐁𝙰𝙱𝚈..**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "•─╼⃝𖠁𝐎𝐔𝐑 𝐆𝐑𝐎𝐔𝐏 𖠁⃝╾─•", url=f"https://t.me/+WDNH4yTCWe5jOTI1")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command(ACTIVEVC_COMMAND)
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/fbb992b2477e3ecd09fc0.jpg",
        caption=f"""**◈ 𝐓𝙷𝙸𝚂 𝐂𝙾𝙼𝙼𝙰𝙽𝙳 𝐈𝚂 𝐎𝙽𝙻𝚈 𝐅𝙾𝚁 𝐒𝚄𝙳𝙾 𝐔𝚂𝙴𝚁𝚂 𝐁𝙰𝙱𝚈..**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "•─╼⃝𖠁𝐎𝐔𝐑 𝐆𝐑𝐎𝐔𝐏 𖠁⃝╾─•", url=f"https://t.me/+WDNH4yTCWe5jOTI1")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command(ACTIVEVIDEO_COMMAND)
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/fbb992b2477e3ecd09fc0.jpg",
        caption=f"""**◈ 𝐓𝙷𝙸𝚂 𝐂𝙾𝙼𝙼𝙰𝙽𝙳 𝐈𝚂 𝐎𝙽𝙻𝚈 𝐅𝙾𝚁 𝐒𝚄𝙳𝙾 𝐔𝚂𝙴𝚁𝚂 𝐁𝙰𝙱𝚈..**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "•─╼⃝𖠁𝐎𝐔𝐑 𝐆𝐑𝐎𝐔𝐏 𖠁⃝╾─•", url=f"https://t.me/+WDNH4yTCWe5jOTI1")
                ]
            ]
        ),
    )
    
@app.on_message(
    filters.command(RESTART_COMMAND)
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/fbb992b2477e3ecd09fc0.jpg",
        caption=f"""**◈ 𝐓𝙷𝙸𝚂 𝐂𝙾𝙼𝙼𝙰𝙽𝙳 𝐈𝚂 𝐎𝙽𝙻𝚈 𝐅𝙾𝚁 𝐒𝚄𝙳𝙾 𝐔𝚂𝙴𝚁𝚂 𝐁𝙰𝙱𝚈..**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "•─╼⃝𖠁𝐎𝐔𝐑 𝐆𝐑𝐎𝐔𝐏 𖠁⃝╾─•", url=f"https://t.me/+WDNH4yTCWe5jOTI1")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command(RESTART_COMMAND)
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/fbb992b2477e3ecd09fc0.jpg",
        caption=f"""**◈ 𝐓𝙷𝙸𝚂 𝐂𝙾𝙼𝙼𝙰𝙽𝙳 𝐈𝚂 𝐎𝙽𝙻𝚈 𝐅𝙾𝚁 𝐒𝚄𝙳𝙾 𝐔𝚂𝙴𝚁𝚂 𝐁𝙰𝙱𝚈..**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "•─╼⃝𖠁𝐎𝐔𝐑 𝐆𝐑𝐎𝐔𝐏 𖠁⃝╾─•", url=f"https://t.me/+WDNH4yTCWe5jOTI1")
                ]
            ]
        ),
    )
    
@app.on_message(
    filters.command(GETVAR_COMMAND)
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/fbb992b2477e3ecd09fc0.jpg",
        caption=f"""**◈ 𝐓𝙷𝙸𝚂 𝐂𝙾𝙼𝙼𝙰𝙽𝙳 𝐈𝚂 𝐎𝙽𝙻𝚈 𝐅𝙾𝚁 𝐒𝚄𝙳𝙾 𝐔𝚂𝙴𝚁𝚂 𝐁𝙰𝙱𝚈..**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "•─╼⃝𖠁𝐎𝐔𝐑 𝐆𝐑𝐎𝐔𝐏 𖠁⃝╾─•", url=f"https://t.me/+WDNH4yTCWe5jOTI1")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command(GETVAR_COMMAND)
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/fbb992b2477e3ecd09fc0.jpg",
        caption=f"""**◈ 𝐓𝙷𝙸𝚂 𝐂𝙾𝙼𝙼𝙰𝙽𝙳 𝐈𝚂 𝐎𝙽𝙻𝚈 𝐅𝙾𝚁 𝐒𝚄𝙳𝙾 𝐔𝚂𝙴𝚁𝚂 𝐁𝙰𝙱𝚈..**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "•─╼⃝𖠁𝐎𝐔𝐑 𝐆𝐑𝐎𝐔𝐏 𖠁⃝╾─•", url=f"https://t.me/+WDNH4yTCWe5jOTI1")
                ]
            ]
        ),
    )
    
@app.on_message(
    filters.command(SEEK_COMMAND)
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/fbb992b2477e3ecd09fc0.jpg",
        caption=f"""**◈ 𝐓𝙷𝙸𝚂 𝐂𝙾𝙼𝙼𝙰𝙽𝙳 𝐔𝚂𝙴 𝐈𝙽 𝐎𝙽𝙻𝚈 𝐆𝚁𝙾𝚄𝙿𝚂 𝐁𝙰𝙱𝚈 **\n**◈ 𝐆𝙾 𝐓𝙾 𝐆𝚁𝙾𝚄𝙿𝚂/𝐀𝙳𝙳 𝐌𝙴 𝐈𝙽 𝐆𝚁𝙾𝚄𝙿𝚂 𝐀𝙽𝙳 𝐔𝚂𝙴 /seek (count) 𝐂𝙾𝙼𝙼𝙰𝙽𝙳.**\n**◈ 𝐓𝙷𝙰𝙽𝙺 𝐔𝙷 𝐁𝙰𝙱𝚈.**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "•─╼⃝𖠁𝐎𝐔𝐑 𝐆𝐑𝐎𝐔𝐏 𖠁⃝╾─•", url=f"https://t.me/+WDNH4yTCWe5jOTI1")
                ]
            ]
        ),
    )


@app.on_message(
    filters.command(RESUME_COMMAND)
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/fbb992b2477e3ecd09fc0.jpg",
        caption=f"""**◈ 𝐓𝙷𝙸𝚂 𝐂𝙾𝙼𝙼𝙰𝙽𝙳 𝐔𝚂𝙴 𝐈𝙽 𝐎𝙽𝙻𝚈 𝐆𝚁𝙾𝚄𝙿𝚂 𝐁𝙰𝙱𝚈 **\n**◈ 𝐆𝙾 𝐓𝙾 𝐆𝚁𝙾𝚄𝙿𝚂/𝐀𝙳𝙳 𝐌𝙴 𝐈𝙽 𝐆𝚁𝙾𝚄𝙿𝚂 𝐀𝙽𝙳 𝐔𝚂𝙴 /resume 𝐂𝙾𝙼𝙼𝙰𝙽𝙳.**\n**◈ 𝐓𝙷𝙰𝙽𝙺 𝐔𝙷 𝐁𝙰𝙱𝚈.**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "•─╼⃝𖠁𝐎𝐔𝐑 𝐆𝐑𝐎𝐔𝐏 𖠁⃝╾─•", url=f"https://t.me/+WDNH4yTCWe5jOTI1")
                ]
            ]
        ),
    )


@app.on_message(
    filters.command(SETTINGS_COMMAND)
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/fbb992b2477e3ecd09fc0.jpg",
        caption=f"""**◈ 𝐓𝙷𝙸𝚂 𝐂𝙾𝙼𝙼𝙰𝙽𝙳 𝐔𝚂𝙴 𝐈𝙽 𝐎𝙽𝙻𝚈 𝐆𝚁𝙾𝚄𝙿𝚂 𝐁𝙰𝙱𝚈 **\n**◈ 𝐆𝙾 𝐓𝙾 𝐆𝚁𝙾𝚄𝙿𝚂/𝐀𝙳𝙳 𝐌𝙴 𝐈𝙽 𝐆𝚁𝙾𝚄𝙿𝚂 𝐀𝙽𝙳 𝐔𝚂𝙴 /settings 𝐂𝙾𝙼𝙼𝙰𝙽𝙳.**\n**◈ 𝐓𝙷𝙰𝙽𝙺 𝐔𝙷 𝐁𝙰𝙱𝚈.**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "•─╼⃝𖠁𝐎𝐔𝐑 𝐆𝐑𝐎𝐔𝐏 𖠁⃝╾─•", url=f"https://t.me/+WDNH4yTCWe5jOTI1")
                ]
            ]
        ),
    )


@app.on_message(
    filters.command(GBAN_COMMAND)
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/fbb992b2477e3ecd09fc0.jpg",
        caption=f"""**◈ 𝐓𝙷𝙸𝚂 𝐂𝙾𝙼𝙼𝙰𝙽𝙳 𝐈𝚂 𝐎𝙽𝙻𝚈 𝐅𝙾𝚁 𝐒𝚄𝙳𝙾 𝐔𝚂𝙴𝚁𝚂 𝐁𝙰𝙱𝚈..**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "•─╼⃝𖠁𝐎𝐔𝐑 𝐆𝐑𝐎𝐔𝐏 𖠁⃝╾─•", url=f"https://t.me/+WDNH4yTCWe5jOTI1")
                ]
            ]
        ),
    )
    
@app.on_message(
    filters.command(GBAN_COMMAND)
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/fbb992b2477e3ecd09fc0.jpg",
        caption=f"""**◈ 𝐓𝙷𝙸𝚂 𝐂𝙾𝙼𝙼𝙰𝙽𝙳 𝐈𝚂 𝐎𝙽𝙻𝚈 𝐅𝙾𝚁 𝐒𝚄𝙳𝙾 𝐔𝚂𝙴𝚁𝚂 𝐁𝙰𝙱𝚈..**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "•─╼⃝𖠁𝐎𝐔𝐑 𝐆𝐑𝐎𝐔𝐏 𖠁⃝╾─•", url=f"https://t.me/+WDNH4yTCWe5jOTI1")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command(UNGBAN_COMMAND)
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/fbb992b2477e3ecd09fc0.jpg",
        caption=f"""**◈ 𝐓𝙷𝙸𝚂 𝐂𝙾𝙼𝙼𝙰𝙽𝙳 𝐈𝚂 𝐎𝙽𝙻𝚈 𝐅𝙾𝚁 𝐒𝚄𝙳𝙾 𝐔𝚂𝙴𝚁𝚂 𝐁𝙰𝙱𝚈..**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "•─╼⃝𖠁𝐎𝐔𝐑 𝐆𝐑𝐎𝐔𝐏 𖠁⃝╾─•", url=f"https://t.me/+WDNH4yTCWe5jOTI1")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command(UNGBAN_COMMAND)
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/fbb992b2477e3ecd09fc0.jpg",
        caption=f"""**◈ 𝐓𝙷𝙸𝚂 𝐂𝙾𝙼𝙼𝙰𝙽𝙳 𝐈𝚂 𝐎𝙽𝙻𝚈 𝐅𝙾𝚁 𝐒𝚄𝙳𝙾 𝐔𝚂𝙴𝚁𝚂 𝐁𝙰𝙱𝚈..**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "•─╼⃝𖠁𝐎𝐔𝐑 𝐆𝐑𝐎𝐔𝐏 𖠁⃝╾─•", url=f"https://t.me/+WDNH4yTCWe5jOTI1")
                ]
            ]
        ),
    )


@app.on_message(
    filters.command(RELOAD_COMMAND)
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/fbb992b2477e3ecd09fc0.jpg",
        caption=f"""**◈ 𝐓𝙷𝙸𝚂 𝐂𝙾𝙼𝙼𝙰𝙽𝙳 𝐔𝚂𝙴 𝐈𝙽 𝐎𝙽𝙻𝚈 𝐆𝚁𝙾𝚄𝙿𝚂 𝐁𝙰𝙱𝚈 **\n**◈ 𝐆𝙾 𝐓𝙾 𝐆𝚁𝙾𝚄𝙿𝚂/𝐀𝙳𝙳 𝐌𝙴 𝐈𝙽 𝐆𝚁𝙾𝚄𝙿𝚂 𝐀𝙽𝙳 𝐔𝚂𝙴 /reload 𝐂𝙾𝙼𝙼𝙰𝙽𝙳.**\n**◈ 𝐓𝙷𝙰𝙽𝙺 𝐔𝙷 𝐁𝙰𝙱𝚈.**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "•─╼⃝𖠁𝐎𝐔𝐑 𝐆𝐑𝐎𝐔𝐏 𖠁⃝╾─•", url=f"https://t.me/+WDNH4yTCWe5jOTI1")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command(UPDATE_COMMAND)
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/fbb992b2477e3ecd09fc0.jpg",
        caption=f"""**◈ 𝐓𝙷𝙸𝚂 𝐂𝙾𝙼𝙼𝙰𝙽𝙳 𝐈𝚂 𝐎𝙽𝙻𝚈 𝐅𝙾𝚁 𝐒𝚄𝙳𝙾 𝐔𝚂𝙴𝚁𝚂 𝐁𝙰𝙱𝚈..**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "•─╼⃝𖠁𝐎𝐔𝐑 𝐆𝐑𝐎𝐔𝐏 𖠁⃝╾─•", url=f"https://t.me/+WDNH4yTCWe5jOTI1")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command(UPDATE_COMMAND)
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/fbb992b2477e3ecd09fc0.jpg",
        caption=f"""**◈ 𝐓𝙷𝙸𝚂 𝐂𝙾𝙼𝙼𝙰𝙽𝙳 𝐈𝚂 𝐎𝙽𝙻𝚈 𝐅𝙾𝚁 𝐒𝚄𝙳𝙾 𝐔𝚂𝙴𝚁𝚂 𝐁𝙰𝙱𝚈..**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "•─╼⃝𖠁𝐎𝐔𝐑 𝐆𝐑𝐎𝐔𝐏 𖠁⃝╾─•", url=f"https://t.me/+WDNH4yTCWe5jOTI1")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command(SPEEDTEST_COMMAND)
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/fbb992b2477e3ecd09fc0.jpg",
        caption=f"""**◈ 𝐓𝙷𝙸𝚂 𝐂𝙾𝙼𝙼𝙰𝙽𝙳 𝐈𝚂 𝐎𝙽𝙻𝚈 𝐅𝙾𝚁 𝐒𝚄𝙳𝙾 𝐔𝚂𝙴𝚁𝚂 𝐁𝙰𝙱𝚈..**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "•─╼⃝𖠁𝐎𝐔𝐑 𝐆𝐑𝐎𝐔𝐏 𖠁⃝╾─•", url=f"https://t.me/+WDNH4yTCWe5jOTI1")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command(SPEEDTEST_COMMAND)
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/fbb992b2477e3ecd09fc0.jpg",
        caption=f"""**◈ 𝐓𝙷𝙸𝚂 𝐂𝙾𝙼𝙼𝙰𝙽𝙳 𝐈𝚂 𝐎𝙽𝙻𝚈 𝐅𝙾𝚁 𝐒𝚄𝙳𝙾 𝐔𝚂𝙴𝚁𝚂 𝐁𝙰𝙱𝚈..**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "•─╼⃝𖠁𝐎𝐔𝐑 𝐆𝐑𝐎𝐔𝐏 𖠁⃝╾─•", url=f"https://t.me/+WDNH4yTCWe5jOTI1")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command(ADDSUDO_COMMAND)
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/fbb992b2477e3ecd09fc0.jpg",
        caption=f"""**◈ 𝐓𝙷𝙸𝚂 𝐂𝙾𝙼𝙼𝙰𝙽𝙳 𝐈𝚂 𝐎𝙽𝙻𝚈 𝐌𝚈 𝐎𝚆𝙽𝙴𝚁 𝐔𝚂𝙴𝚁𝚂 𝐁𝙰𝙱𝚈..**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "•─╼⃝𖠁𝐎𝐔𝐑 𝐆𝐑𝐎𝐔𝐏 𖠁⃝╾─•", url=f"https://t.me/+WDNH4yTCWe5jOTI1")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command(ADDSUDO_COMMAND)
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/fbb992b2477e3ecd09fc0.jpg",
        caption=f"""**◈ 𝐓𝙷𝙸𝚂 𝐂𝙾𝙼𝙼𝙰𝙽𝙳 𝐈𝚂 𝐎𝙽𝙻𝚈 𝐅𝙾𝚁 𝐌𝚈 𝐎𝚆𝙽𝙴𝚁 𝐁𝙰𝙱𝚈..**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "•─╼⃝𖠁𝐎𝐔𝐑 𝐆𝐑𝐎𝐔𝐏 𖠁⃝╾─•", url=f"https://t.me/+WDNH4yTCWe5jOTI1")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command(DELSUDO_COMMAND)
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/fbb992b2477e3ecd09fc0.jpg",
        caption=f"""**◈ 𝐓𝙷𝙸𝚂 𝐂𝙾𝙼𝙼𝙰𝙽𝙳 𝐈𝚂 𝐎𝙽𝙻𝚈 𝐅𝙾𝚁 𝐌𝚈 𝐎𝚆𝙽𝙴𝚁 𝐁𝙰𝙱𝚈..**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "•─╼⃝𖠁𝐎𝐔𝐑 𝐆𝐑𝐎𝐔𝐏 𖠁⃝╾─•", url=f"https://t.me/+WDNH4yTCWe5jOTI1")
                ]
            ]
        ),
    )


@app.on_message(
    filters.command(DELSUDO_COMMAND)
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/fbb992b2477e3ecd09fc0.jpg",
        caption=f"""**◈ 𝐓𝙷𝙸𝚂 𝐂𝙾𝙼𝙼𝙰𝙽𝙳 𝐈𝚂 𝐎𝙽𝙻𝚈 𝐅𝙾𝚁 𝐌𝚈 𝐎𝚆𝙽𝙴𝚁 𝐁𝙰𝙱𝚈..**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "•─╼⃝𖠁𝐎𝐔𝐑 𝐆𝐑𝐎𝐔𝐏 𖠁⃝╾─•", url=f"https://t.me/+WDNH4yTCWe5jOTI1")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command(BROADCAST_COMMAND)
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/fbb992b2477e3ecd09fc0.jpg",
        caption=f"""**◈ 𝐓𝙷𝙸𝚂 𝐂𝙾𝙼𝙼𝙰𝙽𝙳 𝐈𝚂 𝐎𝙽𝙻𝚈 𝐅𝙾𝚁 𝐒𝚄𝙳𝙾 𝐔𝚂𝙴𝚁𝚂 𝐁𝙰𝙱𝚈..**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "•─╼⃝𖠁𝐎𝐔𝐑 𝐆𝐑𝐎𝐔𝐏 𖠁⃝╾─•", url=f"https://t.me/+WDNH4yTCWe5jOTI1")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command(BROADCAST_COMMAND)
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/fbb992b2477e3ecd09fc0.jpg",
        caption=f"""**◈ 𝐓𝙷𝙸𝚂 𝐂𝙾𝙼𝙼𝙰𝙽𝙳 𝐈𝚂 𝐎𝙽𝙻𝚈 𝐅𝙾𝚁 𝐒𝚄𝙳𝙾 𝐔𝚂𝙴𝚁𝚂 𝐁𝙰𝙱𝚈..**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "•─╼⃝𖠁𝐎𝐔𝐑 𝐆𝐑𝐎𝐔𝐏 𖠁⃝╾─•", url=f"https://t.me/+WDNH4yTCWe5jOTI1")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command(AUTH_COMMAND)
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/fbb992b2477e3ecd09fc0.jpg",
        caption=f"""**◈ 𝐓𝙷𝙸𝚂 𝐂𝙾𝙼𝙼𝙰𝙽𝙳 𝐔𝚂𝙴 𝐈𝙽 𝐎𝙽𝙻𝚈 𝐆𝚁𝙾𝚄𝙿𝚂 𝐁𝙰𝙱𝚈 **\n**◈ 𝐆𝙾 𝐓𝙾 𝐆𝚁𝙾𝚄𝙿𝚂/𝐀𝙳𝙳 𝐌𝙴 𝐈𝙽 𝐆𝚁𝙾𝚄𝙿𝚂 𝐀𝙽𝙳 𝐔𝚂𝙴 /auth 𝐂𝙾𝙼𝙼𝙰𝙽𝙳.**\n**◈ 𝐓𝙷𝙰𝙽𝙺 𝐔𝙷 𝐁𝙰𝙱𝚈.**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "•─╼⃝𖠁𝐎𝐔𝐑 𝐆𝐑𝐎𝐔𝐏 𖠁⃝╾─•", url=f"https://t.me/+WDNH4yTCWe5jOTI1")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command(UNAUTH_COMMAND)
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/fbb992b2477e3ecd09fc0.jpg",
        caption=f"""**◈ 𝐓𝙷𝙸𝚂 𝐂𝙾𝙼𝙼𝙰𝙽𝙳 𝐔𝚂𝙴 𝐈𝙽 𝐎𝙽𝙻𝚈 𝐆𝚁𝙾𝚄𝙿𝚂 𝐁𝙰𝙱𝚈 **\n**◈ 𝐆𝙾 𝐓𝙾 𝐆𝚁𝙾𝚄𝙿𝚂/𝐀𝙳𝙳 𝐌𝙴 𝐈𝙽 𝐆𝚁𝙾𝚄𝙿𝚂 𝐀𝙽𝙳 𝐔𝚂𝙴 /unauth 𝐂𝙾𝙼𝙼𝙰𝙽𝙳.**\n**◈ 𝐓𝙷𝙰𝙽𝙺 𝐔𝙷 𝐁𝙰𝙱𝚈.**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "•─╼⃝𖠁𝐎𝐔𝐑 𝐆𝐑𝐎𝐔𝐏 𖠁⃝╾─•", url=f"https://t.me/+WDNH4yTCWe5jOTI1")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command(BLACKLISTCHAT_COMMAND)
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/fbb992b2477e3ecd09fc0.jpg",
        caption=f"""**◈ 𝐓𝙷𝙸𝚂 𝐂𝙾𝙼𝙼𝙰𝙽𝙳 𝐈𝚂 𝐎𝙽𝙻𝚈 𝐅𝙾𝚁 𝐒𝚄𝙳𝙾 𝐔𝚂𝙴𝚁𝚂 𝐁𝙰𝙱𝚈..**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "•─╼⃝𖠁𝐎𝐔𝐑 𝐆𝐑𝐎𝐔𝐏 𖠁⃝╾─•", url=f"https://t.me/+WDNH4yTCWe5jOTI1")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command(BLACKLISTCHAT_COMMAND)
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/fbb992b2477e3ecd09fc0.jpg",
        caption=f"""**◈ 𝐓𝙷𝙸𝚂 𝐂𝙾𝙼𝙼𝙰𝙽𝙳 𝐈𝚂 𝐎𝙽𝙻𝚈 𝐅𝙾𝚁 𝐒𝚄𝙳𝙾 𝐔𝚂𝙴𝚁𝚂 𝐁𝙰𝙱𝚈..**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "•─╼⃝𖠁𝐎𝐔𝐑 𝐆𝐑𝐎𝐔𝐏 𖠁⃝╾─•", url=f"https://t.me/+WDNH4yTCWe5jOTI1")
                ]
            ]
        ),
    )
@app.on_message(
    filters.command(BLOCK_COMMAND)
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/fbb992b2477e3ecd09fc0.jpg",
        caption=f"""**◈ 𝐓𝙷𝙸𝚂 𝐂𝙾𝙼𝙼𝙰𝙽𝙳 𝐈𝚂 𝐎𝙽𝙻𝚈 𝐅𝙾𝚁 𝐒𝚄𝙳𝙾 𝐔𝚂𝙴𝚁𝚂 𝐁𝙰𝙱𝚈..**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "•─╼⃝𖠁𝐎𝐔𝐑 𝐆𝐑𝐎𝐔𝐏 𖠁⃝╾─•", url=f"https://t.me/+WDNH4yTCWe5jOTI1")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command(BLOCK_COMMAND)
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/fbb992b2477e3ecd09fc0.jpg",
        caption=f"""**◈ 𝐓𝙷𝙸𝚂 𝐂𝙾𝙼𝙼𝙰𝙽𝙳 𝐈𝚂 𝐎𝙽𝙻𝚈 𝐅𝙾𝚁 𝐒𝚄𝙳𝙾 𝐔𝚂𝙴𝚁𝚂 𝐁𝙰𝙱𝚈..**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "•─╼⃝𖠁𝐎𝐔𝐑 𝐆𝐑𝐎𝐔𝐏 𖠁⃝╾─•", url=f"https://t.me/+WDNH4yTCWe5jOTI1")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command(UNBLOCK_COMMAND)
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/fbb992b2477e3ecd09fc0.jpg",
        caption=f"""**◈ 𝐓𝙷𝙸𝚂 𝐂𝙾𝙼𝙼𝙰𝙽𝙳 𝐈𝚂 𝐎𝙽𝙻𝚈 𝐅𝙾𝚁 𝐒𝚄𝙳𝙾 𝐔𝚂𝙴𝚁𝚂 𝐁𝙰𝙱𝚈..**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "•─╼⃝𖠁𝐎𝐔𝐑 𝐆𝐑𝐎𝐔𝐏 𖠁⃝╾─•", url=f"https://t.me/+WDNH4yTCWe5jOTI1")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command(UNBLOCK_COMMAND)
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/fbb992b2477e3ecd09fc0.jpg",
        caption=f"""**◈ 𝐓𝙷𝙸𝚂 𝐂𝙾𝙼𝙼𝙰𝙽𝙳 𝐈𝚂 𝐎𝙽𝙻𝚈 𝐅𝙾𝚁 𝐒𝚄𝙳𝙾 𝐔𝚂𝙴𝚁𝚂 𝐁𝙰𝙱𝚈..**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "•─╼⃝𖠁𝐎𝐔𝐑 𝐆𝐑𝐎𝐔𝐏 𖠁⃝╾─•", url=f"https://t.me/+WDNH4yTCWe5jOTI1")
                ]
            ]
        ),
    )

