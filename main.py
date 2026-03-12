import asyncio, os, logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from groq import Groq
from aiohttp import web

logging.basicConfig(level=logging.INFO)

# Инициализация (данные берутся из настроек Render)
bot = Bot(token=os.getenv("TELEGRAM_TOKEN"))
dp = Dispatcher()
groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Ответ для Render (чтобы не было ошибки "Port scan timeout")
async def handle(request):
    return web.Response(text="Бот запущен и работает!")

app = web.Application()
app.router.add_get('/', handle)

@dp.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer("Здравствуйте! Я ваш ИИ-помощник. Чем могу помочь?")

async def main():
    # Настройка порта для Render
    runner = web.AppRunner(app)
    await runner.setup()
    port = int(os.getenv("PORT", 10000))
    site = web.TCPSite(runner, '0.0.0.0', port)
    await site.start()
    
    print(f"Сервер запущен на порту {port}")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
