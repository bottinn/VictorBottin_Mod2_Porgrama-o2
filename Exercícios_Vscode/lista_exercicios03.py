#1
Num_1 = int(input("Insira um valor numérico:  "))
Num_2 = int(input("Insira o segundo valor: "))

Soma = Num_1 + Num_2
subtracao = Num_1 - Num_2
multiplicacao = Num_1 * Num_2
divisao = Num_1 / Num_2

print(f"A soma desses números é de: {Soma}")
print(f"A subtração desses números é de: {subtracao}")
print(f"A multiplicação desses números é de: {multiplicacao}")
print(f"A divisão desses números é de: {divisao}")

#2

Peso = float(input("Insira o seu peço em Quilos: "))
altura = float(input("insira a sua altura em metros: "))
IMC = Peso / (altura*altura)
print(f"Seu IMC é de {IMC}")

#3

Frase = "Bem vindo turma da Programação II ao mundo da programação Python!!!" [:: - 1]
print(Frase)

#4

import random
TamannhoSenhaGerada = int(input("Informe o tamanho da senha: "))
uuid_gerador_senha = "9aed7be2-8905-4c7f-b1da-de9d9979b908" "86fa9665-46e7-4f45-a90f-a0b81105071d" "b5440c24-c6b0-42fb-9105-96497a8ca076"
senha_gerada = " ".join(random.sample(uuid_gerador_senha, TamannhoSenhaGerada))
print(f"Senha gerada com {TamannhoSenhaGerada} caracteres {senha_gerada}")

#5

import datetime
agora = datetime.datetime.now()

print("Data e Hora atual:")
print(agora.strftime("%D/%m/%y          %H:%M:%S"))