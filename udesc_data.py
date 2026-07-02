# ============================================================
# Dados da UDESC - Chatbot para Estudantes Estrangeiros
# Conteúdo bilíngue: Português (pt) e Inglês (en)
# ============================================================

CENTROS = {
    "1": {
        "sigla": "CAV",
        "nome": "Centro de Ciências Agroveterinárias",
        "cidade": "Lages - SC",
        "endereco": "Av. Luiz de Camões, 2090 - Conta Dinheiro, Lages/SC - CEP: 88520-000",
        "url": "https://www.udesc.br/cav",
        "tel": "(49) 3289-9100",
        "tem_residencia": True,
        "residencia_estrangeiro": True,
        "info_residencia": {
            "pt": "O CAV possui residência estudantil disponível para estudantes estrangeiros. Entre em contato com a coordenação para verificar vagas: intercambio.cav@udesc.br | (49) 3289-9100",
            "en": "CAV has student housing available for international students. Contact the coordination office to check for available spots: intercambio.cav@udesc.br | (49) 3289-9100",
        },
        "tutoria_site": "https://www.udesc.br/cav/tutoria",
        "tutoria_email": "tutoria.cav@udesc.br",
        "tutoria_tel": "(49) 3289-9100",
        "tutoria_equipe": {
            "pt": ["Equipe de Tutoria CAV - consulte o site para informações atualizadas."],
            "en": ["CAV Tutoring Team - check the website for updated information."],
        },
        "receita_federal": {
            "pt": "Receita Federal - Lages\nRua Getúlio Vargas, 280 - Centro, Lages/SC\nTel: (49) 3251-6200 | Horário: segunda a sexta, 8h às 17h",
            "en": "Federal Revenue Office (Receita Federal) - Lages\nRua Getúlio Vargas, 280 - Centro, Lages/SC\nPhone: (49) 3251-6200 | Hours: Monday to Friday, 8 AM to 5 PM",
        },
    },
    "2": {
        "sigla": "CEAD",
        "nome": "Centro de Educação à Distância",
        "cidade": "Florianópolis - SC",
        "endereco": "Av. Madre Benvenuta, 2007 - Itacorubi, Florianópolis/SC - CEP: 88035-001",
        "url": "https://www.udesc.br/cead",
        "tel": "(48) 3664-8400",
        "tem_residencia": False,
        "residencia_estrangeiro": False,
        "info_residencia": {
            "pt": "O CEAD é um centro de educação a distância com polo presencial em Florianópolis. O SOE pode indicar opções de moradia: soe@udesc.br",
            "en": "CEAD is a distance education center with a campus in Florianópolis. The SOE can suggest housing options: soe@udesc.br",
        },
        "tutoria_site": "https://www.udesc.br/cead/tutoria",
        "tutoria_email": "tutoria.cead@udesc.br",
        "tutoria_tel": "(48) 3664-8400",
        "tutoria_equipe": {
            "pt": ["Equipe de Tutoria CEAD - consulte o site para informações atualizadas."],
            "en": ["CEAD Tutoring Team - check the website for updated information."],
        },
        "receita_federal": {
            "pt": "Receita Federal - Florianópolis\nRua Vital Brasil, 91 - Estreito, Florianópolis/SC\nTel: (48) 2109-5100 | Horário: segunda a sexta, 8h às 17h",
            "en": "Federal Revenue Office (Receita Federal) - Florianópolis\nRua Vital Brasil, 91 - Estreito, Florianópolis/SC\nPhone: (48) 2109-5100 | Hours: Monday to Friday, 8 AM to 5 PM",
        },
    },
    "3": {
        "sigla": "CEART",
        "nome": "Centro de Artes, Design e Moda",
        "cidade": "Florianópolis - SC",
        "endereco": "Av. Madre Benvenuta, 1907 - Itacorubi, Florianópolis/SC - CEP: 88035-001",
        "url": "https://www.udesc.br/ceart",
        "tel": "(48) 3664-8300",
        "tem_residencia": False,
        "residencia_estrangeiro": False,
        "info_residencia": {
            "pt": "O CEART não possui residência estudantil própria. O SOE pode indicar opções de moradia na cidade: soe@udesc.br",
            "en": "CEART does not have its own student housing. The SOE can suggest housing options in the city: soe@udesc.br",
        },
        "tutoria_site": "https://www.udesc.br/ceart/tutoria",
        "tutoria_email": "tutoria.ceart@udesc.br",
        "tutoria_tel": "(48) 3664-8300",
        "tutoria_equipe": {
            "pt": ["Equipe de Tutoria CEART - consulte o site para informações atualizadas."],
            "en": ["CEART Tutoring Team - check the website for updated information."],
        },
        "receita_federal": {
            "pt": "Receita Federal - Florianópolis\nRua Vital Brasil, 91 - Estreito, Florianópolis/SC\nTel: (48) 2109-5100 | Horário: segunda a sexta, 8h às 17h",
            "en": "Federal Revenue Office (Receita Federal) - Florianópolis\nRua Vital Brasil, 91 - Estreito, Florianópolis/SC\nPhone: (48) 2109-5100 | Hours: Monday to Friday, 8 AM to 5 PM",
        },
    },
    "4": {
        "sigla": "CEAVI",
        "nome": "Centro de Educação Superior do Alto Vale do Itajaí",
        "cidade": "Ibirama - SC",
        "endereco": "Rua Dr. Getúlio Vargas, 2822 - Bela Vista, Ibirama/SC - CEP: 89140-000",
        "url": "https://www.udesc.br/ceavi",
        "tel": "(47) 3357-8484",
        "tem_residencia": False,
        "residencia_estrangeiro": False,
        "info_residencia": {
            "pt": "O CEAVI não possui residência estudantil. Consulte a tutoria para indicações de moradia: tutoria.ceavi@udesc.br",
            "en": "CEAVI does not have student housing. Ask the tutoring team for housing recommendations: tutoria.ceavi@udesc.br",
        },
        "tutoria_site": "https://www.udesc.br/ceavi/tutoria",
        "tutoria_email": "tutoria.ceavi@udesc.br",
        "tutoria_tel": "(47) 3357-8484",
        "tutoria_equipe": {
            "pt": ["Equipe de Tutoria CEAVI - consulte o site para informações atualizadas."],
            "en": ["CEAVI Tutoring Team - check the website for updated information."],
        },
        "receita_federal": {
            "pt": "Receita Federal - Blumenau (mais próxima)\nRua XV de Novembro, 420 - Centro, Blumenau/SC\nTel: (47) 2101-7500 | Horário: segunda a sexta, 8h às 17h",
            "en": "Federal Revenue Office (Receita Federal) - Blumenau (nearest)\nRua XV de Novembro, 420 - Centro, Blumenau/SC\nPhone: (47) 2101-7500 | Hours: Monday to Friday, 8 AM to 5 PM",
        },
    },
    "5": {
        "sigla": "CEFID",
        "nome": "Centro de Ciências da Saúde e do Esporte",
        "cidade": "Florianópolis - SC",
        "endereco": "Rua Pascoal Simone, 358 - Coqueiros, Florianópolis/SC - CEP: 88080-350",
        "url": "https://www.udesc.br/cefid",
        "tel": "(48) 3664-8600",
        "tem_residencia": False,
        "residencia_estrangeiro": False,
        "info_residencia": {
            "pt": "O CEFID não possui residência estudantil própria. O SOE pode indicar opções de moradia na cidade: soe@udesc.br",
            "en": "CEFID does not have its own student housing. The SOE can suggest housing options in the city: soe@udesc.br",
        },
        "tutoria_site": "https://www.udesc.br/cefid/tutoria",
        "tutoria_email": "tutoria.cefid@udesc.br",
        "tutoria_tel": "(48) 3664-8600",
        "tutoria_equipe": {
            "pt": ["Equipe de Tutoria CEFID - consulte o site para informações atualizadas."],
            "en": ["CEFID Tutoring Team - check the website for updated information."],
        },
        "receita_federal": {
            "pt": "Receita Federal - Florianópolis\nRua Vital Brasil, 91 - Estreito, Florianópolis/SC\nTel: (48) 2109-5100 | Horário: segunda a sexta, 8h às 17h",
            "en": "Federal Revenue Office (Receita Federal) - Florianópolis\nRua Vital Brasil, 91 - Estreito, Florianópolis/SC\nPhone: (48) 2109-5100 | Hours: Monday to Friday, 8 AM to 5 PM",
        },
    },
    "6": {
        "sigla": "CEO",
        "nome": "Centro de Educação Superior do Oeste",
        "cidade": "Chapecó - SC",
        "endereco": "Rua Beloni Trombeta Zanin, 680E - Bairro Santo Antônio, Chapecó/SC - CEP: 89815-015",
        "url": "https://www.udesc.br/ceo",
        "tel": "(49) 2049-9524",
        "tem_residencia": True,
        "residencia_estrangeiro": True,
        "info_residencia": {
            "pt": "O CEO dispõe de residência estudantil. Estudantes estrangeiros devem solicitar vaga com antecedência pelo email: intercambio.ceo@udesc.br | (49) 2049-9524",
            "en": "CEO has student housing available. International students should request a spot in advance by email: intercambio.ceo@udesc.br | (49) 2049-9524",
        },
        "tutoria_site": "https://www.udesc.br/ceo/tutoria",
        "tutoria_email": "tutoria.ceo@udesc.br",
        "tutoria_tel": "(49) 2049-9524",
        "tutoria_equipe": {
            "pt": ["Equipe de Tutoria CEO - consulte o site para informações atualizadas."],
            "en": ["CEO Tutoring Team - check the website for updated information."],
        },
        "receita_federal": {
            "pt": "Receita Federal - Chapecó\nRua Marechal Deodoro, 260 - Centro, Chapecó/SC\nTel: (49) 2101-8100 | Horário: segunda a sexta, 8h às 17h",
            "en": "Federal Revenue Office (Receita Federal) - Chapecó\nRua Marechal Deodoro, 260 - Centro, Chapecó/SC\nPhone: (49) 2101-8100 | Hours: Monday to Friday, 8 AM to 5 PM",
        },
    },
    "7": {
        "sigla": "CEPLAN",
        "nome": "Centro de Educação do Planalto Norte",
        "cidade": "São Bento do Sul - SC",
        "endereco": "Rua Luiz Fernando Hastreiter, 180 - Centenário, São Bento do Sul/SC - CEP: 89290-971",
        "url": "https://www.udesc.br/ceplan",
        "tel": "(47) 3647-0074",
        "tem_residencia": False,
        "residencia_estrangeiro": False,
        "info_residencia": {
            "pt": "O CEPLAN não possui residência estudantil própria. Consulte a tutoria para indicações: tutoria.ceplan@udesc.br",
            "en": "CEPLAN does not have its own student housing. Ask the tutoring team for recommendations: tutoria.ceplan@udesc.br",
        },
        "tutoria_site": "https://www.udesc.br/ceplan/tutoria",
        "tutoria_email": "tutoria.ceplan@udesc.br",
        "tutoria_tel": "(47) 3647-0074",
        "tutoria_equipe": {
            "pt": ["Equipe de Tutoria CEPLAN - consulte o site para informações atualizadas."],
            "en": ["CEPLAN Tutoring Team - check the website for updated information."],
        },
        "receita_federal": {
            "pt": "Receita Federal - São Bento do Sul\nRua Getúlio Vargas, 100 - Centro, São Bento do Sul/SC\nTel: (47) 3640-6600 | Horário: segunda a sexta, 8h às 17h",
            "en": "Federal Revenue Office (Receita Federal) - São Bento do Sul\nRua Getúlio Vargas, 100 - Centro, São Bento do Sul/SC\nPhone: (47) 3640-6600 | Hours: Monday to Friday, 8 AM to 5 PM",
        },
    },
    "8": {
        "sigla": "CERES",
        "nome": "Centro de Educação Superior da Região Sul",
        "cidade": "Laguna - SC",
        "endereco": "Rua Cel. Fernandes Martins, 270 - Progresso, Laguna/SC - CEP: 88790-971",
        "url": "https://www.udesc.br/ceres",
        "tel": "(48) 3647-7900",
        "tem_residencia": False,
        "residencia_estrangeiro": False,
        "info_residencia": {
            "pt": "O CERES não possui residência estudantil própria. Entre em contato com a coordenação para indicações de moradia: tutoria.ceres@udesc.br",
            "en": "CERES does not have its own student housing. Contact the coordination office for housing recommendations: tutoria.ceres@udesc.br",
        },
        "tutoria_site": "https://www.udesc.br/ceres/tutoria",
        "tutoria_email": "tutoria.ceres@udesc.br",
        "tutoria_tel": "(48) 3647-7900",
        "tutoria_equipe": {
            "pt": ["Equipe de Tutoria CERES - consulte o site para informações atualizadas."],
            "en": ["CERES Tutoring Team - check the website for updated information."],
        },
        "receita_federal": {
            "pt": "Receita Federal - Tubarão (mais próxima)\nRua Lauro Müller, 180 - Centro, Tubarão/SC\nTel: (48) 3626-0800 | Horário: segunda a sexta, 8h às 17h",
            "en": "Federal Revenue Office (Receita Federal) - Tubarão (nearest)\nRua Lauro Müller, 180 - Centro, Tubarão/SC\nPhone: (48) 3626-0800 | Hours: Monday to Friday, 8 AM to 5 PM",
        },
    },
    "9": {
        "sigla": "CESFI",
        "nome": "Centro de Educação Superior da Foz do Itajaí",
        "cidade": "Balneário Camboriú - SC",
        "endereco": "Av. Lourival Cesario Pereira, s/n - Ed. Alcides Abreu, Nova Esperança, Balneário Camboriú/SC - CEP: 88330-630",
        "url": "https://www.udesc.br/cesfi",
        "tel": "(47) 3398-6484",
        "tem_residencia": False,
        "residencia_estrangeiro": False,
        "info_residencia": {
            "pt": "O CESFI não possui residência estudantil própria. O SOE pode indicar opções de moradia na região: soe@udesc.br",
            "en": "CESFI does not have its own student housing. The SOE can suggest housing options in the region: soe@udesc.br",
        },
        "tutoria_site": "https://www.udesc.br/cesfi/tutoria",
        "tutoria_email": "tutoria.cesfi@udesc.br",
        "tutoria_tel": "(47) 3398-6484",
        "tutoria_equipe": {
            "pt": ["Equipe de Tutoria CESFI - consulte o site para informações atualizadas."],
            "en": ["CESFI Tutoring Team - check the website for updated information."],
        },
        "receita_federal": {
            "pt": "Receita Federal - Blumenau (mais próxima)\nRua XV de Novembro, 420 - Centro, Blumenau/SC\nTel: (47) 2101-7500 | Horário: segunda a sexta, 8h às 17h",
            "en": "Federal Revenue Office (Receita Federal) - Blumenau (nearest)\nRua XV de Novembro, 420 - Centro, Blumenau/SC\nPhone: (47) 2101-7500 | Hours: Monday to Friday, 8 AM to 5 PM",
        },
    },
    "10": {
        "sigla": "CESMO",
        "nome": "Centro de Educação Superior do Meio Oeste",
        "cidade": "Caçador - SC",
        "endereco": "Rua Carlos Coelho de Souza, 120 - Bairro DER, Caçador/SC - CEP: 89500-000",
        "url": "https://www.udesc.br/cesmo",
        "tel": "(48) 3664-8000",
        "tem_residencia": False,
        "residencia_estrangeiro": False,
        "info_residencia": {
            "pt": "O CESMO não possui residência estudantil própria. Consulte a tutoria para indicações: tutoria.cesmo@udesc.br",
            "en": "CESMO does not have its own student housing. Ask the tutoring team for recommendations: tutoria.cesmo@udesc.br",
        },
        "tutoria_site": "https://www.udesc.br/cesmo/tutoria",
        "tutoria_email": "tutoria.cesmo@udesc.br",
        "tutoria_tel": "(48) 3664-8000",
        "tutoria_equipe": {
            "pt": ["Equipe de Tutoria CESMO - consulte o site para informações atualizadas."],
            "en": ["CESMO Tutoring Team - check the website for updated information."],
        },
        "receita_federal": {
            "pt": "Receita Federal - Videira (mais próxima)\nRua Getúlio Vargas, 1000 - Centro, Videira/SC\nTel: (49) 3566-7700 | Horário: segunda a sexta, 8h às 17h",
            "en": "Federal Revenue Office (Receita Federal) - Videira (nearest)\nRua Getúlio Vargas, 1000 - Centro, Videira/SC\nPhone: (49) 3566-7700 | Hours: Monday to Friday, 8 AM to 5 PM",
        },
    },
    "11": {
        "sigla": "CCT",
        "nome": "Centro de Ciências Tecnológicas",
        "cidade": "Joinville - SC",
        "endereco": "Rua Paulo Malschitzki, 200 - Zona Industrial Norte, Joinville/SC - CEP: 89219-710",
        "url": "https://www.udesc.br/cct",
        "tel": "(47) 3481-7900",
        "tem_residencia": True,
        "residencia_estrangeiro": True,
        "info_residencia": {
            "pt": "O CCT possui residência estudantil disponível para estudantes estrangeiros em intercâmbio. Entre em contato com a coordenação de intercâmbio para verificar vagas disponíveis: intercambio.cct@udesc.br | (47) 3481-7900",
            "en": "CCT has student housing available for international exchange students. Contact the exchange coordination office to check for available spots: intercambio.cct@udesc.br | (47) 3481-7900",
        },
        "tutoria_site": "https://www.udesc.br/cct/tutoriaacademica",
        "tutoria_email": "tutoria.cct@udesc.br",
        "tutoria_tel": "(47) 3481-7900",
        "tutoria_equipe": {
            "pt": [
                "Supervisora TADS: Profa. Débora Cabral Nazário",
                "Supervisora Ciência da Computação: Profa. Luciana Rita Guedes",
            ],
            "en": [
                "TADS Supervisor: Prof. Débora Cabral Nazário",
                "Computer Science Supervisor: Prof. Luciana Rita Guedes",
            ],
        },
        "receita_federal": {
            "pt": "Receita Federal - Joinville\nRua Ministro Calógeras, 127 - Centro, Joinville/SC\nTel: (47) 2101-5900 | Horário: segunda a sexta, 8h às 17h",
            "en": "Federal Revenue Office (Receita Federal) - Joinville\nRua Ministro Calógeras, 127 - Centro, Joinville/SC\nPhone: (47) 2101-5900 | Hours: Monday to Friday, 8 AM to 5 PM",
        },
    },
    "12": {
        "sigla": "ESAG",
        "nome": "Centro de Ciências da Administração e Socioeconômicas",
        "cidade": "Florianópolis - SC",
        "endereco": "Av. Madre Benvenuta, 2007 - Itacorubi, Florianópolis/SC - CEP: 88035-901",
        "url": "https://www.udesc.br/esag",
        "tel": "(48) 3664-8200",
        "tem_residencia": False,
        "residencia_estrangeiro": False,
        "info_residencia": {
            "pt": "O ESAG não possui residência estudantil própria. O SOE pode indicar opções de moradia na cidade: soe@udesc.br",
            "en": "ESAG does not have its own student housing. The SOE can suggest housing options in the city: soe@udesc.br",
        },
        "tutoria_site": "https://www.udesc.br/esag/tutoria",
        "tutoria_email": "tutoria.esag@udesc.br",
        "tutoria_tel": "(48) 3664-8200",
        "tutoria_equipe": {
            "pt": ["Equipe de Tutoria ESAG - consulte o site para informações atualizadas."],
            "en": ["ESAG Tutoring Team - check the website for updated information."],
        },
        "receita_federal": {
            "pt": "Receita Federal - Florianópolis\nRua Vital Brasil, 91 - Estreito, Florianópolis/SC\nTel: (48) 2109-5100 | Horário: segunda a sexta, 8h às 17h",
            "en": "Federal Revenue Office (Receita Federal) - Florianópolis\nRua Vital Brasil, 91 - Estreito, Florianópolis/SC\nPhone: (48) 2109-5100 | Hours: Monday to Friday, 8 AM to 5 PM",
        },
    },
    "13": {
        "sigla": "FAED",
        "nome": "Centro de Ciências Humanas e da Educação",
        "cidade": "Florianópolis - SC",
        "endereco": "Av. Madre Benvenuta, 2007 - Itacorubi, Florianópolis/SC - CEP: 88035-901",
        "url": "https://www.udesc.br/faed",
        "tel": "(48) 3664-8500",
        "tem_residencia": False,
        "residencia_estrangeiro": False,
        "info_residencia": {
            "pt": "O FAED não possui residência estudantil própria. O SOE pode indicar opções de moradia na cidade: soe@udesc.br",
            "en": "FAED does not have its own student housing. The SOE can suggest housing options in the city: soe@udesc.br",
        },
        "tutoria_site": "https://www.udesc.br/faed/tutoria",
        "tutoria_email": "tutoria.faed@udesc.br",
        "tutoria_tel": "(48) 3664-8500",
        "tutoria_equipe": {
            "pt": ["Equipe de Tutoria FAED - consulte o site para informações atualizadas."],
            "en": ["FAED Tutoring Team - check the website for updated information."],
        },
        "receita_federal": {
            "pt": "Receita Federal - Florianópolis\nRua Vital Brasil, 91 - Estreito, Florianópolis/SC\nTel: (48) 2109-5100 | Horário: segunda a sexta, 8h às 17h",
            "en": "Federal Revenue Office (Receita Federal) - Florianópolis\nRua Vital Brasil, 91 - Estreito, Florianópolis/SC\nPhone: (48) 2109-5100 | Hours: Monday to Friday, 8 AM to 5 PM",
        },
    },
}

