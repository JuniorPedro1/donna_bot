# DONNA Bot – Telegram + FastAPI

### Comandos disponíveis:

- /start → Mensagem inicial
- /lembrete <texto> → Cria lembrete
- /microvitoria → Envia frase motivacional personalizada

### Como rodar local:
1. pip install -r requirements.txt
2. uvicorn main:app --reload

### Como subir na Railway:
1. Crie projeto com "Deploy from GitHub"
2. Adicione BOT_TOKEN e WEBHOOK_URL nas variáveis
3. Pronto! Telegram começa a responder.