from fastapi import FastAPI, Request
from telegram import Update, Bot
from telegram.ext import Application, CommandHandler, ContextTypes
import os
import asyncio
from donna import setup_handlers

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

app = FastAPI()
bot = Bot(token=BOT_TOKEN)
telegram_app = Application.builder().token(BOT_TOKEN).build()

# Registra os comandos
setup_handlers(telegram_app)

@app.on_event("startup")
async def startup():
    await bot.set_webhook(f"{WEBHOOK_URL}/webhook")
    asyncio.create_task(telegram_app.initialize())
    print("🚀 Webhook registrado com sucesso.")

@app.post("/webhook")
async def telegram_webhook(req: Request):
    data = await req.json()
    await telegram_app.update_queue.put(Update.de_json(data=data, bot=bot))
    return {"ok": True}