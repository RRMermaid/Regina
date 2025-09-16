from aiogram import Bot, Dispatcher
from config import BOT_TOKEN, CHAT_ID
from aiogram import types
from telegram_bot import dp

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

async def grant_access(user_id: int):
invite = await bot.create_chat_invite_link(CHAT_ID, member_limit=1)
return invite.invite_link

async def revoke_access(user_id: int):
await bot.kick_chat_member(CHAT_ID, user_id)

@dp.message_handler()
async def get_chat_id(message: types.Message):
    await message.reply(f"Chat ID: {message.chat.id}")
    print(f"Chat ID: {message.chat.id}")
    