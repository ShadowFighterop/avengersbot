# by uniborg...Thanks @spechide
# Now will be used in personallBot


import asyncio
import datetime
from datetime import datetime

from telethon import events
from telethon.tl import functions, types
from userbot import CMD_HELP
from userbot import ALIVE_NAME, personalversion
from personalBot.utils import admin_cmd, edit_or_reply
from userbot.cmdhelp import CmdHelp

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "personal User"

personal = bot.uid


global USER_offline  # pylint:disable=E0602
global offline_time  # pylint:disable=E0602
global last_offline_message  # pylint:disable=E0602
global offline_start
global offline_end
USER_offline = {}
offline_time = None
last_offline_message = {}
offline_start = {}


@borg.on(events.NewMessage(outgoing=True))  # pylint:disable=E0602
async def set_not_offline(event):
    if event.fwd_from:
        return
    global USER_offline  # pylint:disable=E0602
    global offline_time  # pylint:disable=E0602
    global last_offline_message  # pylint:disable=E0602
    global offline_start
    global offline_end
    came_back = datetime.now()
    offline_end = came_back.replace(microsecond=0)
    if offline_start != {}:
        total_offline_time = str((offline_end - offline_start))
    current_message = event.message.message
    if ".offline" not in current_message and "yes" in USER_offline:  # pylint:disable=E0602
        personalBot = await borg.send_message(
            event.chat_id,
            "🔥__Back Online!__\n**No Longer offline.**\n⏱️ `Was offline for:``"
            + total_offline_time
            + "`", file=personalpic
        )
        try:
            await borg.send_message(  # pylint:disable=E0602
                Config.PRIVATE_GROUP_BOT_API_ID,  # pylint:disable=E0602
                "#offlineFALSE \nSet offline mode to False\n"
                + "🔥__Back online!__\n**No Longer offline.**\n⏱️ `Was offline for:``"
                + total_offline_time
            )
        except Exception as e:  # pylint:disable=C0103,W0703
            await borg.send_message(  # pylint:disable=E0602
                event.chat_id,
                "Please set `PRIVATE_GROUP_BOT_API_ID` "
                + "for the proper functioning of offline functionality "
                + "Ask in @personalSupport to get help setting this value\n\n `{}`".format(str(e)),
                reply_to=event.message.id,
                silent=True,
            )
        await asyncio.sleep(5)
        await personalBot.delete()
        USER_offline = {}  # pylint:disable=E0602
        offline_time = None  # pylint:disable=E0602


@borg.on(
    events.NewMessage(  # pylint:disable=E0602
        incoming=True, func=lambda e: bool(e.mentioned or e.is_private)
    )
)
async def on_offline(event):
    if event.fwd_from:
        return
    global USER_offline  # pylint:disable=E0602
    global offline_time  # pylint:disable=E0602
    global last_offline_message  # pylint:disable=E0602
    global offline_start
    global offline_end
    cum_back = datetime.now()
    offline_end = cum_back.replace(microsecond=0)
    if offline_start != {}:
        total_offline_time = str((offline_end - offline_start))
    current_message_text = event.message.message.lower()
    if "offline" in current_message_text:
        # userbot's should not reply to other userbot's
        # https://core.telegram.org/bots/faq#why-doesn-39t-my-bot-see-messages-from-other-bots
        return False
    if USER_offline and not (await event.get_sender()).bot:
        msg = None
        
        message_to_reply = (
            f"Hey!! My master [{DEFAULTUSER}](tg://user?id={personal}) is currently offline... Since when?\n**For** `{total_offline_time}`\n"
            + f"\n\n👇__Bcoz Of__👇 :-\n`{reason}`"
  if reason
            else f"**Heyy!**\n__I am currently offline.__\n__Since when, you ask? From__ `{total_offline_time}`\nI'll be back when I feel to come🚶"
        )
        msg = await event.reply(message_to_reply, file=personalpic)
        await asyncio.sleep(2)
        if event.chat_id in last_offline_message:  # pylint:disable=E0602
            await last_offline_message[event.chat_id].delete()  # pylint:disable=E0602
        last_offline_message[event.chat_id] = msg  # pylint:disable=E0602


@borg.on(admin_cmd(pattern=r"offline (.*)", outgoing=True))  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    aura = await event.get_reply_message()
    global USER_offline  # pylint:disable=E0602
    global offline_time  # pylint:disable=E0602
    global last_offline_message  # pylint:disable=E0602
    global offline_start
    global offline_end
    global reason
    global personalpic
    USER_offline = {}
    offline_time = None
    last_offline_message = {}
    offline_end = {}
    start_1 = datetime.now()
    offline_start = start_1.replace(microsecond=0)
    reason = event.pattern_match.group(1)
    personalpic = await event.client.download_media(aura)
    if not USER_offline:  # pylint:disable=E0602
        last_seen_status = await borg(  # pylint:disable=E0602
            functions.account.GetPrivacyRequest(types.InputPrivacyKeyStatusTimestamp())
        )
        if isinstance(last_seen_status.rules, types.PrivacyValueAllowAll):
            offline_time = datetime.datetime.now()  # pylint:disable=E0602
        USER_offline = f"yes: {reason} {personalpic}"  # pylint:disable=E0602
        if reason:
            await borg.send_message(
                event.chat_id, f"__**I'm going offline🚶**__ \n⚜️ Bcoz `{reason}`", file=personalpic
            )
        else:
            await borg.send_message(event.chat_id, f"**I am Going offline!**🚶", file=personalpic)
        await asyncio.sleep(0.001)
        await event.delete()
        try:
            await borg.send_message(  # pylint:disable=E0602
                Config.PRIVATE_GROUP_BOT_API_ID,  # pylint:disable=E0602
                f"#offlineTRUE \nSet offline mode to True, and Reason is {reason}",file=personalpic
            )
        except Exception as e:  # pylint:disable=C0103,W0703
            logger.warn(str(e))  # pylint:disable=E0602


CmdHelp("offline").add_command(
  'offline', '<reply to media>/<or type a reson>', 'Marks you offline(Away from Keyboard) with reason(if given) also shows offline time. Media also supported.'
).add()
