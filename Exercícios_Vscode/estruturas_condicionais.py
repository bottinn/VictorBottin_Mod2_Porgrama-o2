#1) Crie 2 variáveis com dois valores numéricos inteiros informados pelo
#suário, caso o valor do primeiro número for maior do que o segundo,
#exiba em tela uma mensagem de acordo, caso contrário, exiba em tela
#uma mensagem dizendo que o primeiro valor digitado é menor que o
#segundo. Os números informados pelo usuário devem aparecer em
#ambas as mensagens.

print("por favor insira o primeiro valor maior que o segundo!")
numero1 = int(input("Insira um númeor inteiro:  "))
numero2 = int(input("Insira um númeor inteiro:  "))
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
print("Gostaria de agendar um consulta?")
print(("Se sim, digite 1"))
print(("Caso contrário, digite 2"))
escolha = print(input("Digite aqui:   "))
if escolha == 1:
    print("Com qual médico deseja fazer a sua consulta?")
elif escolha == 2:
    print("Obrigado por ligar!")
    
