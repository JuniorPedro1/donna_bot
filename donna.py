from fastapi import Request
import httpx
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

async def send_message(chat_id, text):
    async with httpx.AsyncClient() as client:
        await client.post(f"{API_URL}/sendMessage", json={"chat_id": chat_id, "text": text})

async def handle_webhook(update):
    message = update.get("message", {})
    text = message.get("text", "")
    chat_id = message.get("chat", {}).get("id")

    if not chat_id or not text:
        return {"ok": True}

    if text.startswith("/start"):
        await send_message(chat_id, "Sou a DONNA — sua secretária pessoal.
Pode me chamar a qualquer hora!")
    elif text.startswith("/microvitoria"):
        await send_message(chat_id, "✅ Microvitória do dia: você deu mais um passo rumo ao topo.")
    elif text.startswith("/lembrete"):
        await send_message(chat_id, "📌 Lembrete anotado! Vou te avisar.")
    else:
        await send_message(chat_id, "Desculpa, não entendi. Me envie /start, /microvitoria ou /lembrete.")

    return {"ok": True}