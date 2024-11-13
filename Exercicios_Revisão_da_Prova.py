#1. Crie um programa que leia dois números inteiros do usuário e exiba a soma entre eles.
numero1 = int(input("Insira um numero: "))
numero2 = int(input("Insira um numero: "))
print(f"A soma é {numero1 + numero2}")

#2. Faça um programa que leia um número e informe se ele é positivo, negativo ou zero.
numeroInseridoPelaPessoa = int(input("Insira um numero: "))
if (numeroInseridoPelaPessoa > 0):
    print("O número é positivo.")
elif (numeroInseridoPelaPessoa < 0):
    print("O número é negativo.")
else:
    print("O número é 0.")
    
#3. Escreva um programa que leia dois números e exiba o maior deles.
num1 = int(input("Insira um numero: "))
num2 = int(input("Insira um numero: "))
if (num1 > num2):
    print("O primeiro número é o maior.")
elif (num2 > num1):
    print("O segundo número é o maior.")
else:
    print("Os números são iguais.")
    
#4. Crie um programa que calcule o quadrado de um número fornecido pelo usuário..
numeroInseridoPeloUser = int(input("Insira um numero: "))
print(f"O quadrado do número é {numeroInseridoPeloUser*numeroInseridoPeloUser}")

#5. Escreva um programa que verifique se um número é par ou ímpar.
num = int(input("Insira um numero: "))
if (num % 2 == 0):
    print("O número é par.")
else:
    print("O número é ímpar.")
    
#6. Crie um programa que peça a idade do usuário e exiba se ele é maior de idade ou não.
idadeInserida = int(input("Insira sua idade: "))
if (idadeInserida > 18):
    print("Você é maior de idade.")
else:
    print("Você não é maior de idade.")
    
#7. Escreva um programa que calcule a média aritmética de três números fornecidos pelo usuário.
numUm = int(input("Por favor insira o número: "))
numDois = int(input("Por favor insira o número: "))
numTres = int(input("Por favor insira o número: "))
media = numUm + numDois + numTres
print(f"A média entre os três números é de {media/3}")

#8. Faça um programa que leia um valor e informe se ele está entre 10 e 20.
valorInserido = float(input("Insira um valor: "))
if (valorInserido >=10) and (valorInserido <=20):
    print("O valor está entre 10 e 20.")
else :
    print("O valor inserido não está entre 10 e 20.")

#9. Escreva um programa que verifique se um ano é bissexto
anoInserido = int(input("Insira um ano: "))
if(anoInserido % 4 == 0 and anoInserido % 100 != 0):
    print("O ano não é bissexto.")
else:
    print("O ano é bissexto.")

#10. Crie um programa que leia um número e informe se ele é divisível por 3 ou por 5.
numeroColocado = float(input("Insira um número: "))
if (numeroColocado % 3 == 0) or (numeroColocado % 5 == 0):
    print("O número inserido é divisivel por 3 ou 5.")
else:
    print("O número inserido não é divisivel por 3 ou 5.")

#11. Faça um programa que peça um número inteiro e exiba todos os números de 1 até o número fornecido.
numeroInserido = int(input("Informe um valor inteiro: "))
controleDoLaco = 1
while (controleDoLaco <= numeroInserido):
    print(f"{controleDoLaco}")
    controleDoLaco+=1

#12. Crie um programa que leia a temperatura em graus Celsius e converta para Fahrenheit. Expressão de conversão: (celsius * 9/5) + 32.
temperaturaEmCelcius = float(input("Insira a temperatura em graus Celciuis: "))
print(f"A conversão para Farenheit é: {temperaturaEmCelcius*1.8+32}")

#13. Escreva um programa que peça o nome e a idade de uma pessoa e exiba uma mensagem de boas-vindas personalizada
nome = input("Informe o seu nome: ")
idade = int(input("Informe sua idade: "))
print(f"Seja bem-vindo {nome}! Seus {idade} anos de vida e você são muito bem-vindos <3")