SISTEMAS = {
    "1": {
        "nome": "SIGA",
        "descricao": "Sistema Integrado de Gestão Acadêmica",
        "url": "https://www.siga.udesc.br",
        "info": {
            "pt": ("O SIGA é o sistema de gestão acadêmica da UDESC.\nNele você pode consultar:\n - Notas e histórico escolar\n - Faltas e frequência por disciplina\n - Grade horária\n - Requerimentos e solicitações acadêmicas\n\n*Requisitos de acesso:*\n - ID UDESC (login institucional)\n - Senha criada no primeiro acesso\n - Acesso via: https://www.siga.udesc.br\n\nEm caso de problemas de acesso, contate o suporte de TI do seu centro."),
            "en": ("SIGA is UDESC's academic management system.\nIn it you can check:\n - Grades and academic transcript\n - Absences and attendance per course\n - Class schedule\n - Academic requests and applications\n\n*Access requirements:*\n - UDESC ID (institutional login)\n - Password created on first access\n - Access at: https://www.siga.udesc.br\n\nIf you have access issues, contact your campus IT support."),
        },
    },
    "2": {
        "nome": "Moodle",
        "descricao": "Ambiente Virtual de Aprendizagem",
        "url": "https://moodle.udesc.br",
        "info": {
            "pt": ("O Moodle é a plataforma de ensino a distância da UDESC.\nCom ele você pode:\n - Acessar o material das disciplinas\n - Entregar exercícios e trabalhos\n - Participar de fóruns de discussão\n - Fazer provas online\n - Ver feedbacks dos professores\n\n*Requisitos de acesso:*\n - ID UDESC (login institucional)\n - Acesso via: https://moodle.udesc.br\n\nOs professores inscrevem os alunos nas disciplinas no início do semestre."),
            "en": ("Moodle is UDESC's distance-learning platform.\nWith it you can:\n - Access course materials\n - Submit assignments and exercises\n - Participate in discussion forums\n - Take online exams\n - View feedback from professors\n\n*Access requirements:*\n - UDESC ID (institutional login)\n - Access at: https://moodle.udesc.br\n\nProfessors enroll students in courses at the start of the semester."),
        },
    },
    "3": {
        "nome": "SIGAA",
        "descricao": "Sistema Integrado de Gestão de Atividades Acadêmicas",
        "url": "https://sigaa.udesc.br",
        "info": {
            "pt": ("O SIGAA é utilizado em alguns centros da UDESC.\nFuncionalidades principais:\n - Matrícula em disciplinas\n - Consulta de turmas e horários\n - Histórico acadêmico\n - Declarações e documentos\n\n*Requisitos de acesso:*\n - ID UDESC (login institucional)\n - Acesso via: https://sigaa.udesc.br\n\nVerifique com seu centro se o SIGAA está ativo para o seu curso."),
            "en": ("SIGAA is used at some UDESC campuses.\nMain features:\n - Course enrollment\n - Class and schedule lookup\n - Academic transcript\n - Certificates and documents\n\n*Access requirements:*\n - UDESC ID (institutional login)\n - Access at: https://sigaa.udesc.br\n\nCheck with your campus whether SIGAA is active for your program."),
        },
    },
}

