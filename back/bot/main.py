"""TG-bot module"""
import asyncio
from aiogram import Bot, Dispatcher

from . import handlers
from .config import TELEGRAM_BOT_TOKEN


bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher()

dp.include_router(handlers.router)

async def main():
    """Run tg-bot"""
    print("Tg-bot started...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
