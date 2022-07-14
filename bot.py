import asyncio
from os import environ
from pyrogram import Client, filters, idle

API_ID = int(environ.get("API_ID"))
API_HASH = environ.get("API_HASH")
BOT_TOKEN = environ.get("BOT_TOKEN")
SESSION = environ.get("SESSION")
TIME = int(environ.get("TIME"))
GROUPS = []
for grp in environ.get("GROUPS").split():
    GROUPS.append(int(grp))
ADMINS = []
for usr in environ.get("ADMINS").split():
    ADMINS.append(int(usr))

START_MSG = "𝑯𝒆𝒚 {}👋

𝑰 𝒂𝒎 "Mɪᴀ 🦋". 𝑰 𝒄𝒂𝒏 𝒅𝒆𝒍𝒆𝒕𝒆 𝒎𝒆𝒔𝒔𝒂𝒈𝒆 𝒊𝒏 𝒂 𝒈𝒓𝒐𝒖𝒑 𝒂𝒇𝒕𝒆𝒓 𝒔𝒑𝒆𝒄𝒊𝒇𝒊𝒄 𝒕𝒊𝒎𝒆.

𝑬𝒙𝒄𝒍𝒖𝒔𝒊𝒗𝒆𝒍𝒚 𝒎𝒂𝒅𝒆 𝒇𝒐𝒓 𝐌𝐎𝐕𝐈𝐄𝐒𝐇𝐔𝐁"


User = Client(name="user-account",
              session_string=SESSION,
              api_id=API_ID,
              api_hash=API_HASH,
              workers=300
              )


Bot = Client(name="auto-delete",
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN,
             workers=300
             )


@Bot.on_message(filters.command('start') & filters.private)
async def start(bot, message):
    await message.reply(START_MSG.format(message.from_user.mention))

@User.on_message(filters.chat(GROUPS))
async def delete(user, message):
    try:
       if message.from_user.id in ADMINS:
          return
       else:
          await asyncio.sleep(TIME)
          await Bot.delete_messages(message.chat.id, message.id)
    except Exception as e:
       print(e)
       
User.start()
print("User Started!")
Bot.start()
print("Bot Started!")

idle()

User.stop()
print("User Stopped!")
Bot.stop()
print("Bot Stopped!")
