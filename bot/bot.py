import asyncio
from os import getenv
from aiogram import Bot, Dispatcher
from handlers.handlers import router as handlers_router
from dotenv import load_dotenv
from handlers.commands import my_commands
load_dotenv()
TOKEN = getenv("BOT_TOKEN")
API_KEY = getenv("API_KEY")


dp = Dispatcher()
dp.include_router(handlers_router)

async def main() -> None:
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)
    await bot.set_my_commands(my_commands)
if __name__ == "__main__":
    print("Starting bot...")
    asyncio.run(main())


