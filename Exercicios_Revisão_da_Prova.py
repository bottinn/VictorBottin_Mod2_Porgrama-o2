#1. Crie um programa que leia dois números inteiros do usuário e exiba a soma entre
#eles.
PrimeiroNumeroEscolhido = int(input("Escolha um número: "))
SegundoNumeroEscolhido = int(input("Escolha um número:  "))
print(f"O primeiro número escolhido é {PrimeiroNumeroEscolhido}")
print(f"O segundo número escolhido é {SegundoNumeroEscolhido}")

#2. Faça um programa que leia um número e informe se ele é positivo, negativo ou zero.
Numero_Positovo_Negativo_Zero = int(input("Insira um número:    "))
if Numero_Positovo_Negativo_Zero >= 1 :
    print("O número escolhido é positivo")
elif Numero_Positovo_Negativo_Zero <= -1 :
    print("O número escolhido é negativo")
elif Numero_Positovo_Negativo_Zero == 0 :
    print("O número escolhido é zero")

#3. Escreva um programa que leia dois números e exiba o maior deles.
NumeroEscolhido1 = int(input("Insira um número: "))
NumeroEscolhido2 = int(input("Insira um número: "))
if NumeroEscolhido1 > NumeroEscolhido2 :
    print("O primeiro número é maior!")
else :
    print("O segundo número é maior!")
#4. Crie um programa que calcule o quadrado de um número fornecido pelo usuário..
Numero_quadrado = int(input("Insira um número para saber seu quadrado:  "))
Numero_resolvido = Numero_quadrado * Numero_quadrado 
print(f"O quadrado desse número é:  {Numero_resolvido}")

#5. Escreva um programa que verifique se um número é par ou ímpar.
Numero_par_impar = int(input("Insira um número:     "))
if Numero_par_impar % 2 == 0:
    print("O número é par!")
else:
    print("O número é impar!")

#6. Crie um programa que peça a idade do usuário e exiba se ele é maior de idade ou
#não.
IdadeMaior = int(input("insira a sua idade: "))
if IdadeMaior >= 18:
    print("Você é maior de idade!")
else:
    print("Você é menor de idade!")

#7. Escreva um programa que calcule a média aritmética de três números fornecidos
#pelo usuário.
#8. Faça um programa que leia um valor e informe se ele está entre 10 e 20.
#9. Escreva um programa que verifique se um ano é bissexto.
#10. Crie um programa que leia um número e informe se ele é divisível por 3 ou por 5.
#11. Faça um programa que peça um número inteiro e exiba todos os números de 1 até o
#número fornecido.
#12. Crie um programa que leia a temperatura em graus Celsius e converta para
#Fahrenheit. Expressão de conversão: (celsius * 9/5) + 32.
#13. Escreva um programa que peça o nome e a idade de uma pessoa e exiba uma
#mensagem de boas-vindas personalizada.
#14. Crie um programa que leia dois números e exiba o resultado da multiplicação entre
#eles.
#15. Faça um programa que leia três números e exiba o menor deles.
#16. Escreva um programa que leia a nota de um aluno e verifique se ele foi aprovado
#(nota >= 6).
#17. Crie um programa que leia o peso e a altura de uma pessoa e calcule seu IMC.
#18. Faça um programa que leia um número e exiba sua tabuada (de 1 a 10).
#19. Crie um programa que conte de 1 até 100 e exiba apenas os números pares.
#20. Faça um programa que simule uma calculadora simples (soma, subtração,
#multiplicação e divisão) com duas entradas do usuário.
#21. Crie um programa que peça um número ao usuário e imprima se ele é primo ou não.
#22. Escreva um programa que some todos os números de 1 até 100.
#23. Crie um programa que peça um número e calcule seu fatorial.