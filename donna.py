from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Frases motivacionais
MICROVITORIAS = [
    "🔥 Você já venceu só por levantar da cama com dois filhos pequenos!",
    "🚀 Só de não ter surtado hoje, já tá no lucro!",
    "📦 Empresa rodada, filhos vivos, você tá jogando no hard mode e indo bem."
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Sou a DONNA — sua secretária pessoal. Pode me pedir lembrete, microvitória ou me xingar se quiser.")

async def lembrete(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = ' '.join(context.args) or "lembrete padrão"
    await update.message.reply_text(f"⏰ Lembrete registrado: {msg}")

async def microvitoria(update: Update, context: ContextTypes.DEFAULT_TYPE):
    from random import choice
    await update.message.reply_text(f"💪 Microvitória de hoje: {choice(MICROVITORIAS)}")

def setup_handlers(app: Application):
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("lembrete", lembrete))
    app.add_handler(CommandHandler("microvitoria", microvitoria))