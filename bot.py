
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command
import asyncio
import os

from binance_api import get_price
from gpt import get_crypto_recommendation

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_handler(message: Message):
    await message.answer("Привет! Введи /recommend BTC или /recommend ETH для получения рекомендации.")

@dp.message(Command("recommend"))
async def recommend_handler(message: Message):
    try:
        parts = message.text.split()
        symbol = parts[1].upper() + "USDT"
        price = get_price(symbol)
        if price:
            reply = get_crypto_recommendation(symbol, price)
            await message.answer(reply)
        else:
            await message.answer("Не удалось получить данные. Проверь тикер.")
    except Exception as e:
        await message.answer(f"Ошибка: {str(e)}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
