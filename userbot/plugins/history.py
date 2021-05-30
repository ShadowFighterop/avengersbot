from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from personalBot import bot, CmdHelp
from personalBot.utils import admin_cmd, edit_or_reply as eor, sudo_cmd

@personalBot.on(admin_cmd(pattern="history ?(.*)"))
@personalBot.on(sudo_cmd(pattern="history ?(.*)", allow_sudo=True))
async def _(personalevent):
    if personalevent.fwd_from:
        return 
    if not personalevent.reply_to_msg_id:
       await eor(personalevent, "`Please Reply To A User To Get This Module Work`")
       return
    reply_message = await personalevent.get_reply_message() 
    chat = "Sangmatainfo_bot"
    victim = reply_message.sender.id
    if reply_message.sender.bot:
       await eor(personalevent, "Need actual users. Not Bots")
       return
    await eor(personalevent, "Checking...")
    async with personalevent.client.conversation(chat) as conv:
          try:     
              response1 = conv.wait_event(events.NewMessage(incoming=True,from_users=461843263))
              response2 = conv.wait_event(events.NewMessage(incoming=True,from_users=461843263))
              response3 = conv.wait_event(events.NewMessage(incoming=True,from_users=461843263))
              await conv.send_message("/search_id {}".format(victim))
              response1 = await response1 
              response2 = await response2 
              response3 = await response3 
          except YouBlockedUserError: 
              await personalevent.reply("Please unblock ( @Sangmatainfo_bot ) ")
              return
          if response1.text.startswith("No records found"):
             await eor(personalevent, "User never changed his Username...")
          else: 
             await personalevent.delete()
             await personalevent.client.send_message(personalevent.chat_id, response2.message)

@personalBot.on(admin_cmd(pattern="unh ?(.*)"))
@personalBot.on(sudo_cmd(pattern="unh ?(.*)", allow_sudo=True))
async def _(personalevent):
    if personalevent.fwd_from:
        return 
    if not personalevent.reply_to_msg_id:
       await eor(personalevent, "`Please Reply To A User To Get This Module Work`")
       return
    reply_message = await personalevent.get_reply_message() 
    chat = "Sangmatainfo_bot"
    victim = reply_message.sender.id
    if reply_message.sender.bot:
       await eor(personalevent, "Need actual users. Not Bots")
       return
    await eor(personalevent, "Checking...")
    async with personalevent.client.conversation(chat) as conv:
          try:     
              response1 = conv.wait_event(events.NewMessage(incoming=True,from_users=461843263))
              response2 = conv.wait_event(events.NewMessage(incoming=True,from_users=461843263))
              response3 = conv.wait_event(events.NewMessage(incoming=True,from_users=461843263))
              await conv.send_message("/search_id {}".format(victim))
              response1 = await response1 
              response2 = await response2 
              response3 = await response3 
          except YouBlockedUserError: 
              await personalevent.reply("Please unblock ( @Sangmatainfo_bot ) ")
              return
          if response1.text.startswith("No records found"):
             await eor(personalevent, "User never changed his Username...")
          else: 
             await personalevent.delete()
             await personalevent.client.send_message(personalevent.chat_id, response3.message)

CmdHelp("history").add_command(
  "history", "<reply to a user>", "Fetches the name history of replied user."
).add_command(
  "unh", "<reply to user>", "Fetches the Username History of replied users."
).add()