SISTEMAS_UDESC = {
    "1": {
        "nome": "SIGA",
        "info": {
            "pt": ("*SIGA - Notas e Faltas*\n\nO SIGA permite acompanhar:\n - Suas notas por disciplina e avaliação\n - Percentual de faltas (limite: 25% por disciplina)\n - Situação acadêmica (aprovado/reprovado)\n - Histórico de todos os semestres\n\nAcesso: https://www.siga.udesc.br\nLogin: ID UDESC + senha"),
            "en": ("*SIGA - Grades and Attendance*\n\nSIGA lets you track:\n - Your grades by course and assessment\n - Absence percentage (limit: 25% per course)\n - Academic status (passed/failed)\n - Transcript for all semesters\n\nAccess: https://www.siga.udesc.br\nLogin: UDESC ID + password"),
        },
    },
    "2": {
        "nome": "Moodle",
        "info": {
            "pt": ("*Moodle - Disciplinas e Exercícios*\n\nO Moodle é onde acontece o ensino online:\n - Material de aula (slides, PDFs, vídeos)\n - Entrega de trabalhos com prazo\n - Fóruns e discussões com professores\n - Quizzes e provas online\n - Comunicados das disciplinas\n\nAcesso: https://moodle.udesc.br\nLogin: ID UDESC + senha"),
            "en": ("*Moodle - Courses and Assignments*\n\nMoodle is where online learning happens:\n - Class materials (slides, PDFs, videos)\n - Assignment submissions with deadlines\n - Forums and discussions with professors\n - Online quizzes and exams\n - Course announcements\n\nAccess: https://moodle.udesc.br\nLogin: UDESC ID + password"),
        },
    },
    "3": {
        "nome": "Site UDESC",
        "info": {
            "pt": ("*Site UDESC - Informações Acadêmicas*\n\nNo site oficial você encontra:\n - PPC (Plano Pedagógico do Curso) - grade curricular completa\n - Lista de professores e contatos\n - Calendário acadêmico\n - Editais e notícias institucionais\n - Informações sobre intercâmbio\n\nSite principal: https://www.udesc.br\nBusque seu centro específico no site para mais informações"),
            "en": ("*UDESC Website - Academic Information*\n\nOn the official website you'll find:\n - PPC (Course Pedagogical Plan) - full curriculum\n - List of professors and contacts\n - Academic calendar\n - Notices and institutional news\n - Information about exchange programs\n\nMain site: https://www.udesc.br\nSearch for your specific campus on the site for more information"),
        },
    },
    "4": {
        "nome": "SAS",
        "info": {
            "pt": ("*SAS - Agendamento de Salas*\n\nO Sistema de Agendamento de Salas (SAS) permite:\n - Verificar disponibilidade de salas e laboratórios\n - Agendar espaços para estudo em grupo\n - Consultar agendamentos existentes\n\nAcesso: https://sas.udesc.br\nLogin: ID UDESC + senha\n\nAtenção: Disponibilidade de salas varia por centro."),
            "en": ("*SAS - Room Booking*\n\nThe Room Booking System (SAS) lets you:\n - Check room and lab availability\n - Book spaces for group study\n - View existing bookings\n\nAccess: https://sas.udesc.br\nLogin: UDESC ID + password\n\nNote: room availability varies by campus."),
        },
    },
    "5": {
        "nome": "Office 365",
        "info": {
            "pt": ("*Office 365 - E-mail e Aplicativos Microsoft*\n\nCom sua conta institucional UDESC você tem acesso gratuito a:\n - E-mail institucional (@edu.udesc.br)\n - Word, Excel, PowerPoint online\n - OneDrive (armazenamento em nuvem)\n - Teams (videoconferências)\n - OneNote e outros apps Microsoft\n\n*Como acessar:*\n 1. Acesse portal.office.com\n 2. Login: ID_UDESC@edu.udesc.br\n 3. Use a senha do seu ID UDESC\n\nPortal: https://portal.office.com"),
            "en": ("*Office 365 - Email and Microsoft Apps*\n\nWith your UDESC institutional account you get free access to:\n - Institutional email (@edu.udesc.br)\n - Word, Excel, PowerPoint online\n - OneDrive (cloud storage)\n - Teams (video conferencing)\n - OneNote and other Microsoft apps\n\n*How to access:*\n 1. Go to portal.office.com\n 2. Login: UDESC_ID@edu.udesc.br\n 3. Use your UDESC ID password\n\nPortal: https://portal.office.com"),
        },
    },
    "6": {
        "nome": "Biblioteca Online",
        "info": {
            "pt": ("*Biblioteca Online UDESC*\n\nA biblioteca online oferece:\n - Busca de livros físicos e digitais\n - Repositório de TCCs de todos os cursos\n - Dissertações e teses de mestrado/doutorado\n - Bases de dados científicas (CAPES, SciELO)\n - Renovação e reserva de livros\n\nAcesso: https://www.udesc.br/bibliotecas\nRepositório: https://repositorio.udesc.br\nLogin: ID UDESC + senha"),
            "en": ("*UDESC Online Library*\n\nThe online library offers:\n - Search for physical and digital books\n - Repository of undergraduate theses from all programs\n - Master's and doctoral dissertations and theses\n - Scientific databases (CAPES, SciELO)\n - Book renewal and reservation\n\nAccess: https://www.udesc.br/bibliotecas\nRepository: https://repositorio.udesc.br\nLogin: UDESC ID + password"),
        },
    },
}

