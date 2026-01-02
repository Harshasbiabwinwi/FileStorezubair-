import os
import threading
from aiohttp import web
from pyrogram import Client
from config import (
    API_ID,
    API_HASH,
    BOT_TOKEN
)

# ---------------- WEB SERVER (Koyeb Health Check FIX) ---------------- #

def run_web():
    app = web.Application()
    app.router.add_get("/", lambda r: web.Response(text="FileStore Bot is Alive ✅"))
    web.run_app(
        app,
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 8000))
    )

threading.Thread(target=run_web).start()

# ---------------- PYROGRAM BOT ---------------- #

app = Client(
    "FileStoreBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

print("🤖 FileStore Bot Started Successfully")

app.run()

