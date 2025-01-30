SOMAR = "SOMAR"
SUBTRAIR = "SUBTRAIR"

menu = """\nMenu de Opções:
            1 - Cadastrar evento
            2 - Cadastrar aluno
            3 - Inscrever aluno
            4 - Listar eventos cadastrados
            5 - Listar alunos cadastrados
            6 - Resumo participação
            7 - Sair\n"""

# Dicionários
evento = {}  # keys: titulo, capacidade, vagas_restantes
aluno = {}  # keys: nome, curso, instituição
inscricao = {}  # keys: evento_nome, aluno_nome

# Listas de dicionários
eventos_cadastrados = []  # manipula evento
alunos_cadastrados = []  # manipula aluno
inscricoes_cadastradas = []  # manipula inscrição de alunos em eventos já cadastrados


def exibir_menu():
    print(menu)


def exibir_eventos_cadastrados():
    for evento in eventos_cadastrados:
        print(evento)


def exibir_alunos_cadastrados():
    for aluno in alunos_cadastrados:
        print(aluno)


def exibir_inscricoes_efetuadas():
    for inscricao in inscricoes_cadastradas:
        print(inscricao)


def cadastrar_evento():
    titulo = input('\nDIGITE O NOME DO EVENTO: ').title().strip()
    capacidade = input('DIGITE A CAPACIDADE MÁXIMA DO EVENTO: ').strip()

    evento = {
        'titulo_evento': titulo,
        'capacidade': capacidade,
        'vagas_restantes': capacidade
    }

    eventos_cadastrados.append(evento)


def cadastrar_aluno():
    nome = input('\nDIGITE O NOME DO ALUNO: ').strip()
    curso = input('DIGITE O CURSO DO ALUNO: ').strip()
    instituicao = input('DIGITE A INSTITUIÇÃO EM QUE O ALUNO ESTUDA: ').strip()

    aluno = {
        'nome_aluno': nome,
        'curso': curso,
        'instituicao': instituicao
    }

    alunos_cadastrados.append(aluno)


def inscrever_aluno_curso():
    nomeEvento = input('\nDIGITE O NOME DO EVENTO EM QUE O ALUNO QUER SE INSCREVER: ').strip()
    nomeAluno = input('DIGITE O NOME DO ALUNO: ').strip()

    inscricao = {
        'evento_nome': nomeEvento,
        'aluno_nome': nomeAluno
    }

    inscricoes_cadastradas.append(inscricao)
    print(atualizar_vagas(nomeEvento, SUBTRAIR))


def atualizar_vagas(nomeEvento, tipoAtualizacao):
    msg = ''

    if eventos_cadastrados:
        for evento in eventos_cadastrados:
            if evento.get('titulo_evento').upper() == nomeEvento.upper():
                if tipoAtualizacao == SOMAR:
                    atualizar = int(evento.get('vagas_restantes')) + 1
                else:
                    atualizar = int(evento.get('vagas_restantes')) - 1

                if atualizar >= 0:
                    evento.update({'vagas_restantes': atualizar})
                    msg = f'O evento "{evento["titulo_evento"]}" foi atualizado com sucesso!'
                else:
                    msg = 'Não há mais vagas disponíveis neste curso.'
                break
        else:
            msg = 'Evento não encontrado.'
    else:
        msg = 'Não existem eventos cadastrados.'

    return msg


def executar_menu():
    while True:
        exibir_menu()

        opcaoDigitada = input("DIGITE UMA OPÇÃO VÁLIDA DO MENU: ")

        if opcaoDigitada == "1":
            cadastrar_evento()

        elif opcaoDigitada == "2":
            cadastrar_aluno()

        elif opcaoDigitada == "3":
            inscrever_aluno_curso()

        elif opcaoDigitada == "4":
            exibir_eventos_cadastrados()

        elif opcaoDigitada == "5":
            exibir_alunos_cadastrados()

        elif opcaoDigitada == "6":
            exibir_inscricoes_efetuadas()

        elif opcaoDigitada == "7":
            break

        else:
            print(f"{opcaoDigitada} - OPÇÃO INVÁLIDA DE MENU.")


executar_menu()