SOE_INFO = {
    "pt": ("*Serviço de Orientação ao Estudante (SOE)*\n\nO SOE oferece apoio ao estudante estrangeiro em diversas áreas:\n\n*Serviços disponíveis:*\n - Orientação psicológica e emocional\n - Apoio pedagógico e acadêmico\n - Orientação sobre adaptação cultural\n - Mediação de conflitos\n - Encaminhamento para serviços de saúde\n - Apoio para alunos com necessidades especiais\n\n*Horário de atendimento:*\n  Segunda a sexta: 8h às 12h e 13h às 17h\n\n*Contato:*\n  Site: https://www.udesc.br/soe\n  E-mail: soe@udesc.br\n\nO atendimento é gratuito e confidencial."),
    "en": ("*Student Guidance Service (SOE)*\n\nSOE offers support to international students in several areas:\n\n*Available services:*\n - Psychological and emotional guidance\n - Academic and pedagogical support\n - Guidance on cultural adaptation\n - Conflict mediation\n - Referral to health services\n - Support for students with special needs\n\n*Office hours:*\n  Monday to Friday: 8 AM-12 PM and 1 PM-5 PM\n\n*Contact:*\n  Website: https://www.udesc.br/soe\n  Email: soe@udesc.br\n\nAssistance is free and confidential."),
}

