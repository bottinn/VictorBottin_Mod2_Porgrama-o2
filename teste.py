import re

# Solicitar ao usuário que insira a senha
senha = input("Digite sua senha: ")

# Definir os caracteres especiais permitidos
caracteres_especiais = r'[#@!%&*]'

# Verificar se a senha contém pelo menos um caractere especial
if re.search(caracteres_especiais, senha):
    print("Senha válida! Sua senha é:", senha)
else:
    print("A senha deve conter pelo menos um caractere especial (#, @, !, %, &, *).")
