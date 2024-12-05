import random
#FUNÇÃO PRINCIPAL
def main():
    while True:
        entradaUsuario = input('''Selecione qual lista de exercícios deseja visualizar:
            1 - Lista de exercícios 03;
            2 -  Lista de exercício estruturas condicionais ou de decisão;
            3 - Exercício 01 - estruturas de repetição;
            4 - Código exemplo validação da entrada via stdin;
            5 - Lista For de exercícios.
            Insira o número da lista que deseja ver os programas: ''').strip().lower()
        if (entradaUsuario == "sair"):
            print("Programa encerrado.")
            break
        elif not (entradaUsuario == "1" or entradaUsuario == "2" or entradaUsuario == "3" or entradaUsuario == "4" or entradaUsuario == "5"):
            print("O valor deve ser entre 1 e 5.")
        elif (entradaUsuario == "1"):
            calculadoraNumeros()
            imc()
            inversoTexto()
            geraSenha()
            break
        elif (entradaUsuario == "2"):
            doisValoresMaiorMenor()
            escolherMedico()
            desmontarFrase()
            parOuImpar()
            doisNumerosNegativoPositivo()
            maiorEntreDoisNumeros()
            imcCategorias()
            break
        elif (entradaUsuario == "3"):
            ValorMaiorVariavel()
            TentativaDeAcertarOnumero()
            VerificarEndereco()
            break
        elif (entradaUsuario == "4"):
            validacaoEntradaStdin()
            break
        elif (entradaUsuario == "5"):
            FraseInstituto()
            NumerosParesFOr()
            MultiplicacaoDeDoisNumeros()
            VinteSegundos()
            SomaNumerosPareseImpares()
            NumeroPrimo()
            Palindromo()
            ParametrosIndefinidos()
            QuantidadeMaiusculaseMinusculas()
            break
        else:
            print("Insira um valor númerico válido.")
            
            
    

#Lista de exercícios 3
def calculadoraNumeros():
    while True:
        try:
            num1 = int(input("Por favor, insira um número: "))
            break
        except ValueError:
            print("Insira um valor válido.")
    while True:
        try:
            num2 = int(input("Agora o segundo: "))
            break
        except ValueError:
            print("Insira um valor válido.")
    print(f'''Os resultados foram: 
      Soma: {num1+num2}
      Subtração: {num1-num2}
      Multiplicação: {num1*num2}
      Divisão: {num1/num2}''')

def imc():
    altura = float(input("Insira a altura da pessoa, em metros, por favor: "))
    peso = float(input("Agora, o peso: "))
    alturaa = altura*altura
    imc = peso / alturaa
    print(f"O IMC dessa pessoa é de {imc:.2f}")
    return imc
    
def inversoTexto():
    texto = "Bem vindo turma da Programação II ao mundo da programação Python!!!"
    inverso = texto[::-1]
    return inverso

def geraSenha():
    numeroCaracteres = int(input("Insira o número de caracteres que deseja na sua senha: "))
    uuid_gerador_senha = "3b33eab3-50d4-4223-8e9a-e8bea8906fdd"
    if (numeroCaracteres > 128 or numeroCaracteres < 0):
        semha_gerada = "".join(random.sample(uuid_gerador_senha, numeroCaracteres))
        print(f"Senha gerada com {numeroCaracteres}. Senha: {semha_gerada}")
    else:
        print("Número inválido.")
    return semha_gerada

#Lista de exercício estruturas condicionais ou de decisão
def doisValoresMaiorMenor():
    while True:
        numMenor = input("Insira o primeiro número, ele deve ser menor do que o próximo.\n").strip()
        if (numMenor.isdigit() == False):
            print("Prompt inválido, tente novamente.")
        else:
            break
    while True:
        numMaior = input("Agora, insira o número maior.").strip()
        if(numMaior.isdigit() == False):
            print("Prompt inválido, tente novamente.")
        else:
            break
    if(numMenor > numMaior):
        print(f"O primeiro número inserido ({numMenor}) foi maior que o segundo ({numMaior}).")
    elif(numMenor == numMaior):
        print(f"Os números maior ({numMaior}) e menor ({numMenor}) são iguais.")
    else:
        print(f"O primeiro número inserido ({numMenor}) foi menor que o segundo ({numMaior}).")
        
def escolherMedico():
    while True:
        numeroMedico = input('''Escolha com qual médico deseja ter a consulta:
                         Digite 1 para Carlão Gaúcho de Apartamento
                         Digite 2 para Rogério das Cenoura Cozida
                         Digite 3 para Tiago Come Sucuri''').strip()
        if (numeroMedico.isdigit() == False):
            print("Tente novamente.")
        else:
            if(numeroMedico == "1"):
                print(f"Consulta agendada com Carlao Gaucho de Apartamento!")
                break
            elif(numeroMedico == "2"):
                print(f"Consulta agendada com Rogério das Cenoura Cozida!")
                break
            elif(numeroMedico == "3"):
                print(f"Consulta agendada com Thiago Come Sucuri!")
                break
            else:
                print("Número inválido.")

