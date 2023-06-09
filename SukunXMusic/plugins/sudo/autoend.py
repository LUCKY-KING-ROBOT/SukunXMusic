#
# Copyright (C) 2021-2022 by TeamSukun@Github, < https://github.com/TeamSukun >.
#
# This file is part of < https://github.com/TeamSukun/SukunXMusic > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamSukun/SukunXMusic/blob/master/LICENSE >
#
# All rights reserved.

from pyrogram import filters

import config
from strings import get_command
from SukunXMusic import app
from SukunXMusic.misc import SUDOERS
from SukunXMusic.utils.database import autoend_off, autoend_on
from SukunXMusic.utils.decorators.language import language

# Commands
AUTOEND_COMMAND = get_command("AUTOEND_COMMAND")


@app.on_message(filters.command(AUTOEND_COMMAND) & SUDOERS)
async def auto_end_stream(client, message):
    usage = "**ᴜsᴀɢᴇ:**\n\n/autoend [enable|disable]"
    if len(message.command) != 2:
        return await message.reply_text(usage)
    state = message.text.split(None, 1)[1].strip()
    state = state.lower()
    if state == "enable":
        await autoend_on()
        await message.reply_text(
            "ᴀᴜᴛᴏ ᴇɴᴅ sᴛʀᴇᴀᴍ ᴇɴᴀʙʟᴇᴅ.\n\nᴀɢᴀʟ ᴋᴏɪ sᴏɴɢ ɴᴏɪ sᴜɴ ʟᴀʜᴀ ʜᴏɢᴀ ᴠᴄ ᴘᴇ ᴛᴏʜ ᴍᴀɪɴ ᴠᴄ sᴇ ᴄʜᴀʟɪ ᴊᴀᴜɴɢɪ.."
        )
    elif state == "disable":
        await autoend_off()
        await message.reply_text("ᴀᴜᴛᴏ ᴇɴᴅ sᴛʀᴇᴀᴍ ᴅɪsᴀʙʟᴇᴅ.")
    else:
        await message.reply_text(usage)
