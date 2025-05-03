from fastapi import FastAPI
from donna import handle_webhook
import os

app = FastAPI()

@app.get("/")
def root():
    return {"status": "DONNA online"}

@app.post(f"/webhook/{os.getenv('BOT_TOKEN').split(':')[0]}")
async def telegram_webhook(update: dict):
    return await handle_webhook(update)