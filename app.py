import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

bot = Bot(token="7074813458:AAF6yAU_eqyqLvYanL1m0HJCiX_nkx6gL6Y")

dp = Dispatcher()



@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer('Это была команда старт')













async def main():
    await dp.start_polling(bot)


asyncio.run(main())