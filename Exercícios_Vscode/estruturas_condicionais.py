#1) Crie 2 variáveis com dois valores numéricos inteiros informados pelo
#suário, caso o valor do primeiro número for maior do que o segundo,
#exiba em tela uma mensagem de acordo, caso contrário, exiba em tela
#uma mensagem dizendo que o primeiro valor digitado é menor que o
#segundo. Os números informados pelo usuário devem aparecer em
#ambas as mensagens.

print("por favor insira o primeiro valor maior que o segundo!")
numero1 = int(input("Insira um número inteiro:  "))
numero2 = int(input("Insira um número inteiro:  "))
if numero1 > numero2: 
    print(f"O valor {numero1} é maior que o número {numero2}")
else :
    print(f"O valor {numero1} é menor que o valor {numero2}, por favor insira um número valido")
    
#2) Crie um programa que possa marcar uma consulta médica. Como opções,
#teremos disponíveis apenas 03 médicos, que devem ter seus nomes
#exibidos na tela, p/ que possam ser escolhidos. Após a escolha do
#profissional médico, exibir mensagem na tela informando que a consulta
#foi marcada com o médico escolhido (nome do médico). 

print("Bom dia!")
print("Gostaria de agendar um consulta com qual médico?")
print("Se deseja o médico João, digite 1.")
print("Se deseja o médico Luciano, digite 2.")
print("Se deseja o médico Ronaldo, digite 3.")
escolha = int(input("Com qual médico deseja fazer a consulta?: "))
if escolha == 1 :
    print("O médico escolhido foi o João!")
elif escolha == 2:
    print("o Médico escolhido foi o Luciano!")
if escolha == 3 :
    print("o Médico escolhido foi o Ronaldo!")
elif escolha > 4:
    print("Por favor escolha um número entre 1 - 3.")

#3) Escreva um programa que verifica se uma determinada palavra consta
#em um texto de origem. O texto não será conhecido pelo usuário que
#usará de palavras aleatórias na tentativa de adivinhar que palavras
#compõem a frase oculta. Frase: "Python é uma excelente linguagem de
#programação!!! Se acertar, a mensagem: "A palavra (palavra digitada
#pelo usuário) está na frase". Se errar, a mensagem: "A palavra (palavra
#digitada pelo usuário) não está na frase". Use a função "find", referenciada
#na documentação:
#https://docs.python.org/3/library/stdtypes.html
 
frase=("Python é uma excelente linguagem de programação!!!")
palavraescolhida= str(input("qual palavra deseja saber se está na frase?\n"))
posicao = frase.find("palavraescolhida")
if  posicao != -1:
    print(f"a palavra ({palavraescolhida}) está na frase.")
else:
    print(f"a palavra ({palavraescolhida}) não está na frase.")

#4) Crie um programa que leia um número e verifique se ele é par ou ímpar

NumeroEscolhido = int(input("Escolha um número: "))
if NumeroEscolhido % 2 == 0:
    print(f"O número {NumeroEscolhido} par")
else:
    print(f"O número{NumeroEscolhido} é ímpar")

#5) Escreva um programa que receba dois números e verifique se ambos são
#positivos

PossivelNumeroPositivo1 = float(input("Escolha um número:   "))
PossivelNumeroPositivo2 = float(input("escolha um número:   "))
if PossivelNumeroPositivo1 >= 1 and PossivelNumeroPositivo2 >= 1:
    print("Os dois números são possiivos!")
elif PossivelNumeroPositivo1 <= 0 and PossivelNumeroPositivo2 <= 0: 
    print("Os dois números são negativos!")
elif PossivelNumeroPositivo1 >= 1 and PossivelNumeroPositivo2 <= 0 :
    print("O primeiro número digitado é positivo, e o segundo é negativo")
elif PossivelNumeroPositivo1 <= 0 and PossivelNumeroPositivo2 >= 1 :
    print("O Pirmeiro número é negativo, e o segundo é positivo!")

#6) Crie um programa que leia dois números e exiba o maior entre eles. Caso
#sejam iguais, exiba uma mensagem informando isso.

PrimeiroNumeroEscolhidoParaMaiorOuMenor = int(input("Escolha um número: "))
SegundoNumeroEscolhidoParaMaiorOuMenor = int(input("Escolha um número:  "))
if PrimeiroNumeroEscolhidoParaMaiorOuMenor > SegundoNumeroEscolhidoParaMaiorOuMenor :
    print(f"O 1º Número {PrimeiroNumeroEscolhidoParaMaiorOuMenor} é maior que o 2º número {SegundoNumeroEscolhidoParaMaiorOuMenor} .")
elif PrimeiroNumeroEscolhidoParaMaiorOuMenor < SegundoNumeroEscolhidoParaMaiorOuMenor : 
    print(f"O 2º Número {SegundoNumeroEscolhidoParaMaiorOuMenor} é maior que o 1º número{PrimeiroNumeroEscolhidoParaMaiorOuMenor} .")
elif PrimeiroNumeroEscolhidoParaMaiorOuMenor == SegundoNumeroEscolhidoParaMaiorOuMenor: 
    print(f"Os dois Números {PrimeiroNumeroEscolhidoParaMaiorOuMenor} e {SegundoNumeroEscolhidoParaMaiorOuMenor} são iguais.")

#7) Crie um programa que receba o peso e a altura de uma pessoa e calcule
#seu Índice de Massa Corporal (IMC). imc = peso / (altura * altura) . O
#programa deve exibir uma mensagem na tela de acordo com a seguinte
#tabela:
# Abaixo de 18.5: Abaixo do peso
# Entre 18.5 e 24.9: Peso normal
# Entre 25 e 29.9: Sobrepeso
# Acima de 30: Obesidade sdg

PesoEmQuilos = float(input("Insira o seu peso em quilos:    "))
Altura = float(input("Insira a sua altura em metros:    "))
IMC = PesoEmQuilos / (Altura*Altura)
print(f"seu IMC é de {IMC}")
if IMC <= 18.5: 
    print("Você está abaixo do Peso!") 
elif IMC >=18.51 and IMC <=24.9: 
    print("Você está com o Peso normal!")
elif IMC >= 25 and IMC <=24.9: 
    print("Você está acima do Peso!")
elif IMC >= 30: 
    print("Você está Obeso!")