def desmontarFrase():
    fraseOrigem = "python é uma excelente linguagem de programação!!!"
    larguraDaMensagem = len(fraseOrigem)
    tentativaUsuario = input(f"Sem conhecer a frase base, tente adivinhar uma ou mais palavras que constam nela.\n").lower()
    larguraDaTentativa = len(tentativaUsuario)
    if (larguraDaTentativa > larguraDaMensagem): #impede que palavras menores sejam achadas em maiores, como "casaco" caiba em "casa"
        print("A tentativa tem mais caracteres do que a frase original.")
    else:
        for i in range(len(tentativaUsuario), 0, -1): #pega o tamanho da tentativa e decrementa -1 diminuindo uma letra por vez
            subFrase = tentativaUsuario[:i] #fatia a string de acordo com o valor do contador
            verificacao = fraseOrigem.find(subFrase) #verifica se cada string fatiada está presente na frase
            if verificacao != -1:
                print(f"O trecho '{subFrase}' está na frase original.")
                break #sai do loop, pq achou a maior substring posível
            else:
                print(f"O trecho '{subFrase}' não está na frase original.")
                #mesmo picotando tudo ele não conseguiu acha nada.
                
def parOuImpar():
    while True:
        nume = input("Insira um número. O programa irá calcular se ele é par ou ímpar.").strip()
        if (nume.isdigit() == False):
            print("Tente novamente.")
        else:
            nume = int(nume)
            if(nume % 2 == 0):
                print(f"O número {nume} é par.")
                break
            else:
                print(f"O número {nume} é ímpar.")
                break
            
def doisNumerosNegativoPositivo():
    while True:    
        numer1 = input("Insira o primeiro número.").strip()
        if(numer1.isdigit() == False):
            print("Tente novamente.")
        numer2 = input("Agora, o segundo.").strip()
        if(numer2.isdigit() == False):
            print("Tente novamente.")
        if(numer1 > 0 and numer2 > 0):
            print("Ambos os números são positivos.")
            break
        else:
            print("Um dos números ou os dois são negativos.")
            break
        
def maiorEntreDoisNumeros():
    while True:
        nume1 = input("Insira o primeiro número.").strip()
        if (nume1.isdigit() == False):
            print("Tente novamente.")
        nume2 = input("Agora, insira o segundo número.").strip()
        if (nume2.isdigit() == False):
            print("Tente novamente.")
        if(nume1 > nume2):
            print(f"O primeiro número inserido ({nume1}) foi maior que o segundo ({nume2}).")
            break
        elif(nume1 == nume2):
            print(f"Os dois números ({nume1} e {nume2}) são iguais.")
            break
        else:
            print(f"O primeiro número inserido ({nume1}) foi menor que o segundo ({nume2}).")
            break

def imcCategorias():
    while True:
        peso = input(f"Para calcular o IMC, insira o peso em quilos: ").strip()
        try:
            peso = float(peso)
        except ValueError:
            print("Tente novamente.")
            continue #a boa prática hahaha
        altura = input(f"Agora, a altura em metros: ").strip()
        try:
            altura = float(altura)
        except ValueError:
            print("Tente novamente.")
            continue
        alturaPotenciada = altura**2
        imc = peso / alturaPotenciada
        if(imc <= 18.5):
            print(f"O IMC é de {imc:.2f}, caindo na categoria Abaixo do Peso.")
            break
        elif(imc > 18.5 and imc <= 24.9):
            print(f"O IMC é de {imc:.2f}, caindo na categoria Peso Normal.")
            break
        elif(imc > 24.9 and imc <= 29.9):
            print(f"O IMC é de {imc:.2f}, caindo na categoria Sobrepeso.")
            break
        elif(imc >= 30):
            print(f"O IMC é de {imc:.2f}, caindo na categoria Obesidade Sdg.")
            break
        else:
            print("IMC inválido.")
            break

#Exercício 01 - estruturas de repetição
def ValorMaiorVariavel():
    valor = int(50)
    while True:
        try: 
            inputUsuario = int(input("Insira um valor. \n"))
            break
        except ValueError:
            print("Digite um número válido.")
    if (inputUsuario <= valor):
        print("O valor inserido ainda é menor ou igual ao da variável.")
    else:
        print("O valor inserido é maior que o da variável.")
        
def TentativaDeAcertarOnumero():
        numeroRandom = random.randint(0,10)
        contador = 0
        numerosTentados = []
        while (contador != 5):
            while True:
                try:
                    inputUser = int(input("Um número de 0-10 foi salvo numa variável. Tente adivinhá-lo."))
                    break
                except ValueError:
                    print("Insira um número válido.")
            if (inputUser > 10 or inputUser < 0):
                print("Por favor, insira um número entre 0 e 10.")
            else:
                if (inputUser in numerosTentados):
                    print("Você já tentou utilizar esse número. Tente outro.")
                else:
                    if (inputUser == numeroRandom):
                        print("Parabéns, você conseguiu acertar o número!")
                        break
                    elif (inputUser != numeroRandom and contador < 4):
                        print(f"Você não conseguiu acertar o número. Por favor tente novamente. Tentativa número {contador+1}.")
                        contador = contador + 1
                        numerosTentados.append(inputUser)
                    else:
                        print("Você não acertou o número. Acabaram suas tentativas.")
                        break
                    
