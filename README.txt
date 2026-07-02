============================================================
 CHATBOT UDESC - Assistente para Estudantes Estrangeiros
 Disciplina: Redes de Computadores - TADS - UDESC/CCT - 2026/1
 Prof.: Janine Kniess
============================================================

DESCRIÇÃO
---------
Chatbot baseado em regras (máquina de estados) para auxiliar estudantes estrangeiros em intercâmbio na UDESC. 
Disponível via WhatsApp (Twilio) e Telegram.

IDIOMA
------
Antes de qualquer menu, o chatbot pergunta o idioma de preferência do usuário: Português ou English. Essa é sempre a primeira interação de um novo usuário (ou após digitar "reset"/limpar a sessão). 
Todo o conteúdo dos 8 menus abaixo está disponível nos dois idiomas. A qualquer momento o usuário pode digitar "idioma" (ou "language") para trocar o idioma escolhido.

MENUS IMPLEMENTADOS
-------------------
0. Escolha de idioma (Português / English) - primeira interação
1. Endereço e URL dos Centros UDESC
2. Sistemas acadêmicos (SIGA, Moodle, SIGAA)
3. Como obter o ID UDESC
4. Sistemas UDESC (SIGA, Moodle, Site, SAS, Office 365, Biblioteca)
5. CPF para estrangeiros + endereço da Receita Federal por centro
6. Equipe de Tutoria por centro
7. Serviço de Orientação ao Estudante (SOE)
8. Residência estudantil por centro

ESTRUTURA DO PROJETO
--------------------
udesc_chatbot/
|-- app.py                  -> Servidor Flask (WhatsApp + Telegram)
|-- teste_terminal.py       -> Teste local via terminal
|-- setup_telegram.py       -> Registra webhook do Telegram
|-- requirements.txt        -> Dependências Python
|-- README.txt              -> Este arquivo
|-- bot/
|   |-- __init__.py
|   |-- responder.py        -> Lógica do chatbot (máquina de estados)
|-- data/
    |-- __init__.py
    |-- udesc_data.py       -> Dados dos centros, sistemas e menus

============================================================
 PASSO A PASSO PARA EXECUÇÃO
============================================================

PRÉ-REQUISITOS
--------------
- Python 3.10 ou superior instalado
- pip (gerenciador de pacotes Python)
- Acesso à internet
- Conta Twilio (gratuita) para WhatsApp
- Conta Telegram e um bot criado via @BotFather para Telegram
- ngrok instalado (para expor o servidor local)
  Download: https://ngrok.com/download

------------------------------------------------------------
ETAPA 1 - INSTALAÇÃO DAS DEPENDÊNCIAS
------------------------------------------------------------

1.1 Abra o terminal na pasta do projeto:
    cd udesc_chatbot

1.2 (Opcional, recomendado) Crie um ambiente virtual:
    python -m venv venv

    Ative o ambiente virtual:
    - Windows:  venv\Scripts\activate
    - Linux/Mac: source venv/bin/activate

1.3 Instale as dependências:
    pip install -r requirements.txt

1.3.1 Se não funcionar, rode:
    sudo apt install python3-flask
    sudo apt install python3-twilio
    sudo apt install python3-requests

------------------------------------------------------------
ETAPA 2 - TESTE LOCAL VIA TERMINAL (sem WhatsApp/Telegram)
------------------------------------------------------------

Execute:
    python teste_terminal.py

O chatbot iniciará no terminal. Você pode navegar por todos os menus digitando os números das opções.

Para sair: digite "sair"
Para reiniciar a sessão: digite "reset"

------------------------------------------------------------
ETAPA 3 - EXECUTAR O SERVIDOR FLASK
------------------------------------------------------------

3.1 Inicie o servidor:
    python app.py

    O servidor rodará em http://localhost:5000

3.2 Teste via navegador (opcional):
    Abra: http://localhost:5000/chat?user=eu&msg=oi
    Mude o parâmetro 'msg' para simular mensagens.

------------------------------------------------------------
ETAPA 4 - EXPOR O SERVIDOR COM NGROK
------------------------------------------------------------

4.1 Em outro terminal, execute:
    ngrok http 5000

4.1.1 Ou então, rode o arquivo ngrok.exe e rode 
    ngrok http 5000

4.2 Registre uma conta, se necessário

4.3 O ngrok vai gerar uma URL pública, exemplo:
    https://abc123.ngrok.io

4.3.1 No caso,
    https://snuff-cover-geiger.ngrok-free.dev

4.4 Guarde essa URL - será usada nos passos seguintes.

ATENÇÃO: A URL do ngrok muda cada vez que você reinicia.
Repita o registro de webhook sempre que reiniciar o ngrok.

