# 1. Crie uma função que calcule o tamanho de uma String. Tal função deverá ter um
# parâmetro de entrada, do tipo String. O retorno da função deverá ser do tipo Inteiro.
# No primeiro teste da função o valor do parâmetro de entrada deverá ser a letra de
# uma música de sua preferência. O programa que usará a função deverá exibir a
# mensagem “A letra da música (nome da música) tem (número de caracteres)
# caracteres. O desenvolvedor deverá validar o tipo do parâmetro de entrada, caso
# não seja válido, retornar o valor -1. Nesse caso o programa que usará a função
# deverá exibir mensagem de erro informando que a entrada de dados é inválida.”
NomeMusica = input("insira o TITULO da música:  \n")
letraMusica = input("Insira a letra da música desejada: \n")
def CalcularTamanhoMusicaString(letraMusica):
    TamanhoString = len(letraMusica)
    if (TamanhoString == -1):
        print("O valor escolhido é invalido!")
    else:
        return TamanhoString
print(f"A musica {NomeMusica} tem {CalcularTamanhoMusicaString(letraMusica)} caractéres.")

# 2. Crie uma função que retorne um caracter de uma String em uma posição específica.
# Para tanto, dois argumentos de entrada deverão ser fornecidos: a string e a posição
# que se deseja ter um carácter retornado. O controle sobre a posição (índice)
# passada por parâmetro é de responsabilidade do desenvolvedor. Caso uma posição
# inválida (IndexError: string index out of range) seja fornecida pelo usuário, a função
# deverá retornar “-1”. Nesse caso, o programa que usa a função deverá exibir a
# mensagem “Índice fora do intervalo". A String não possui o índice {índice passado
# como parâmetro}”. Execute os testes na função tal que o primeiro caracter possa ser
# retornado, o último, um do meio da String, etc…
StringFrase = str(input("Insira uma frase:  \n"))
PosicaoString = int(input("INforme a posição da letra que quer: \n"))
def  LocalizarCaracter(StringFrase, PosicaoString):
    try:
        print(f"A letra de index {PosicaoString} é {StringFrase[PosicaoString - 1]}")
    except IndexError():
        print("Indice fora do alcance!")
LocalizarCaracter(StringFrase, PosicaoString)

# 3. Crie uma função que itere sobre uma String, através de um laço de repetição,
# passada como parâmetro e exiba o caracter e a posição que esse caracter aparece
# na String. Por exemplo: Z - 8º caracter da String “string passada como parâmetro”
def exibir_caracteres_com_posicao(StringCaracterPosicao):
    # Itera sobre a string e exibe o caractere e sua posição
    for i, CaracterEscolhido in enumerate(StringCaracterPosicao):
        print(f"{CaracterEscolhido} - {i + 1}º caracter da string")
FraseAtividade3 = input("Digite uma Frase: ")
exibir_caracteres_com_posicao(FraseAtividade3)

# 4. Crie uma função que retorne verdadeiro ou falso quando avalia se uma frase termina
# com determinada palavra ou letra. A frase deverá ser passada através de uma
# variável, criada e inicializada previamente, enquanto que a palavra ou letra deve ser
# passada entre aspas duplas. O programa que usar essa função deverá exibir a
# mensagem [A frase passada por parâmetro] termina com [palavra ou letra passada
# por parâmetro] quando a função retornar VERDADEIRO. Caso contrário, exibir a
# mensagem: [A frase passada por parâmetro] NÃO termina com [palavra ou letra
# passada por parâmetro]. Para efeito de testes, inicialize a variável criada com uma
# das estrofes do hino nacional brasileiro.
FraseParaTerminar = str(input("Informe uma palavra ou frase para verificar se termina com alguma letra/palavra:    \n "))
FraseOuPalavraParaVerificar = input("Insira uma palavra ou letra para ver se ela está presente no final da palavra:  \n")
def FuncaoVerdadeiroFalso(FraseParaTerminar,FraseOuPalavraParaVerificar):
    if (FraseParaTerminar.endswith(FraseOuPalavraParaVerificar)):
        print(f"{FraseParaTerminar} Termina com {FraseOuPalavraParaVerificar}!")
    else:
        print(f"{FraseParaTerminar} Não Termina com {FraseOuPalavraParaVerificar}!")
(FuncaoVerdadeiroFalso(FraseParaTerminar, FraseOuPalavraParaVerificar))

# 5. Crie uma função que implemente a questão 1 da avaliação01 teórico-prática.
def conceitoVariavel():
    print('''Em Python, uma variável é um nome que se refere a um valor específico. Pense nela como uma caixinha onde você pode guardar um número, um texto, uma lista ou qualquer outro tipo de dado. Você dá um nome a essa caixinha para que possa encontrar o valor armazenado mais tarde.
    Existem algumas regras e convenções que você deve seguir ao nomear suas variáveis em Python:
    Os nomes das variáveis devem começar com uma letra ou um underscore (_).
    Os nomes das variáveis podem conter letras, números e underscores.
    Os nomes das variáveis não podem conter espaços ou caracteres especiais, e não podem ser palavras reservadas do Python (como if, for, print, etc.).
    Python diferencia maiúsculas de minúsculas, portanto variavel e Variavel seriam consideradas variáveis diferentes.''')
