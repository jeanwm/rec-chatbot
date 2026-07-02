"""
bot/responder.py
lógica do chatbot UDESC baseado em regras - máquina de estados por usuário.
suporte bilíngue: a primeira interação sempre pergunta o idioma (português ou inglês) antes de mostrar o menu principal.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from data.udesc_data import (
    CENTROS, SISTEMAS, SISTEMAS_UDESC,
    SOE_INFO, ID_UDESC_INFO, CPF_INFO
)


# ------------------------------------------------------------------ #
# máquina de estados: cada chave é o ID do usuário (número de telefone ou chat_id) e o valor é um dicionário com 'estado', 'idioma' e dados temporários.
# ------------------------------------------------------------------ #
_sessoes = {}


# ---- estados possíveis ------------------------------------------- #
ESTADO_IDIOMA        = "escolha_idioma"
ESTADO_MENU_PRINC    = "menu_principal"
ESTADO_MENU1         = "menu1_escolhe_centro"
ESTADO_MENU2         = "menu2_escolhe_sistema"
ESTADO_MENU4         = "menu4_escolhe_subsistema"
ESTADO_MENU5_CENTRO  = "menu5_escolhe_centro_cpf"
ESTADO_MENU6         = "menu6_escolhe_centro_tutoria"

# ---- idiomas suportados ------------------------------------------- #
IDIOMA_PADRAO = "pt"

def _get_sessao(user_id: str) -> dict:
    if user_id not in _sessoes:
        _sessoes[user_id] = {"estado": ESTADO_IDIOMA, "centro_id": None, "idioma": None}
    return _sessoes[user_id]

def _set_estado(user_id: str, estado: str, **extras):
    s = _get_sessao(user_id)
    s["estado"] = estado
    s.update(extras)


# ------------------------------------------------------------------ #
# seleção de idioma (primeira opção apresentada ao usuário)
# ------------------------------------------------------------------ #

_MAPA_IDIOMA = {
    "1": "pt", "pt": "pt", "pt-br": "pt", "português": "pt", "portugues": "pt", "portuguese": "pt",
    "2": "en", "en": "en", "en-us": "en", "english": "en", "inglês": "en", "ingles": "en",
}

def _msg_escolha_idioma() -> str:
    return (
        "*Bem-vindo(a) à UDESC! / Welcome to UDESC!*\n\n"
        "Por favor, escolha seu idioma / Please choose your language:\n\n"
        "1- Português\n"
        "2- English\n"
    )

def _tratar_escolha_idioma(user_id: str, msg: str) -> str:
    if msg in _MAPA_IDIOMA:
        idioma = _MAPA_IDIOMA[msg]
        _set_estado(user_id, ESTADO_MENU_PRINC, idioma=idioma)
        return _msg_boas_vindas(idioma)
    return _msg_escolha_idioma()


# ------------------------------------------------------------------ #
# textos fixos (bilíngues)
# ------------------------------------------------------------------ #

def _msg_boas_vindas(idioma: str) -> str:
    if idioma == "en":
        return (
            "*Welcome to UDESC!*\n\n"
            "This chatbot helps international exchange students.\n\n"
            + _msg_menu_principal(idioma)
        )
    return (
        "*Bem-vindo(a) à UDESC!*\n\n"
        "Este chatbot ajuda estudantes estrangeiros em intercâmbio.\n\n"
        + _msg_menu_principal(idioma)
    )

def _msg_menu_principal(idioma: str) -> str:
    if idioma == "en":
        return (
            "*MAIN MENU* - Type the option number:\n\n"
            "1- UDESC Campus Addresses\n"
            "2- Academic Systems (SIGA, Moodle, SIGAA)\n"
            "3- How to get your UDESC ID\n"
            "4- UDESC Systems and Services\n"
            "5- CPF for Foreigners\n"
            "6- Tutoring Team\n"
            "7- Student Guidance Service (SOE)\n"
            "8- Student Housing\n\n"
            "Type *menu* anytime to return here.\n"
            "Type *language* to change the language."
        )
    return (
        "*MENU PRINCIPAL* - Digite o número da opção:\n\n"
        "1- Endereço dos Centros UDESC\n"
        "2- Sistemas acadêmicos (SIGA, Moodle, SIGAA)\n"
        "3- Como obter o ID UDESC\n"
        "4- Sistemas e serviços UDESC\n"
        "5- CPF para estrangeiros\n"
        "6- Equipe de Tutoria\n"
        "7- Serviço de Orientação ao Estudante (SOE)\n"
        "8- Residência Estudantil\n\n"
        "Digite *menu* a qualquer momento para voltar aqui.\n"
        "Digite *idioma* para trocar de idioma."
    )

# texto de contexto exibido junto da lista de centros, conforme o motivo
_TEXTOS_PROPOSITO_CENTRO = {
    "endereco":   {"pt": "",                                              "en": ""},
    "tutoria":    {"pt": " para ver a equipe de tutoria",                 "en": " to see the tutoring team"},
    "cpf":        {"pt": " para ver a Receita Federal mais próxima",      "en": " to see the nearest Federal Revenue (Receita Federal) office"},
    "residencia": {"pt": " para ver informações de residência estudantil","en": " to see student housing information"},
}

def _msg_lista_centros(idioma: str, proposito: str = "endereco") -> str:
    contexto = _TEXTOS_PROPOSITO_CENTRO.get(proposito, {}).get(idioma, "")
    titulo = "*Escolha seu centro" if idioma == "pt" else "*Choose your campus"
    texto = f"{titulo}{contexto}:*\n\n"
    for k, c in CENTROS.items():
        texto += f"{k}- {c['sigla']} - {c['nome']} ({c['cidade']})\n"
    return texto

def _msg_lista_sistemas(idioma: str) -> str:
    if idioma == "en":
        return (
            "*Choose the system:*\n\n"
            "1- SIGA\n"
            "2- Moodle\n"
            "3- SIGAA\n"
        )
    return (
        "*Escolha o sistema:*\n\n"
        "1- SIGA\n"
        "2- Moodle\n"
        "3- SIGAA\n"
    )

def _msg_lista_subsistemas(idioma: str) -> str:
    if idioma == "en":
        return (
            "*UDESC Systems and Services - Choose:*\n\n"
            "1- SIGA (grades and attendance)\n"
            "2- Moodle (courses and assignments)\n"
            "3- UDESC Website (curriculum, professors)\n"
            "4- SAS (room booking)\n"
            "5- Office 365 (institutional email, Word, Excel...)\n"
            "6- Online Library\n"
        )
    return (
        "*Sistemas e Serviços UDESC - Escolha:*\n\n"
        "1- SIGA (notas e faltas)\n"
        "2- Moodle (disciplinas e exercícios)\n"
        "3- Site UDESC (PPC, professores)\n"
        "4- SAS (agendamento de salas)\n"
        "5- Office 365 (e-mail institucional, Word, Excel...)\n"
        "6- Biblioteca Online\n"
    )

def _msg_erro_opcao(idioma: str, validas: list) -> str:
    opts = ", ".join(validas)
    if idioma == "en":
        return (
            f"Invalid option. Type a number from the available options ({opts}).\n"
            "Type *menu* to return to the main menu."
        )
    return (
        f"Opção inválida. Digite um número entre as opções disponíveis ({opts}).\n"
        "Digite *menu* para voltar ao menu principal."
    )

def _rodape_menu(idioma: str) -> str:
    return "\n\nType *menu* to go back." if idioma == "en" else "\n\nDigite *menu* para voltar."

def _is_saudacao(msg: str) -> bool:
    palavras = {"oi", "olá", "ola", "hello", "hi", "hola", "bom dia", "boa tarde", "boa noite", "hey", "start", "/start", "good morning", "good afternoon", "good evening"}
    return any(p in msg for p in palavras)

def _is_menu(msg: str) -> bool:
    return msg in {"menu", "voltar", "inicio", "início", "back", "home", "main"}

def _is_comando_idioma(msg: str) -> bool:
    return msg in {"idioma", "language", "lang", "/idioma", "/language"}


# ------------------------------------------------------------------ #
# função principal de resposta
# ------------------------------------------------------------------ #

def responder(user_id: str, mensagem_raw: str) -> str:
    """
    recebe user_id e mensagem, retorna a resposta do chatbot. toda a lógica é baseada em regras (máquina de estados). 
    a primeira interação de cada usuário sempre pergunta o idioma antes de seguir para o menu principal.
    """
    msg = mensagem_raw.strip().lower()
    s   = _get_sessao(user_id)

    # ---- passo 0: se o usuário ainda não escolheu o idioma, trata isso antes de tudo ---- #
    if s.get("idioma") is None:
        return _tratar_escolha_idioma(user_id, msg)

    idioma = s["idioma"]

    # ---- comando global para trocar de idioma a qualquer momento ---- #
    if _is_comando_idioma(msg):
        _set_estado(user_id, ESTADO_IDIOMA, idioma=None)
        return _msg_escolha_idioma()

    # ---- comandos globais que funcionam em qualquer estado ---- #
    if _is_saudacao(msg) or _is_menu(msg):
        _set_estado(user_id, ESTADO_MENU_PRINC)
        return _msg_menu_principal(idioma)

    estado = s["estado"]

    # ---- estado: aguardando opção do menu principal ---- #
    if estado == ESTADO_MENU_PRINC:
        return _tratar_menu_principal(user_id, msg, idioma)

    # ---- estado: menu 1 - escolher centro ---- #
    elif estado == ESTADO_MENU1:
        return _tratar_menu1(user_id, msg, idioma)

    # ---- estado: menu 2 - escolher sistema ---- #
    elif estado == ESTADO_MENU2:
        return _tratar_menu2(user_id, msg, idioma)

    # ---- estado: menu 4 - escolher subsistema ---- #
    elif estado == ESTADO_MENU4:
        return _tratar_menu4(user_id, msg, idioma)

    # ---- estado: menu 5 - escolher centro para CPF ---- #
    elif estado == ESTADO_MENU5_CENTRO:
        return _tratar_menu5_centro(user_id, msg, idioma)

    # ---- estado: menu 6 - escolher centro para tutoria ---- #
    elif estado == ESTADO_MENU6:
        return _tratar_menu6(user_id, msg, idioma)

    # fallback
    else:
        _set_estado(user_id, ESTADO_MENU_PRINC)
        prefixo = "Sorry, I didn't understand. See the menu below:\n\n" if idioma == "en" \
            else "Desculpe, não entendi. Veja o menu abaixo:\n\n"
        return prefixo + _msg_menu_principal(idioma)


# ------------------------------------------------------------------ #
# tratadores por estado
# ------------------------------------------------------------------ #

def _tratar_menu_principal(user_id: str, msg: str, idioma: str) -> str:
    opcoes = {
        "1": _acao_menu1,
        "2": _acao_menu2,
        "3": _acao_menu3,
        "4": _acao_menu4,
        "5": _acao_menu5,
        "6": _acao_menu6,
        "7": _acao_menu7,
        "8": _acao_menu8,
    }
    if msg in opcoes:
        _set_estado(user_id, ESTADO_MENU_PRINC)
        return opcoes[msg](user_id, idioma)
    aviso = "Option not recognized. " if idioma == "en" else "Opção não reconhecida. "
    return aviso + _msg_menu_principal(idioma)

def _acao_menu1(user_id: str, idioma: str) -> str:
    _set_estado(user_id, ESTADO_MENU1, contexto_menu="endereco")
    return _msg_lista_centros(idioma, "endereco")

def _acao_menu2(user_id: str, idioma: str) -> str:
    _set_estado(user_id, ESTADO_MENU2)
    return _msg_lista_sistemas(idioma)

def _acao_menu3(user_id: str, idioma: str) -> str:
    _set_estado(user_id, ESTADO_MENU_PRINC)
    return ID_UDESC_INFO[idioma] + _rodape_menu(idioma)

def _acao_menu4(user_id: str, idioma: str) -> str:
    _set_estado(user_id, ESTADO_MENU4)
    return _msg_lista_subsistemas(idioma)

def _acao_menu5(user_id: str, idioma: str) -> str:
    _set_estado(user_id, ESTADO_MENU5_CENTRO)
    return CPF_INFO[idioma] + "\n\n" + _msg_lista_centros(idioma, "cpf")

def _acao_menu6(user_id: str, idioma: str) -> str:
    _set_estado(user_id, ESTADO_MENU6)
    return _msg_lista_centros(idioma, "tutoria")

def _acao_menu7(user_id: str, idioma: str) -> str:
    _set_estado(user_id, ESTADO_MENU_PRINC)
    return SOE_INFO[idioma] + _rodape_menu(idioma)

def _acao_menu8(user_id: str, idioma: str) -> str:
    _set_estado(user_id, ESTADO_MENU1, contexto_menu="residencia")
    return _msg_lista_centros(idioma, "residencia")


# ---- menu 1: endereço do centro ---- #

def _tratar_menu1(user_id: str, msg: str, idioma: str) -> str:
    s = _get_sessao(user_id)
    contexto = s.get("contexto_menu", "endereco")

    if msg not in CENTROS:
        return _msg_erro_opcao(idioma, list(CENTROS.keys()))

    c = CENTROS[msg]
    _set_estado(user_id, ESTADO_MENU_PRINC, contexto_menu=None)

    if contexto == "residencia":
        if idioma == "en":
            res_status = "Has student housing" if c["tem_residencia"] else "Does not have its own student housing"
            est_status = "Available for foreign students" if c["residencia_estrangeiro"] else "Not currently available for foreign students"
            return (
                f"*Student Housing - {c['sigla']}*\n\n"
                f"{res_status}\n"
                f"{est_status}\n\n"
                f"{c['info_residencia']['en']}\n\n"
                "Type *menu* to go back."
            )
        res_status = "Possui residência estudantil" if c["tem_residencia"] else "Não possui residência estudantil própria"
        est_status = "Atende estrangeiros" if c["residencia_estrangeiro"] else "Não disponível para estrangeiros no momento"
        return (
            f"*Residência Estudantil - {c['sigla']}*\n\n"
            f"{res_status}\n"
            f"{est_status}\n\n"
            f"{c['info_residencia']['pt']}\n\n"
            "Digite *menu* para voltar."
        )

    # caso padrão: endereço
    if idioma == "en":
        return (
            f"*{c['nome']} ({c['sigla']})*\n\n"
            f"City: {c['cidade']}\n"
            f"Address: {c['endereco']}\n"
            f"Phone: {c['tel']}\n"
            f"Website: {c['url']}\n\n"
            "Type *menu* to go back."
        )
    return (
        f"*{c['nome']} ({c['sigla']})*\n\n"
        f"Cidade: {c['cidade']}\n"
        f"Endereço: {c['endereco']}\n"
        f"Telefone: {c['tel']}\n"
        f"Site: {c['url']}\n\n"
        "Digite *menu* para voltar."
    )


# ---- menu 2: sistemas ---- #

def _tratar_menu2(user_id: str, msg: str, idioma: str) -> str:
    if msg not in SISTEMAS:
        return _msg_erro_opcao(idioma, list(SISTEMAS.keys()))

    sis = SISTEMAS[msg]
    _set_estado(user_id, ESTADO_MENU_PRINC)
    return sis["info"][idioma] + _rodape_menu(idioma)


# ---- menu 4: subsistemas ---- #

def _tratar_menu4(user_id: str, msg: str, idioma: str) -> str:
    if msg not in SISTEMAS_UDESC:
        return _msg_erro_opcao(idioma, list(SISTEMAS_UDESC.keys()))

    sub = SISTEMAS_UDESC[msg]
    _set_estado(user_id, ESTADO_MENU_PRINC)
    return sub["info"][idioma] + _rodape_menu(idioma)


# ---- menu 5: receita federal por centro ---- #

def _tratar_menu5_centro(user_id: str, msg: str, idioma: str) -> str:
    if msg not in CENTROS:
        return _msg_erro_opcao(idioma, list(CENTROS.keys()))

    c = CENTROS[msg]
    _set_estado(user_id, ESTADO_MENU_PRINC)

    if idioma == "en":
        return (
            f"*Nearest Federal Revenue Office (Receita Federal) to {c['sigla']}*\n\n"
            f"{c['receita_federal']['en']}\n\n"
            "*Remember to bring:*\n"
            "  - Original passport\n"
            "  - Valid student visa\n"
            "  - UDESC enrollment certificate\n"
            "  - Online application protocol number\n\n"
            "Type *menu* to go back."
        )
    return (
        f"*Receita Federal mais próxima do {c['sigla']}*\n\n"
        f"{c['receita_federal']['pt']}\n\n"
        "*Lembre-se de levar:*\n"
        "  - Passaporte original\n"
        "  - Visto de estudante\n"
        "  - Comprovante de matrícula UDESC\n"
        "  - Número de protocolo da solicitação online\n\n"
        "Digite *menu* para voltar."
    )


# ---- menu 6: tutoria por centro ---- #

def _tratar_menu6(user_id: str, msg: str, idioma: str) -> str:
    if msg not in CENTROS:
        return _msg_erro_opcao(idioma, list(CENTROS.keys()))

    c = CENTROS[msg]
    equipe_str = "\n".join(f"  • {m}" for m in c["tutoria_equipe"][idioma])
    _set_estado(user_id, ESTADO_MENU_PRINC)

    if idioma == "en":
        return (
            f"*Tutoring Team - {c['sigla']}*\n\n"
            f"Website: {c['tutoria_site']}\n"
            f"Email: {c['tutoria_email']}\n"
            f"Phone: {c['tutoria_tel']}\n\n"
            f"*Team:*\n{equipe_str}\n\n"
            "Type *menu* to go back."
        )
    return (
        f"*Equipe de Tutoria - {c['sigla']}*\n\n"
        f"Site: {c['tutoria_site']}\n"
        f"E-mail: {c['tutoria_email']}\n"
        f"Telefone: {c['tutoria_tel']}\n\n"
        f"*Equipe:*\n{equipe_str}\n\n"
        "Digite *menu* para voltar."
    )
