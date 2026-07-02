"""
teste_terminal.py
teste interativo do chatbot diretamente no terminal para validar todos os fluxos sem precisar de whatsApp ou telegram

uso:
    python teste_terminal.py
"""

from bot.responder import responder

USER_ID = "usuario_teste"

print("=" * 60)
print("  CHATBOT UDESC - Teste via Terminal")
print("  A primeira mensagem vai pedir o idioma (1-PT / 2-EN)")
print("  Digite 'idioma' ou 'language' para trocar de idioma")
print("  Digite 'sair' para encerrar")
print("  Digite 'reset' para reiniciar a sessão")
print("=" * 60)
print()

# inicia com a mensagem de boas-vindas
print(responder(USER_ID, "oi"))
print()

while True:
    try:
        entrada = input("Você: ").strip()
    except (EOFError, KeyboardInterrupt):
        print("\n[Erro! Encerrando chatbot.]")
        break

    if entrada.lower() == "sair":
        print("[Até a próxima!]")
        break

    if entrada.lower() == "reset":
        from bot import responder as mod
        mod._sessoes.clear()
        print("[Sessão reiniciada.]")
        print(responder(USER_ID, "oi"))
        print()
        continue

    if not entrada:
        continue

    resposta = responder(USER_ID, entrada)
    print(f"\nBot: {resposta}\n")
