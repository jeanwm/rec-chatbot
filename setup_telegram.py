"""
setup_telegram.py
registra o webhook do Telegram apontando para o servidor (via ngrok ou URL pública).

uso:
    python setup_telegram.py
"""

import requests
import os

# ---- Configure aqui -------------------------------------------- #
TOKEN    = os.environ.get("TELEGRAM_BOT_TOKEN", "8660995619:AAFoyYP9oCMTLG0RL1mqDL4tlNK9JrBRcyo")
BASE_URL = os.environ.get("WEBHOOK_BASE_URL", "https://snuff-cover-geiger.ngrok-free.dev")
# ---------------------------------------------------------------- #

WEBHOOK_URL = f"{BASE_URL}/telegram/{TOKEN}"

print(f"Registrando webhook: {WEBHOOK_URL}")

r = requests.post(
    f"https://api.telegram.org/bot{TOKEN}/setWebhook",
    json={"url": WEBHOOK_URL}
)

print(f"Status: {r.status_code}")
print(f"Resposta: {r.json()}")

# verificar info do bot
info = requests.get(f"https://api.telegram.org/bot{TOKEN}/getMe").json()
print(f"\nBot: @{info.get('result', {}).get('username', '?')}")
print("Webhook configurado com sucesso.")
