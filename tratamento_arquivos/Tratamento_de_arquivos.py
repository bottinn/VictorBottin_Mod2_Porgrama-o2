'''RECUPERAÇÃO PROGRAMAÇÃO II
Essa atividade avaliativa de recuperação poderá ser feita de forma individual ou em dupla, desde que seja a 
mesma dupla que fez a avaliação 02. O Visual Studio Code deverá ser utilizado para implementar as funcionalidades, 
usando a linguagem de programação Python. Um arquivo, com as questões resolvidas, deverá ser postado no Sigaa.
Nome do arquivo: "nome_sobrenome_prog2_recuperacao.py".
Desenvolva um sistema simples que gerencie a participação dos alunos e eventos durante a SNCT 2024, câmpus Chapecó. O programa deverá:
- Permitir que o usuário cadastre e exclua eventos com título e capacidade máxima de participantes;
- Permitir que o usuário cadastre e exclua alunos interessados em participar dos eventos;
- Exibir, na tela, a lista de eventos e as vagas restantes para cada um.
- Permitir que o usuário selecione um evento para inscrever alunos, respeitando o limite de vagas.
- Exibir um resumo final da SNCT, mostrando quantos alunos participaram de cada evento;
- O programa deve rodar em um laço de repetição que exiba "Opções de Menu" referentes às funcionalidades 
mencionadas acima. Para finalizar o programa, o usuário deverá digitar "Sair".
- Para implementar tais funcionalidades, utilize funções que: cadastre eventos com título e capacidade de 
participantes; exclui eventos previamente cadastrados;cadastre alunos interessados em participar do evento; 
exclui alunos inscritos em eventos e atualize a capacidade de participantes do evento;
exibe na tela os eventos cadastrados e as vagas disponíveis;
exibe o resumo da participação de alunos por evento; exibe o menu de opções.
Implemente as funcionalidades mencionadas acima usando estruturas de dados, do tipo: tupla, lista e dicionário.
Façam validações relevantes, por exemplo: não permita que um aluno seja inscrito em um evento que não foi 
cadastrado; não inscreva mais alunos que a capacidade máxima do evento; não permita que uma opção inválida de 
menu seja aceita, etc... Fiquem atentos a necessidade de uso de estruturas condicionais ou de decisão, estruturas 
de repetição, e outras questões conceituais estudadas em sala de aula referentes a linguagem de programação 
Python. Está liberado o uso da criatividade e diferentes formas de implementação serão aceitas. (10,0)'''
''''''
import os

ARQUIVO_EVENTO = "evento.txt"
ARQUIVO_ALUNO = "aluno.txt"
ARQUIVO_INSCRITOS = "inscricoes.txt"

SOMAR = "SOMAR"
SUBTRAIR = "SUBTRAIR"

menu = """\nMenu de Opções:
            1- Cadastrar evento
            2- Cadastrar aluno
            3- Inscrever aluno
            4- Listar eventos cadastrados
            5- Listar alunos cadastrados
            6- Resumo participação
            7 - Sair\n"""

# Listas de dicionários
eventos_cadastrados = []  # manipula evento
alunos_cadastrados = []  # manipula aluno
inscricoes_cadastradas = []  # manipula inscrição de alunos em eventos já cadastrados

def validarString(entrada):
    if not entrada or not entrada.isalpha():
        return False
    return True

def exibir_menu():
    print(menu)


def arquivo_existe(nome_arquivo):
    return os.path.exists(nome_arquivo)


def cadastrar_evento():
    titulo = input('\nDIGITE O NOME DO EVENTO: ').title().strip()
    capacidade = input('DIGITE A CAPACIDADE MÁXIMA DO EVENTO: ').strip()

    # Cria um evento novo que é armazenado em uma variável do tipo "dicionário"
    evento = {
        'titulo_evento': titulo,
        'capacidade': int(capacidade),
        'vagas_restantes': int(capacidade)
    }

    # Armazena, na lista de dicionários, o evento novo criado
    eventos_cadastrados.append(evento)

    # Salva o evento no arquivo
    with open(ARQUIVO_EVENTO, "a") as fevento:
        fevento.write(f"{titulo},{capacidade},{capacidade}\n")