ID_UDESC_INFO = {
    "pt": ("*Como obter o ID UDESC*\n\nO ID UDESC é seu login institucional para acessar todos os sistemas da universidade.\n\n*Passo a passo:*\n\n1- Acesse o portal: https://id.udesc.br\n\n2- Clique em *'Primeiro acesso'* ou *'Ativar conta'*\n\n3- Informe seu CPF e data de nascimento\n\n4- Confirme seus dados cadastrais\n\n5- Crie uma senha segura (mínimo 8 caracteres, letras e números)\n\n6- Pronto! Use o ID para acessar SIGA, Moodle, Office 365 e demais sistemas.\n\n*Importante:*\n - Você precisa de um CPF brasileiro ativo para ativar o ID UDESC\n - Em caso de problemas, contate o suporte de TI do seu centro\n - Guarde bem sua senha - ela é pessoal e intransferível\n\nSuporte TI: Entre em contato com seu centro UDESC"),
    "en": ("*How to get your UDESC ID*\n\nYour UDESC ID is the institutional login used to access all university systems.\n\n*Step by step:*\n\n1- Go to the portal: https://id.udesc.br\n\n2- Click *'First access'* or *'Activate account'*\n\n3- Enter your CPF and date of birth\n\n4- Confirm your registration data\n\n5- Create a secure password (minimum 8 characters, letters and numbers)\n\n6- Done! Use your ID to access SIGA, Moodle, Office 365 and other systems.\n\n*Important:*\n - You need an active Brazilian CPF to activate your UDESC ID\n - If you run into problems, contact your campus IT support\n - Keep your password safe - it is personal and non-transferable\n\nIT Support: Contact your UDESC campus for assistance"),
}

