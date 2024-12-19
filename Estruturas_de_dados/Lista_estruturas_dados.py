import sys
sys.path.append('.')
sys.path.append('. ./custom_utils/utils')


from custom_utils import utils

'''1. Crie 03 variáveis do tipo tupla que contenham: os dias da semana, os meses
do ano, as estações do ano. Crie uma função, que tenha 1 parâmetro, que
imprima na tela os valores definidos em cada uma das tuplas.'''
diaTupla = ("domingo","segunda", "terça","quarta", "quinta", "sexta", "sábado")
mesesTupla = ("Janeiro","Fevereiro", "Março", "Abril","maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro")
estacoesTupla = ("verão","outono","inverno","primavera")
listaDasTuplas = [diaTupla, mesesTupla, estacoesTupla]

utils.imprimirtuplas(listaDasTuplas)

'''2. Crie 03 variáveis do tipo lista que contenham: os dias da semana, os meses
do ano, as estações do ano. Crie uma função, que tenha 1 parâmetro, que
imprima na tela os valores definidos em cada uma das listas.'''
diaLista = ["domingo","segunda", "terça","quarta", "quinta", "sexta", "sábado"]
mesesLista = ["Janeiro","Fevereiro", "Março", "Abril","maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]
estacoesLista =["verão","outono","inverno","primavera"]
tuplaDasListas = (diaLista, mesesLista, estacoesLista)

utils.ExibirListaComChaves(tuplaDasListas)

'''3. Exiba o tamanho e os elementos: primeiro, terceiro e último das estruturas de
dados criadas e inicializadas nas questões 1 e 2.'''

utils.exibirListas(listaDasTuplas)

'''4. Crie uma lista de compras de supermercado com 15 itens. Através de um
laço de repetição, exiba na tela, cada um dos itens dessa lista de compras.
Você deve decidir que tipo de estrutura de dados utilizar e imprimir, logo
abaixo da lista de compras, os motivos da sua decisão, ou seja, explique
porque utilizou tal estrutura de dados.'''
listaDeCompras = ["maçã", "banana", "pêssego", "abacaxi", "fruta do conde", "pera", "kiwi", "almôndegas", "baralho", "pacú", "melão", "mamão", "picanha", "fraldinha", "esponja"]
print(listaDeCompras)
#foi utilizado lista, porque uma lista de supermercado pode receber valores e ser alterada no futuro, 
# além de também ser uma estrutura de dados indexada (o que nos permite pegar o index de cada item)

'''5. Crie um programa que atualize a lista de compras da questão 4. O programa
deve solicitar ao usuário, através de um menu de opções, que tipo de
operação deseja efetuar sobre a lista de compras: incluir um novo item,
remover um item ou atualizar um item existente. Crie uma função para cada
tipo de operação permitida. Após o usuário informar uma das opções válida
do menu, o programa deve solicitar que o usuário digite o nome do
produto\item para que a função correta seja chamada e a alteração da lista
de compras possa ser feita. Implemente uma forma de encerrar o programa
através da interação do usuário'''

def menu():
    while True:
        print("\nMenu de opções:")
        print("1. Incluir um novo item")
        print("2. Remover um item")
        print("3. Atualizar um item existente")
        print("4. Exibir lista de compras")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            utils.incluir_item(listaDeCompras)
        elif opcao == "2":
            utils.remover_item(listaDeCompras)
        elif opcao == "3":
            utils.atualizar_item(listaDeCompras)
        elif opcao == "4":
            print("\nLista de Compras:")
            utils.exibirListas(listaDeCompras)
        elif opcao == "5":
            print("Encerrando o programa. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")


'''6. Crie uma estrutura de dados que armazene o nome das linguagens de
programação: C, C++, JavaScript, Java, Lua e Python. Implemente um
programa que solicite ao usuário que tente adivinhar quais linguagens de
programação constam em uma lista oculta de nomes, informando, para tanto,
nomes de linguagens de programação. Exiba mensagem na tela para o
usuário informando se a linguagem consta ou não na lista oculta. A
funcionalidade de procurar em uma lista oculta de nomes deverá ser
implementada através de função.'''
linguagensProgramacao = ("C", "C++", "JavaScript", "Java", "Lua", "Python")
def main():
    while True:
        print("Tente adivinhar as linguagens de programação salvas numa tupla.")
        tentativaUser = input("Insira alguma linguagem: \n").title()
        verificarLista(tentativaUser)
        break

def verificarLista(tentativa):
    if tentativa in linguagensProgramacao:
        print(f"Você acertou! {tentativa} está dentro da tupla original!")
    else:
        print("Bah, tu errou meu!")
main()

'''7. Crie um programa que possa marcar uma consulta médica. Utilize uma
estrutura de dados para armazenar o nome dos médicos que atendem na
clínica. Solicite ao usuário que informe com qual profissional deseja marcar
uma consulta médica. Implemente funções que possam: imprimir na tela o
nome dos profissionais, procurar na lista de profissionais o nome informado,
exibir na tela mensagem de que a consulta foi marcada com sucesso. Em
caso de falha, exibir mensagem na tela informando o usuário do ocorrido.'''
nomeMedicos = ("Dr. Carlos Henrique", "Dr. Pedro Gnoatto", "Dr. Branco Preto")
utils.principal(nomeMedicos)