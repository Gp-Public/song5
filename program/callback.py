# Copyright (C) 2021 By VeezMusicProject

from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""โจ **Welcome [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**\n
๐ญ **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) allows you to play music and video on groups through the new Telegram's video chats!**

๐ก **Find out all the Bot's commands and how they work by clicking on the ยป ๐ Commands button!**


๐  [๐ซ๐ฃ๐ฟ๐ฎ๊ช๐ถ๐ป๐ซ](https://t.me/Gplove_Rp)**if you have any problem contact**

โ **To know how to use this bot, please click on the ยป ๐ค Basic Guide button!**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "โ ๐ผ๐ฟ๐ฟ ๐๐ ๐๐ ๐๐๐๐ ๐๐๐๐๐ โ",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("๐ค Basic Guide", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton("๐ Commands", callback_data="cbcmds"),
                    InlineKeyboardButton("๐ owner", url=f"https://t.me/{OWNER_NAME}"),
                ],
                [
                    InlineKeyboardButton(
                        "๐ฅ Official Group", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "๐ข Official Channel", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "๐ง๐  ๐๐๐ผ๐ฟ๐ฒ๐ ๐๐๐๐๐พ", url="https://t.me/Shadows_Musicbot"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""โ **Basic Guide for using this bot:**

1.) **first, add me to your group.**
2.) **then promote me as admin and give all permissions except anonymous admin.**
3.) **add @{ASSISTANT_NAME} to your group or type /userbotjoin to invite her.**
4.) **turn on the video chat first before start to play video.**
5.) **all the command list you can see on ยป ๐ Commands button, find it on start home, tap the ยป Go Back button below.**

๐ก **If you have a follow-up questions about this bot, you can tell it on my support chat here: @{GROUP_SUPPORT}**

โก __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("๐ Go Back", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbhelps(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""๐ Here is the Commands list:

ยป /play - play music on voice chat
ยป /stream - enter the radio link
ยป /vplay - play video on video chat
ยป /vstream - for m3u8/live link
ยป /playlist - show you the playlist
ยป /video (query) - download video from youtube
ยป /song (query) - download song from youtube
ยป /lyric (query) - scrap the song lyric
ยป /search (query) - search a youtube video link
ยป /queue - show you the queue list (admin only)
ยป /pause - pause the stream (admin only)
ยป /resume - resume the stream (admin only)
ยป /skip - switch to next stream (admin only)
ยป /stop - stop the streaming (admin only)
ยป /userbotjoin - invite the userbot to join chat (admin only)
ยป /userbotleave - order userbot to leave from group (admin only)
ยป /reload - update the admin list (admin only)
ยป /rmw - clean raw files (sudo only)
ยป /rmd - clean downloaded files (sudo only)
ยป /leaveall - order userbot leave from all group (sudo only)

โก __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("๐ Go Back", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    await query.message.delete()
