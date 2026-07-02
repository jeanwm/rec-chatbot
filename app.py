"""
app.py
servidor flask do chatbot UDESC.
suporta:
  - whatsApp via twilio sandbox (POST /whatsapp)
  - telegram via webhook      (POST /telegram/<TOKEN>)
  - teste via terminal        (GET  /chat?user=xxx&msg=yyy)
"""

import os
from flask import Flask, request, Response
from twilio.twiml.messaging_response import MessagingResponse
import requests

from bot.responder import responder

app = Flask(__name__)

# ------------------------------------------------------------------ #
# configurações (defina como variáveis de ambiente ou edite aqui)
# ------------------------------------------------------------------ #
TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "8660995619:AAFoyYP9oCMTLG0RL1mqDL4tlNK9JrBRcyo")


# ------------------------------------------------------------------ #
# Rota WhatsApp - Twilio
# ------------------------------------------------------------------ #
@app.route("/whatsapp", methods=["POST"])
def whatsapp():
    """
    twilio envia um POST com 'Body' (texto) e 'From' (número do usuário). retorna TwiML com a resposta.
    """
    msg_recebida = request.form.get("Body", "").strip()
    numero       = request.form.get("From", "unknown")

    print(f"[WhatsApp] De: {numero} | Msg: {msg_recebida}")

    resposta_texto = responder(user_id=numero, mensagem_raw=msg_recebida)

    twiml = MessagingResponse()
    twiml.message(resposta_texto)

    return Response(str(twiml), mimetype="application/xml")


# ------------------------------------------------------------------ #
# rota telegram - webhook
# ------------------------------------------------------------------ #
@app.route(f"/telegram/{TELEGRAM_BOT_TOKEN}", methods=["POST"])
def telegram():
    """
    o telegram envia um JSON com a mensagem do usuário. responde enviando uma requisição de volta à api do telegram.
    """
    data = request.get_json(force=True)

    # extrai informações do update
    message = data.get("message", {})
    if not message:
        return "ok", 200

    chat_id   = message.get("chat", {}).get("id")
    texto     = message.get("text", "").strip()
    user_name = message.get("from", {}).get("first_name", "")

    if not chat_id or not texto:
        return "ok", 200

    print(f"[Telegram] De: {user_name} (chat_id={chat_id}) | Msg: {texto}")

    resposta_texto = responder(user_id=f"telegram_{chat_id}", mensagem_raw=texto)

    # envia a resposta de volta ao Telegram
    telegram_url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id":    chat_id,
        "text":       resposta_texto,
        "parse_mode": "Markdown",
    }
    try:
        r = requests.post(telegram_url, json=payload, timeout=10)
        print(f"[Telegram] Resposta enviada. Status: {r.status_code}")
    except Exception as e:
        print(f"[Telegram] Erro ao enviar resposta: {e}")

    return "ok", 200


# ------------------------------------------------------------------ #
# rota de teste (via navegador ou curl)
# ------------------------------------------------------------------ #
@app.route("/chat", methods=["GET"])
def chat_teste():
    """
    rota de teste simples.
    uso: GET /chat?user=teste&msg=oi
    """
    user_id = request.args.get("user", "teste_user")
    msg     = request.args.get("msg", "oi")
    resp    = responder(user_id=user_id, mensagem_raw=msg)
    return f"<pre>{resp}</pre>", 200


# ------------------------------------------------------------------ #
# rota de status
# ------------------------------------------------------------------ #
@app.route("/", methods=["GET"])
def health():
    return "Chatbot UDESC está online!", 200


# ------------------------------------------------------------------ #
# inicialização
# ------------------------------------------------------------------ #
if __name__ == "__main__":
    porta = int(os.environ.get("PORT", 5000))
    print("=" * 50)
    print("  Chatbot UDESC - Estudantes Estrangeiros")
    print(f"  Servidor rodando na porta {porta}")
    print(f"  Webhook Telegram: /telegram/8660995619:AAFoyYP9oCMTLG0RL1mqDL4tlNK9JrBRcyo")
    print(f"  Webhook WhatsApp: /whatsapp")
    print(f"  Teste: http://localhost:{porta}/chat?user=eu&msg=oi")
    print("=" * 50)
    app.run(debug=True, host="0.0.0.0", port=porta)
