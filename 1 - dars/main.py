import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message
import random

TOKEN = ""

dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Salom bot ishlayabdi!\n 1 dan 10 gacha son kiriting misol uchun -> 5 !")

    @dp.message(F.text.isdigit())
    async def echo(message: Message):
        number = random.randint(1, 10)
        text = message.text
        if number == int(text):
            await message.answer(f"{number} == {text}")
        else:
            await message.answer(f"{number} != {text}")

    @dp.message()
    async def echo2(message: Message):
        await message.answer(f"siz text kiridingiz -> {message.text}! Son kiriting miziol uchun -> 8")


async def main() -> None:
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
