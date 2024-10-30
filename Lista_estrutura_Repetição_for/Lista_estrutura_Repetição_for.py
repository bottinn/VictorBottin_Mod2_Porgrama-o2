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
#7) Crie um programa que pede que o usuário digite um nome ou uma frase,
#verifique se esse conteúdo digitado é um palíndromo ou não, exibindo em
#tela esse resultado.
#8) Crie uma função de número de parâmetros indefinido, que realize a soma
#dos números passados como parâmetro, independentemente da
#quantidade de parâmetros.
#9) Escreva um programa que lê uma palavra ou frase digitada pelo usuário,
#retornando o número de letras maiúsculas e minúsculas da mesma. Usar
#apenas de logica e de funções embutidas ao sistema.