import time
from userbot import *
from personalBot.utils import *
from userbot.cmdhelp import CmdHelp
from telethon import events, version
from telethon.events import NewMessage
from telethon.tl.custom import Dialog
from telethon.tl.types import Channel, Chat, User
from telethon import version
from userbot import ALIVE_NAME, StartTime, personalversion
from personalbot.utils import admin_cmd, edit_or_reply, sudo_cmd


#-------------------------------------------------------------------------------


async def reply_id(event):
    reply_to_id = None
    if event.sender_id in Config.SUDO_USERS:
        reply_to_id = event.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    return reply_to_id

ludosudo = Config.SUDO_USERS
if ludosudo:
    sudou = "True"
else:
    sudou = "False"

DEFAULTUSER = ALIVE_NAME or "Personal User"
Personal_IMG = Config.ALIVE_PIC
CUSTOM_ALIVE_TEXT = Config.ALIVE_MSG or "YOUR PERSONAL BOT !"

USERID = bot.uid

mention = f"[{DEFAULTUSER}](tg://user?id={USERID})"


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


uptime = get_readable_time((time.time() - StartTime))


@bot.on(admin_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    reply_to_id = await reply_id(alive)

    if Personal_IMG:
        Personal_caption = f"**{CUSTOM_ALIVE_TEXT}**\n\n"

        Personal_caption += f"      __**╚»★BOT INFO★«╝**__\n"
        Personal_caption += f"**╭────────☆═━┈┈┈━═☆───────╮**\n"
        Personal_caption += f"**※┄┄➳ BOT OWNER:** {mention}\n"
        Personal_caption += f"**※┄┄➳ BOT STATUS : WORKING NORMALLY **\n"
        Personal_caption += f"**※┄┄➳ YOUR BOT VERSION :**`{personalversion}`\n"
        Personal_caption += f"**※┄┄➳ 𝚂𝙴𝙲𝚄𝚁𝙸𝚃𝚈 𝚂𝚃𝙰𝚃𝚄𝚂 : NO BUGS AND ERRORS **\n"
        Personal_caption += f"**※┄┄➳ TELETHON VERSION :** `{version.__version__}`**\n"
        Personal_caption += f"**※┄┄➳ UPTIME :** `{uptime}\n`"
        Personal_caption += f"**※┄┄➳ SUDO STATUS: `{sudou}`**\n"
        Personal_caption += f"**※┄┄➳ 𝙳𝙴𝚅𝙴𝙻𝙿𝙾𝙴𝚁 𝚂𝚃𝙰𝚃𝚄𝚂 : ACTIVE**\n"
        Personal_caption +=  f"**※┄┄➳ CREATOR : [🇮🇳• ITS A SECRET •🇮🇳](https://t.me/furious_x_y)**\n"
        Personal_caption += f"**╰────────☆═━┈┈┈━═☆───────╯**\n"
        Personal_caption += "[✨REPO✨](https://github.com/FURIOUS-XY/personalbot) 🔹 [📜License📜](https://github.com/FURIOUS-XY/personalbot/blob/master/LICENSE)"

        await alive.client.send_file(
            alive.chat_id, Personal_IMG, caption=Personal_caption, reply_to=reply_to_id
        )
        await alive.delete()
    else:
        await edit_or_reply(
            alive,
            f"**{CUSTOM_ALIVE_TEXT}**\n\n"
            f"     __**╚»★BOT INFO★«╝**__\n"
            f"**╭────────☆═━┈┈┈━═☆───────╮**\n"
            f"**※┄┄➳ BOT STATUS : WORKING NORMALLY **\n"
            f"**※┄┄➳ YOUR BOT VERSION :**`{personalversion}`\n"
            f"**※┄┄➳ 𝚂𝙴𝙲𝚄𝚁𝙸𝚃𝚈 𝚂𝚃𝙰𝚃𝚄𝚂 : NO BUGS AND ERRORS **\n"
            f"**※┄┄➳ TELETHON VERSION :** `{version.__version__}`**\n"
            f"**※┄┄➳ UPTIME :** `{uptime}\n`"
            f"**※┄┄➳ SUDO STATUS: `{sudou}`**\n"
            f"**※┄┄➳ 𝙳𝙴𝚅𝙴𝙻𝙿𝙾𝙴𝚁 𝚂𝚃𝙰𝚃𝚄𝚂 : ACTIVE**\n"
            f"**※┄┄➳ CREATOR : [🇮🇳• ITS A SECRET •🇮🇳](https://t.me/furious_x_y)**\n"
            f"**※┄┄➳ MASTER:** {mention}\n"
            f"**╰────────☆═━┈┈┈━═☆───────╯**\n"
            "[✨REPO✨](https://github.com/FURIOUS-XY/PERSONAL-USERBOT) 🔹 [📜License📜](https://github.com/FURIOUS-XY/PERSONAL-USERBOT/blob/master/LICENSE)",
        )

CmdHelp("alive").add_command(
  'alive', None, 'Check weather the bot is alive or not'
  ).add_info(
  'mar gaya ya jinda hai?'
).add()
