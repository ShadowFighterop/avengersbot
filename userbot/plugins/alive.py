
from userbot import *

from userbot.utils import *

from telethon.events import NewMessage

from telethon.tl.custom import Dialog

from telethon.tl.types import Channel, Chat, User





DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Darkbot User"



ludosudo = Config.SUDO_USERS

if ludosudo:



    sudou = "True"



else:

    sudou = "False"

    

dark = bot.uid



PM_IMG = "https://telegra.ph/file/bd05af18c9b4fc5b57233.mp4"



pm_caption = "__** ✨𝙿𝙴𝚁𝚂𝙾𝙽𝙰𝙻 𝚄𝚂𝙴𝚁𝙱𝙾𝚃 𝙾𝙵 『🔥[{DEFAULTUSER}](tg://user?id={dark})🔥』**__\n\n"




pm_caption += (

    f"           𝙻𝙸𝙽𝚄𝚇 𝚂𝚈𝚂𝚃𝙴𝙼 :- TRUE**\n\n"

)






pm_caption += f 👨‍🔬"**𝙳𝙴𝚅𝙴𝙻𝙿𝙾𝙴𝚁 𝚂𝚃𝙰𝚃𝚄𝚂   : ACTIVE ** \n\n"



pm_caption += f" ** 𝚃𝙴𝙻𝙴𝚃𝙷𝙾𝙽 𝚅𝙴𝚁𝚂𝙸𝙾𝙽  : 1.2.1 ** \n\n"







pm_caption += "**⭐𝚂𝙴𝙲𝚄𝚁𝙸𝚃𝚈 𝚂𝚃𝙰𝚃𝚄𝚂🤖 : NO BUGS AND ERRORS **✅\n\n◆"







pm_caption +=  "**[☠️ᴅᴀʀᴋ ʙᴏᴛ ʀᴇᴘᴏ ☠️ ] : 𝙿𝙴𝚁𝚂𝙾𝙽𝙰𝙻 ** "    





@bot.on(admin_cmd(outgoing=True, pattern="alive$"))

async def amireallyalive(alive):

    await alive.get_chat()

    await alive.delete()

    """ For .alive command, check if the bot is running.  """

    await borg.send_file(alive.chat_id, PM_IMG, caption=pm_caption)

    await alive.delete()





    



    
    
