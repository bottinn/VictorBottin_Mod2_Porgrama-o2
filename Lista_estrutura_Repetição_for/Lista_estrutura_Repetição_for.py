#LISTA DE EXERCÍCIOS ESTRUTURA DE REPETIÇÃO
#“FOR”
#1) Crie uma estrutura de repetição que percorra a String “Instituto Federal
#de Santa Catarina” exibindo na tela letra por letra dessa String, tanto na
#orientação horizontal quanto na vertical.
FraseIFSC = 'Instituto Federal de Santa Catarina'
print("Frase na forma Vertical:")
for i in FraseIFSC:
    print(f"{i}")
print("Frase de forma Horizontal:")
for i in FraseIFSC:
    print(f"{i}", end="")
print("\n")
#2) Crie um programa que realiza a contagem de 0 a 20, exibindo apenas os
#números pares.
for i in range(1,21):
    if i %2 == 0:
        print(f"{i}")
#3) Crie um programa que exiba na tela a tabuada de um determinado número
#fornecido pelo usuário.
Numero_Tabuada = int(input("Insira um número para saber a sua tabuada:  "))
for i in range(1,11):
    print(f"O número {Numero_Tabuada} vezes {i} é de {Numero_Tabuada*i}")
#4) Crie um programa que realiza a contagem regressiva de 20 segundos.
for i in range(20,0,-1):
    print(f"Segundo: {i}")
#5) Crie um programa que realiza a contagem de 1 até 100, considerando
#apenas os números ímpares. Exiba na tela quantos números ímpares
#foram encontrados nesse intervalo e qual a soma desses números
#ímpares.
soma = 0
contagem = 0
for i in range(1, 101):
    if i % 2 != 0:
        print(f"Números impares {i}")
        soma += i       
        contagem += 1   
print(f"Números ímpares encontrados: {contagem}")
print(f"Soma dos números ímpares: {soma}")
#6) Crie um programa que pede ao usuário que digite um número qualquer,
#em seguida retorne se esse número é primo ou não, caso não, retorne
#também quantas vezes esse número é divisível.
numero_primo = int(input("Digite um número: "))
divisores_primo = 0
for i in range(1, numero_primo + 1):
    if numero_primo % i == 0:
        divisores_primo += 1
if divisores_primo == 2:
    print(f"O número {numero_primo} é primo.")
else:
    print(f"O número {numero_primo} não é primo e é divisível {divisores_primo} vezes.")

#7) Crie um programa que pede que o usuário digite um nome ou uma frase,
#verifique se esse conteúdo digitado é um palíndromo ou não, exibindo em
#tela esse resultado.
entrada = input("Digite um nome ou uma frase: ")
entrada_processada = entrada.replace(" ", "").lower()
if entrada_processada == entrada_processada[::-1]:
    print(f'"{entrada}" é um palíndromo.')
else:
    print(f'"{entrada}" não é um palíndromo.')
for i in entrada_processada:
    print(f"{i}")
#8) Crie uma função de número de parâmetros indefinido, que realize a soma
#dos números passados como parâmetro, independentemente da
#quantidade de parâmetros.
def soma(*args):
    return sum(args)
print("Função de parâmetros:    ")
print(soma(1, 2, 3))  
print(soma(10, 20, 30, 40))  
print(soma(5, 5)) 

#9) Escreva um programa que lê uma palavra ou frase digitada pelo usuário,
#retornando o número de letras maiúsculas e minúsculas da mesma. Usar
#apenas de logica e de funções embutidas ao sistema.
FraseDigitadaParaContadorDeLetras = str(input("Insira Uma frase ou palavra: "))
LetrasMaiusculas = sum(1 for letra in FraseDigitadaParaContadorDeLetras if letra.isupper())
LetrasMinusculas = sum(1 for letra in FraseDigitadaParaContadorDeLetras if letra.islower())
print(f"O número de Letras maisculas é de {LetrasMaiusculas}")
print(f"O número de Letras minusculas é de {LetrasMinusculas}")