#14. Crie um programa que leia dois números e exiba o resultado da multiplicação entre eles.
primeiroNumeroInserido = float(input("Insira o primeiro número: "))
segundoNumeroInserido = float(input("Insira o segundo número: "))
print(f"A multiplicação entre estes dois números é: {primeiroNumeroInserido*segundoNumeroInserido}")

#15. Faça um programa que leia três números e exiba o menor deles.
primeiroNumero = float(input("Insira o primeiro número: "))
segundoNumero = float(input("Insira o segundo número: "))
terceiroNumero = float(input("Insira o terceiro número: "))
menorNumero = primeiroNumero
if (segundoNumero < menorNumero):
    menorNumero = segundoNumero
elif (terceiroNumero < menorNumero):
    menorNumero = terceiroNumero
print(f"O menor número é: {menorNumero}")

#16. Escreva um programa que leia a nota de um aluno e verifique se ele foi aprovado (nota >= 6).
nota = float(input("Insira a nota do aluno: "))
if (nota >= 6):
    print("Aluno aprovado.")
else:
    print("Aluno reprovado")

#17. Crie um programa que leia o peso e a altura de uma pessoa e calcule seu IMC. 
peso = float(input("Informe seu peso: "))
altura = float(input("informe sua altura: "))
imc = peso/(altura**2)
print(f"O seu ídice de massa corporal é: {imc}")

#18. Faça um programa que leia um número e exiba sua tabuada (de 1 a 10)
numeroBotado = int(input("Informe um número inteiro: "))
for i in range (0,10):
    print(f"O número {numeroBotado} vezes {i} é igual à {numeroBotado * i}\n")

#19. Crie um programa que conte de 1 até 100 e exiba apenas os números pares
controleDoLacoWhile = 1
while (controleDoLacoWhile <= 100):
    if (controleDoLacoWhile % 2 == 0):
        print(f"{controleDoLacoWhile}")
    controleDoLacoWhile = controleDoLacoWhile + 1

#20. Faça um programa que simule uma calculadora simples (soma, subtração, multiplicação e divisão) com duas entradas do usuário.
entradaUm = float(input("Insira o primeiro valor"))
entradaDois = float(input("Insira o segundo valor"))
operacao = int(input("Escolha a Operação: 1- soma 2- subtração 3- multiplicação 4- divisão"))
if(operacao == 1):
    print(f"Soma selecionada. {entradaUm} + {entradaDois} = {entradaUm + entradaDois}")
elif (operacao == 2):
    print(f"Subtração selecionada. {entradaUm} - {entradaDois} = {entradaUm - entradaDois}")
elif (operacao == 3):
    print(f"Multiplicação selecionada. {entradaUm} * {entradaDois} = {entradaUm * entradaDois}")
elif (operacao == 4):
    print(f"Divisão selecionada. {entradaUm} / {entradaDois} = {entradaUm / entradaDois}")
else:
    print("Seleção inválida")

#21. Crie um programa que peça um número ao usuário e imprima se ele é primo ou não.
numero = int(input("Informe um número inteiro: "))
if (numero%1==0) and (numero%numero==0) and (numero%3!=0) and (numero%2!=0):
    print("É um número primo")
else :
    print("Não é um número primo.")

#22. Escreva um programa que some todos os números de 1 até 100.
soma = 0 
controleDoLacoRepeticao = 1
while (controleDoLacoRepeticao <= 100):
    soma += controleDoLacoRepeticao
    controleDoLacoRepeticao += 1
print(f"A soma dos 100 primeiros números é {soma}")

#23. Crie um programa que peça um número e calcule seu fatorial.
numeroASerCalculadoOFatorial = int(input("Informe um número para ser calculado o fatorial: "))
fatorial = 1
controleDoLacoDeRepeticao = 1
while (controleDoLacoDeRepeticao <= numeroASerCalculadoOFatorial):
    fatorial *= controleDoLacoDeRepeticao
    controleDoLacoDeRepeticao += 1
print(f"O fatorial do número digitado é {fatorial}")