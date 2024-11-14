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
StringAtividade2 = str(input("Insira uma palavra ou frase:  \n"))
PosicaoAtividade2 = int(input("Insira o Número da casa que queira saber:    \n"))
def PosicaoEscolhidaNumeroAtividade2(StringAtividade2,PosicaoAtividade2):
    if PosicaoAtividade2 == -1:
        return -1
    elif PosicaoAtividade2 == [1-100]:
        return (PosicaoAtividade2)
CasaEscolhida = PosicaoAtividade2        



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



# 5. Crie uma função que implemente a questão 1 da avaliação01 teórico-prática.
# 6. Crie uma função que implemente a questão 4 da avaliação01 teórico-prática.


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
