def exibirMenu():

    menu = (

        "--- Menu de Opções ---\n"

        "1. Cadastrar Evento\n"

        "2. Remover Evento\n"

        "3. Cadastrar Aluno\n"

        "4. Remover Aluno\n"

        "5. Mostrar Eventos e Vagas\n"

        "6. Exibir Resumo da SNCT\n"

        "7. Editar Evento ou Aluno\n"

        "Digite 'sair' para encerrar o programa.\n"

    )

    return menu



def validarString(entrada):

    if not entrada or not entrada.isalpha():

        return False

    return True



def CadastrarEvento(eventosSNCT):

    TituloEvento = input("Insira o título do evento: ").strip()

    if not validarString(TituloEvento):

        return "ERRO: O título do evento deve conter apenas letras e não pode estar vazio."

    if TituloEvento in eventosSNCT:

        return "ERRO: Evento já cadastrado."

    try:

        CapacidadeEvento = int(input("Insira a capacidade máxima do evento: "))

        if CapacidadeEvento <= 0:

            return "ERRO: A capacidade do evento deve ser maior do que zero."

        eventosSNCT[TituloEvento] = {"capacidade": CapacidadeEvento, "inscritos": []}

        return f"Evento '{TituloEvento}' cadastrado com sucesso!"

    except ValueError:

        return "ERRO: A capacidade do evento deve ser um número inteiro."



def ExcluirEvento(eventos):

    TituloEvento = input("Insira o título do evento a ser excluído: ").strip()

    if TituloEvento in eventos:

        del eventos[TituloEvento]

        return f"Evento '{TituloEvento}' excluído com sucesso."

    return "ERRO: Evento não encontrado."



def CadastrarAluno(alunos, eventos):

    NomeAluno = input("Insira o nome do aluno: ").strip()

    if not validarString(NomeAluno):

        return "ERRO: O nome do aluno deve conter apenas letras e não pode estar vazio."

    if NomeAluno in alunos:

        return "ERRO: Aluno já cadastrado."

    alunos.append(NomeAluno)

    if not eventos:

        alunos.remove(NomeAluno)

        return "Nenhum evento cadastrado. O aluno não pode ser inscrito."

    EventoSelecionado = SelecionarEvento(eventos)

    if EventoSelecionado:

        return InscreverAlunoNoEvento(NomeAluno, EventoSelecionado)

    alunos.remove(NomeAluno)

    return "Aluno removido por falta de inscrição em evento."



def SelecionarEvento(eventos):

    lista_eventos = []

    for titulo, dados in eventos.items():

        VagasRestantes = dados["capacidade"] - len(dados["inscritos"])

        lista_eventos.append(f"Evento: {titulo} | Vagas Restantes: {VagasRestantes}")

    return lista_eventos



def InscreverAlunoNoEvento(NomeAluno, evento):

    if len(evento["inscritos"]) >= evento["capacidade"]:

        return "ERRO: O evento já atingiu a capacidade máxima."

    evento["inscritos"].append(NomeAluno)

    return f"Aluno '{NomeAluno}' inscrito com sucesso!"



def ExcluirAluno(alunos, eventos):

    AlunoASerExcluido = input("Insira o nome do aluno a ser excluído: ").strip()

    if not validarString(AlunoASerExcluido):

        return "ERRO: O nome do aluno deve conter apenas letras e não pode estar vazio."

    if AlunoASerExcluido in alunos:

        alunos.remove(AlunoASerExcluido)

        for evento in eventos.values():

            if AlunoASerExcluido in evento["inscritos"]:

                evento["inscritos"].remove(AlunoASerExcluido)

        return f"Aluno '{AlunoASerExcluido}' excluído com sucesso."

    return "ERRO: Aluno não encontrado."



def ExibirEventos(eventos):

    if not eventos:

        return "Nenhum evento cadastrado."

    lista_eventos = []

    for titulo, dados in eventos.items():

        VagasRestantes = dados["capacidade"] - len(dados["inscritos"])

        lista_eventos.append(f"Evento: {titulo} | Capacidade: {dados['capacidade']} | Vagas Restantes: {VagasRestantes}")

    return lista_eventos