------------------------------------------------------------
ETAPA 5 - CONFIGURAR WHATSAPP VIA TWILIO
------------------------------------------------------------

5.1 Crie uma conta gratuita em: https://www.twilio.com

5.2 Acesse o Console Twilio:
    https://console.twilio.com

5.3 Vá em: Messaging > Try it out > Send a WhatsApp message

5.4 Siga as instruções para ativar o Sandbox:
    - Envie a mensagem indicada (ex: "join xxx-xxx") para o número Twilio via WhatsApp

5.5 Configure o Webhook no Sandbox:
    - Em "Sandbox Settings", defina:
      WHEN A MESSAGE COMES IN:
      URL: https://SEU-NGROK.ngrok.io/whatsapp
      Method: HTTP POST

5.6 Clique em "Save" e teste enviando uma mensagem do seu WhatsApp para o número Twilio.

5.7 Se não funcionar, repita o passo 5.4 com a mensagem "join amount-flower" para o número "+1 415 523 8886"

------------------------------------------------------------
ETAPA 6 - CONFIGURAR TELEGRAM
------------------------------------------------------------

6.1 No Telegram, converse com @BotFather:
    /newbot
    Siga as instruções para criar o bot.
    Guarde o TOKEN gerado (ex: 123456:ABCdef...)

6.2 Configure o TOKEN no arquivo app.py:
    Linha: TELEGRAM_BOT_TOKEN = "SEU_TOKEN_AQUI"
    Substitua pelo token real (8660995619:AAFoyYP9oCMTLG0RL1mqDL4tlNK9JrBRcyo)

    OU defina como variável de ambiente:
    - Windows:  set TELEGRAM_BOT_TOKEN=123456:ABCdef...
    - Linux/Mac: export TELEGRAM_BOT_TOKEN=123456:ABCdef...

6.3 Reinicie o servidor (python app.py) se já estiver rodando.

6.4 Registre o webhook do Telegram:
    python setup_telegram.py

    OU manualmente via curl:
    curl -X POST "https://api.telegram.org/bot<TOKEN>/setWebhook" \
         -d "url=https://SEU-NGROK.ngrok.io/telegram/<TOKEN>"

6.5 Teste abrindo o Telegram, buscando seu bot pelo nome
    e enviando /start ou "oi".

------------------------------------------------------------
ETAPA 7 - VERIFICAÇÃO FINAL
------------------------------------------------------------

7.1 Verifique que o servidor Flask está rodando (python app.py)
7.2 Verifique que o ngrok está ativo e a URL está correta
7.3 Teste no WhatsApp: envie "oi" para o número Twilio
7.4 Teste no Telegram: envie /start para seu bot
7.5 Navegue por todos os 8 menus e verifique as respostas

============================================================
 INFORMAÇÕES DE REDE (para apresentação oral)
============================================================

PROTOCOLO DE TRANSPORTE: TCP
O Flask/HTTP e o Telegram/WhatsApp usam TCP na camada de
transporte, pois exigem entrega garantida e ordenada.

PORTAS:
- Servidor local Flask:  porta 5000 (configurável via PORT)
- HTTPS para Twilio/Telegram: porta 443 (destino)
- ngrok tunnel: porta local 5000 → URL pública 443

IDENTIFICAR IP ORIGEM E DESTINO (exemplo):
- Use Wireshark ou tcpdump para capturar o tráfego
- IP origem: IP da sua máquina (verifique com: ipconfig / ifconfig)
- IP destino: IP do servidor Twilio ou api.telegram.org
  Resolver: nslookup api.telegram.org

FLUXO DE COMUNICAÇÃO:
  Usuário (WhatsApp)
      \/ TCP/HTTPS (porta 443)
  Twilio API (servidor Twilio)
      \/ POST HTTP Webhook (TCP, porta 5000 via ngrok)
  ngrok tunnel
      \/
  Flask (localhost:5000)
      \/
  bot/responder.py (lógica baseada em regras)
      \/ resposta TwiML XML
  Twilio API
      \/
  Usuário (WhatsApp)

============================================================
 DEPENDÊNCIAS
============================================================

Flask      >= 2.3.0  - Servidor web / API HTTP
twilio     >= 8.0.0  - Integração com WhatsApp via Twilio
requests   >= 2.31.0 - Envio de mensagens para Telegram API

Python stdlib (sem instalação adicional):
  os, sys  - Variáveis de ambiente e caminhos

============================================================
 AUTORES
============================================================

[Jean Ernani Witt Meier, Kauane Delvoss Ribas, Laura Helena Schmaltz da Costa]
UDESC/CCT - Tecnólogo em Análise e Desenvolvimento de Sistemas / TADS
Disciplina: Redes de Computadores - 2026/1

============================================================