def VerificarEndereco():
    while True:
        endereçoDigitado = input("Por favor, escreva o endereço da URL:\n").strip()
        if (endereçoDigitado.startswith("www.") == True and endereçoDigitado.endswith(".com.br") == True):
            print(f"Perfeito, o endereço {endereçoDigitado} foi escrito corretamente.")
            break
        else:
            print("O endereço foi escrito errado, nele podem estar faltando ou incorretos os termos de 'www.' e/ou '.com.br.")
            print(f"Link digitado: {endereçoDigitado}")

#Código exemplo validação da entrada via stdin
def validacaoEntradaStdin():
    primeiroValorInformadoPeloUsuario = input("Digite o primeiro número: ")
    segundoValorInformadoPeloUsuario  = input("Digite o segundo número: ")
    #Validação do tipo de entrada informada pelo Stdin (teclado)
    if not (primeiroValorInformadoPeloUsuario.strip().isnumeric()):
        print(f"O primeiro valor informado: \"{primeiroValorInformadoPeloUsuario}\" não é um valor numérico válido.")
    elif (not (segundoValorInformadoPeloUsuario.strip().isnumeric())):
        print(f"O segundo valor informado: \"{segundoValorInformadoPeloUsuario}\" não é um valor numérico válido.")
    else:
        opcaoDigitadaPeloUsuario = input("Informe um valor numérico de 1 a 10: ")
        #Validação do tipo de entrada informada pelo Stdin (teclado)
        if not (opcaoDigitadaPeloUsuario.strip().isnumeric()):
            print(f"A opção informada: \"{opcaoDigitadaPeloUsuario}\" é inválida. As opções numéricas válidas são: 1, 2, 3 ou 4.")
        elif (int(opcaoDigitadaPeloUsuario) <= 0 or int(opcaoDigitadaPeloUsuario) > 10):
            print(f"A opção informada: \"{opcaoDigitadaPeloUsuario}\" é inválida. As opções numéricas válidas são: 1, 2, 3 ou 4.")
        else:
            print("Todos os valores numéricos informados via stdin foram válidos.")    
        

#Lista For de exercícios
def FraseInstituto():
    frase = "Instituto Federal de Santa Catarina"
    print("Vertical:\n")
    for i in frase:
        print(f"{i}")
    print("Horizontal:")
    for i in frase:
        print(f"{i}", end="")

def NumerosParesFOr():
    print("\n")
    for i in range(0,20):
        if (i % 2 == 0):
            print(f"{i}")
            
def MultiplicacaoDeDoisNumeros():
    numeroInserido = int(input("Por favor, insira um número: "))
    for i in range (1,11):
        print(f"O número {numeroInserido} vezes {i} é igual à {numeroInserido*i}")
        
def VinteSegundos():
    for i in range(1, 20):
        print(f"{i}")
        
def SomaNumerosPareseImpares():
    somaImpares = int()
    quantVezes = int()
    for i in range(1, 100):
        if (i % 2 != 0):
            print(f"{i}")
            somaImpares = somaImpares + i
            quantVezes = quantVezes + 1
    print(f"A quantidade de vezes foi {quantVezes}, e a soma dos números é {somaImpares}.")
    
def NumeroPrimo():
    numerosDivisiveis = int()
    listaDivisiveis = []
    numeroColocado = int(input("Por favor, insira um número para saber se ele é primo: "))
    for i in reversed(range(1, numeroColocado + 1)):
        if (numeroColocado % i == 0):
            numerosDivisiveis += 1
            listaDivisiveis.append(i)
    if (numerosDivisiveis != 2):
        print(f"o número não é primo. Esse número é divisivel {numerosDivisiveis} vezes, sendo os divisores:\n{listaDivisiveis}")
    else:
        print(f"O número {numeroColocado} é primo.")
        
def Palindromo():
    inputUsuario = input("Digite uma frase ou string qualquer: ")
    fraseBackwards = ""
    for i in reversed(inputUsuario):
        fraseBackwards = fraseBackwards + i
    if (fraseBackwards == inputUsuario):
        print(f"A palavra {inputUsuario} é um palíndromo.")
    else:
        print(f"A palavra {inputUsuario} não é um palíndromo.")
        
def ParametrosIndefinidos():
    def soma(*arg):
        soma_num = 0 
        for c in range(0,len(arg)):
            soma_num = soma_num + arg[c]
        print(soma_num)
        soma(8,8)
        
def QuantidadeMaiusculaseMinusculas():
    fraseOriginal = input("Insira uma frase ou texto para verificar os seus caracteres: ")
    quantMaiusculas = sum(1 for letra  in fraseOriginal if letra.isupper)
    quantMinusculas = sum(1 for letra  in fraseOriginal if letra.islower)
    print(f"O número de maiúsculas é {quantMaiusculas}, e de minúsculas é {quantMinusculas}.")
    
main()