def ExibirResumo(eventos):

    if not eventos:

        return "Nenhum evento cadastrado para resumo."

    resumo = []

    for titulo, dados in eventos.items():

        resumo.append(f"Evento: {titulo} | Participantes: {len(dados['inscritos'])}")

    return resumo



def EditarEventoOuAluno(eventos, alunos):

    EdicaoAlunoOuEvento = input("Escolha uma opção (1 para Evento, 2 para Aluno): ").strip()

    if EdicaoAlunoOuEvento == "1":

        titulo = input("Insira o título do evento a ser editado: ").strip()

        if not validarString(titulo):

            return "ERRO: O título do evento deve conter apenas letras e não pode estar vazio."

        if titulo in eventos:

            NovoTitulo = input("Digite o novo título do evento: ").strip()

            if not validarString(NovoTitulo):

                return "ERRO: O novo título do evento deve conter apenas letras e não pode estar vazio."

            if NovoTitulo in eventos and NovoTitulo != titulo:

                return "ERRO: Já existe um evento com esse título."

            try:

                NovaCapacidade = int(input("Insira a nova capacidade do evento: "))

                if NovaCapacidade < len(eventos[titulo]["inscritos"]):

                    return "ERRO: A nova capacidade não pode ser menor que o número de inscritos."

                eventos[NovoTitulo] = eventos.pop(titulo)

                eventos[NovoTitulo]["capacidade"] = NovaCapacidade

                return "Evento editado com sucesso."

            except ValueError:

                return "ERRO: A capacidade deve ser um número inteiro."

        return "ERRO: Evento não encontrado."

    elif EdicaoAlunoOuEvento == "2":

        NomeAlunoAserEditado = input("Insira o nome do aluno a ser editado: ").strip()

        if not validarString(NomeAlunoAserEditado):

            return "ERRO: O nome do aluno deve conter apenas letras e não pode estar vazio."

        if NomeAlunoAserEditado in alunos:

            NovoNome = input("Insira o novo nome do aluno: ").strip()

            if not validarString(NovoNome):

                return "ERRO: O novo nome do aluno deve conter apenas letras e não pode estar vazio."

            for evento in eventos.values():

                if NomeAlunoAserEditado in evento["inscritos"]:

                    evento["inscritos"].remove(NomeAlunoAserEditado)

                    evento["inscritos"].append(NovoNome)

            alunos[alunos.index(NomeAlunoAserEditado)] = NovoNome

            return "Aluno editado com sucesso."

        return "ERRO: Aluno não encontrado."

    return "Opção inválida."



def main():

    eventos = {

        "PalestraIA": {"capacidade": 50, "inscritos": []},

        "OficinaPython": {"capacidade": 30, "inscritos": []},

    }

    alunos = ["Ana", "Bruno", "Carla"]


    while True:

        print(exibirMenu())

        opcao = input("Escolha uma opção: ").strip().lower()

        if opcao == "1":

            print(CadastrarEvento(eventos))

        elif opcao == "2":

            print(ExcluirEvento(eventos))

        elif opcao == "3":

            print(CadastrarAluno(alunos, eventos))

        elif opcao == "4":

            print(ExcluirAluno(alunos, eventos))

        elif opcao == "5":

            eventos_listados = ExibirEventos(eventos)

            if isinstance(eventos_listados, list):

                for evento in eventos_listados:

                    print(evento)

            else:

                print(eventos_listados)

        elif opcao == "6":

            resumo = ExibirResumo(eventos)

            if isinstance(resumo, list):

                for linha in resumo:

                    print(linha)

            else:

                print(resumo)

        elif opcao == "7":

            print(EditarEventoOuAluno(eventos, alunos))

        elif opcao == "sair":

            print("Encerrando o programa. Até logo!")

            break

        else:

            print("Opção inválida. Tente novamente.")



if __name__ == "__main__":

    main()