def cadastrar_aluno():
    nome = input('\nDIGITE O NOME DO ALUNO: ').strip()
    curso = input('DIGITE O CURSO DO ALUNO: ').strip()
    instituicao = input('DIGITE A INSTITUIÇÃO EM QUE O ALUNO ESTUDA: ').strip()

    # Cria um aluno novo que é armazenado em uma variável do tipo "dicionário"
    aluno = {
        'nome_aluno': nome,
        'curso': curso,
        'instituicao': instituicao
    }

    # Armazena, na lista de dicionários, o aluno novo criado
    alunos_cadastrados.append(aluno)

    # Salva o aluno no arquivo
    with open(ARQUIVO_ALUNO, "a") as faluno:
        faluno.write(f"{nome},{curso},{instituicao}\n")


def inscrever_aluno_curso():
    nomeEvento = input('\nDIGITE O NOME DO EVENTO EM QUE O ALUNO QUER SE INSCREVER: ').strip()
    nomeAluno = input('DIGITE O NOME DO ALUNO: ').strip()

    # Verifica se o evento existe
    evento_encontrado = next((evento for evento in eventos_cadastrados if evento['titulo_evento'].upper() == nomeEvento.upper()), None)
    if not evento_encontrado:
        print("Evento não encontrado.")
        return

    # Verifica se o aluno existe
    aluno_encontrado = next((aluno for aluno in alunos_cadastrados if aluno['nome_aluno'].upper() == nomeAluno.upper()), None)
    if not aluno_encontrado:
        print("Aluno não encontrado.")
        return

    # Cria uma inscrição nova que é armazenada em uma variável do tipo "dicionário"
    inscricao = {
        'evento_nome': nomeEvento,
        'aluno_nome': nomeAluno
    }

    # Armazena, na lista de dicionários, a inscrição nova criada
    inscricoes_cadastradas.append(inscricao)

    # Atualiza o número de vagas restantes no evento
    atualizar_vagas(nomeEvento, SUBTRAIR)


def atualizar_vagas(nomeEvento, tipoAtualizacao):
    for evento in eventos_cadastrados:
        if evento['titulo_evento'].upper() == nomeEvento.upper():
            if tipoAtualizacao == SOMAR:
                evento['vagas_restantes'] += 1
            else:
                if evento['vagas_restantes'] > 0:
                    evento['vagas_restantes'] -= 1
                else:
                    print("Não há mais vagas disponíveis neste evento.")
                    return
            print(f"O evento {evento['titulo_evento']} foi atualizado com sucesso!")
            return
    print("Evento não encontrado.")

def exibir_eventos_cadastrados():
    if eventos_cadastrados:
        print("\nEventos Cadastrados:")
        for evento in eventos_cadastrados:
            print(f"Nome: {evento['titulo_evento']}, Capacidade: {evento['capacidade']}, Vagas Restantes: {evento['vagas_restantes']}")
    else:
        print("Nenhum evento cadastrado.")


def exibir_alunos_cadastrados():
    if alunos_cadastrados:
        print("\nAlunos Cadastrados:")
        for aluno in alunos_cadastrados:
            print(f"Nome: {aluno['nome_aluno']}, Curso: {aluno['curso']}, Instituição: {aluno['instituicao']}")
    else:
        print("Nenhum aluno cadastrado.")


def exibir_inscricoes_efetuadas():
    if inscricoes_cadastradas:
        print("\nInscrições Efetuadas:")
        for inscricao in inscricoes_cadastradas:
            print(f"Evento: {inscricao['evento_nome']}, Aluno: {inscricao['aluno_nome']}")
    else:
        print("Nenhuma inscrição efetuada.")


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
            print("Programa encerrado!")        
            break
        else:
            print(f"{opcaoDigitada} - OPÇÃO INVÁLIDA DE MENU.")


executar_menu()
