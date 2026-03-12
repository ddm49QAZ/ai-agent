from aiohttp import web

# Ответ для Render
async def handle(request):
    return web.Response(text="Бот работает!")

# В функции main (в самом низу):
runner = web.AppRunner(app)
await runner.setup()
# Берем порт, который дает Render
port = int(os.getenv("PORT", 10000))
site = web.TCPSite(runner, '0.0.0.0', port)
await site.start()