CPF_INFO = {
    "pt": ("*CPF para Estudantes Estrangeiros*\n\nO CPF (Cadastro de Pessoa Física) é essencial para:\n - Ativar o ID UDESC\n - Abrir conta bancária\n - Alugar moradia\n - Acesso a serviços no Brasil\n\n*Passo 1 - Solicitar CPF online:*\n 1. Acesse: https://servicos.receita.fazenda.gov.br/servicos/cpf/inscricao/\n 2. Selecione *'Estrangeiro residente no exterior'*\n 3. Preencha o formulário com seus dados pessoais\n 4. Anote o número de protocolo gerado\n\n*Passo 2 - Validar presencialmente na Receita Federal:*\n  Atenção: Estrangeiros DEVEM comparecer pessoalmente à Receita Federal para validar o CPF!\n\n  *Documentos necessários:*\n   - Passaporte original\n   - Visto de estudante vigente\n   - Comprovante de matrícula na UDESC\n   - Número de protocolo da solicitação online\n\nEscolha seu centro no Menu 1 para ver o endereço da Receita Federal mais próxima."),
    "en": ("*CPF for International Students*\n\nThe CPF (Individual Taxpayer Registration) is essential for:\n - Activating your UDESC ID\n - Opening a bank account\n - Renting housing\n - Accessing services in Brazil\n\n*Step 1 - Apply for your CPF online:*\n 1. Go to: https://servicos.receita.fazenda.gov.br/servicos/cpf/inscricao/\n 2. Select *'Foreigner residing abroad'*\n 3. Fill out the form with your personal information\n 4. Write down the protocol number generated\n\n*Step 2 - Validate in person at the Federal Revenue Office:*\n  Attention: foreigners MUST appear in person at the Federal Revenue Office (Receita Federal) to validate the CPF!\n\n  *Required documents:*\n   - Original passport\n   - Valid student visa\n   - UDESC enrollment certificate\n   - Online application protocol number\n\nChoose your campus in Menu 1 to see the nearest Federal Revenue Office address."),
}
