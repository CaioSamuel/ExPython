# @cikey fc86fd6b8ea7c6291f0829f791a2dfa4
# @sid 20251174010007
# @aid V8.5

contatos = "contatos.txt"

def adicionar_contato(nome, telefone):
    with open(contatos, "a") as f:
        f.write(f'{nome},{telefone}')

def consultar_contato(contatos):
    with open(contatos, "r") as f:
        f.readlines()
        for contato in contatos:
            print(contato.strip())

print("_______________________")
print("1 - Adicionar Contato")
print("2 - Ver Contatos")
print("3 - Sair")
pergunta = input("O que você deseja fazer? ")

while pergunta != "3":
    if pergunta == "1":
        nome = input("Digite o nome: ")
        telefone = input("Digite o telefone: ")
        adicionar_contato(nome, telefone)
    elif pergunta == "2":
        consultar_contato(contatos)
    else:
        print("Escolha inválida")
    pergunta = input("O que você deseja fazer? ")