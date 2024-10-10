#1) Crie e inicialize uma variável do tipo inteiro. Enquanto o valor dessa variável for
#menor ou igual a um valor definido por você, exiba uma mensagem na tela e o
#valor dessa variável. Explique em um comentário como o controle do laço vai
#funcionar.

ValorIncial = 100
while True:
    ValorEscolhido = int(input("Escolha um número:  "))
    if (ValorEscolhido <= ValorIncial):
        print("O valor escolhido não é aceitavel")
    else :    
        print("O valor escolhido é finalmente aceito")
        break


#2)Escreva um programa que gera um número aleatório entre 0 a 10, salvando
#esse número em uma variável. Solicite ao usuário que tente adivinhar o
#número que foi gerado aleatoriamente através da digitação via stdin. Caso o
#usuário acerte o número, exiba uma mensagem parabenizando-o e mostrando
#na mensagem o número adivinhado. Utilize a instrução “import” para que a
#biblioteca Random possa ser utilizada. O número aleatório deverá ser
#gerado através da função randint. Restrinja ao máximo de 5 tentativas por
#parte do usuário, caso não acerte, exiba mensagem e termine o programa.

#import random 
#NumeroAleatorio = random.randint(0,10)
CincoTentativa = 5
TentativaJogadas = 0
while CincoTentativa > TentativaJogadas:
    Chute = int(input(f"Seu chute (tentativa {TentativaJogadas}):   "))
    CincoTentativa = CincoTentativa - 1
    if Chute == NumeroAleatorio:
        print(f"Parabéns! Você acetou o número secreto {NumeroAleatorio}")
        break
    else: 
        print("Errado! Tente novamente.")
        TentativaJogadas + 1 == CincoTentativa
    if CincoTentativa == TentativaJogadas:
        print(f"Infelizmente você usou todas as suas chances. O número secreto era {NumeroAleatorio}")

#3) Escreva um programa que verifica se um endereço URL de um site foi digitado
#levando-se em conta o prefixo “www.” e o sufixo “.com.br”. Se o endereço foi
#digitado nesse formato corretamente, exiba mensagem, inclusive mostrando o
#endereço digitado, e finalize o programa. Se não digitou corretamente, exiba
#uma mensagem informando que a URL é inválida, mostre o endereço no
#formato errado e solicite ao usuário que digite novamente a URL do site. Uma
#forma de resolver esse problema é utilizar métodos da classe String do Python,
#como por exemplo: startswith() e endswith(). A documentação desses métodos
#pode ser encontrada em: https://docs.python.org/ptbr/3/library/stdtypes.html.dgs
#Enquanto a URL informada não estiver correta, o programa não deve ser
#finalizado.        
    
while True: 
    site = input("Insira um URL:    ")
    if site.startswith("www.")== True and site.endswith(".com.br") == True:
        print("Parabéns! Você acertou o site!")
        break
    else:
        print(f"Insira novamente o URL, {site}")