def conceitoLacoInfinito():
    print('''O loop infinito é um conceito importante na programação, e em Python não é diferente. Em termos simples, um loop infinito é um trecho de código que se repete continuamente, sem uma condição de parada definida. Isso significa que o código dentro do loop será executado repetidamente, até que uma condição específica seja atendida para interromper a execução. Em Python, podemos criar um loop infinito usando a estrutura de controle “while True”.''')
def conceitoSemantica():
    print('''O Que é Semântica? Aqui, a semântica é clara: o código soma x e y e imprime o resultado, que será 15 . Se você trocasse o + por - , o resultado seria -5 . A semântica ajuda você a entender o que cada linha do código está realmente fazendo. É a parte abstrata do código.''')
def conceitoSintaxe():
    print('''A sintaxe é a parte "concreta" do código, as palavras e comandos utilizados. Ela checa se eles estão escritos da forma correta perante as regras de cada um e se funcionam dentro de seu contexto.''')
def inputDoUsuario():
    while True:
        opcaoUsuario = input("Insira a opção que deseja escolher: ").strip().lower()
        if (opcaoUsuario == ""):
            print("Insira, pelo menos, ALGUMA COISA.")
        elif (opcaoUsuario == "sair"):
            break
        elif (opcaoUsuario == "1"):
            conceitoVariavel()
            break
        elif (opcaoUsuario == "2"):
            conceitoLacoInfinito()
            break
        elif (opcaoUsuario == "3"):
            conceitoSemantica()
            break
        elif (opcaoUsuario == "4"):
            conceitoSintaxe()
            break
        elif (opcaoUsuario.isdigit == True):
            print("Insira um número disponível no menu.")
        else:
            print("Para sair do programa, digite 'sair'.")
print('''Para cada, opção, digite seu número correspondente:
      1 - Conceito de variáveis
      2 - Conceito de loops infinitos 
      3 - Conceito de semântica
      4 - Conceito de sintaxe''')
inputDoUsuario()


# 6. Crie uma função que implemente a questão 4 da avaliação01 teórico-prática.
('''- Uma letra maiúscula;
- Uma letra minúscula;
- Um caracter especial ($#!@&)
- Mínimo de 6 caracteres;
- Máximo de 20 caracteres.''')
def criarSenha():
    while True:
        senhaOriginal = input("Insira a senha:\n").strip()
        if (len(senhaOriginal) < 6):
            print("A senha deve ter mais de 6 caracteres.")
        elif (len(senhaOriginal) > 20):
            print("A senha deve ter menos de 20 caracteres.")
        elif (not any(i.isupper() for i in senhaOriginal)):
            print("A senha deve conter pelo menos uma letra maiúscula.")
        elif (not any(i.islower() for i in senhaOriginal)):
            print("A senha deve conter pelo menos uma letra minúscula.")
        elif (not any(i in "$#!@&" for i in senhaOriginal)):
            print("A senha deve conter pelo menos um caracter especial ($#!@&).")
        else:
            print("Senha criada com sucesso! (espaços retirados!)")
            return senhaOriginal
def verificarSenha(senhaOriginal):
    while True:
        tentativaConfirmacao = input("Confirme a senha criada:\n")
        if (tentativaConfirmacao != senhaOriginal):
            print("A senha inserida não está correta. Tente novamente.")
        else:
            print("Senha confirmada com sucesso!")
            break
senha = criarSenha()
verificarSenha(senha)

# 7. Crie uma função que receba uma String, toda em letras minúsculas, e retorne essa
# mesma String passada como parâmetro com a primeira letra de cada palavra em
# maiuscula. O desenvolvedor deve garantir que a String esteja em letras minúsculas.
# Como forma de testes, o seu nome completo pode ser passado como parâmetro
# dessa função.
def string_para_palavras_minusculas(StringMaiuscula):
    StringMaiuscula = StringMaiuscula.lower()
    return StringMaiuscula.title()
palavraStringParaDeixarmaiuscula = str(input("Insira o seu nome completo em letras minusculas: \n"))
ResultadoJamaiusculo = string_para_palavras_minusculas(palavraStringParaDeixarmaiuscula)
print(f"{palavraStringParaDeixarmaiuscula.title()}")


# 8. Crie uma função que receba uma String e um caracter imprimível. Essa função
# deverá retornar a String passada por parâmetro com o caracter dentro da string, por
# exemplo “Python” -> “P*y*t*h*o*n”.
TextoString = str(input("Insira uma palavra ou texto:   \n"))
CaracterSelecionado = input("Insira um caracter para ser colocado entre as letras:  \n")
def inserir_caractere_na_string(TextoString, CaracterSelecionado):
    return CaracterSelecionado.join(TextoString)
resultado = inserir_caractere_na_string(f"{TextoString}", f"{CaracterSelecionado}")
print(resultado) 
