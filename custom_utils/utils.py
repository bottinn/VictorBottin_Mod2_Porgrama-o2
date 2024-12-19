#1
def imprimirtuplas(listaTupla):
    for i in listaTupla:
        print(f"{i}")

#2
def ExibirListaComChaves(listaLista):
    for i in listaLista:
        print(f"{i}")
 
#3
def exibirListas(listaTupla): #lista das tuplas contem 3 tuplas com diferentes dados
    for i in listaTupla:
        print(f"Tamanho de {i}: {len(i)}")
        print(f"Primeiro elemento: {i[0]}")
        print(f"Terceiro elemento: {i[2]}")
        print(f"Último elemento: {i[-1]}")
        print("=-"*30)
        
#5
def incluir_item(listaDeCompras):
    item = input("Digite o item a ser incluído:")
    listaDeCompras.append(item)
    print(f"Item'{item}' incluído com sucesso")

def remover_item(listaDeCompras):
    item = input("Insira o item a ser removido: ")
    if item in listaDeCompras:
        listaDeCompras.remove(item)
        print(f"Item '{item}' removido da lista")
    else:
        print(f"Item '{item}' não encontrado na lista") 

def atualizar_item(listaDeCompras):
    item_antigo = input("Insira o item que deseja trocar")
    if item_antigo in listaDeCompras:
        novo_item = input("Insira o novo item ")
        index = listaDeCompras.index(item_antigo)
        listaDeCompras[index] = novo_item
        print(f"Item '{item_antigo}' alterado para '{novo_item}'")
    else:
        print("Item não econtrado na lista")

#7
def principal(nomeMedicos):
    while True:
        exibirMedicos(nomeMedicos)
        tentativaMedico = input("")
        if (tentativaMedico.isdigit()):
            print("O nome deve conter letras.")
        elif (tentativaMedico in nomeMedicos):
            print(f"O médico {tentativaMedico} foi encontrado com sucesso na tupla mãe! Consulta marcada.")
            break
        else:
            print("Digite um nome válido.")

def exibirMedicos(nomes):
    print(f'''{"-="*30}
            {"LISTA DOS MÉDICOS":^{15}}
{"-="*30}
Deseja marcar uma consulta? Os médicos disponíveis são:
{nomes}
Por favor, insira o nome do médico que deseja ver: ''')