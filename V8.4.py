# @cikey fc86fd6b8ea7c6291f0829f791a2dfa4
# @sid 20251174010007
# @aid V8.4

nome_arquivo = "cpf.txt"

def adicionarCPF(cpf, nome):
    with open(nome_arquivo, "a") as f:
        f.write("{}; {}\n".format(cpf, nome))

def CPFs(nome_arquivo):
    with open(nome_arquivo, "r") as f:
        cpfs = f.readlines()
        for cpf in cpfs:
            #Strip: Método de String que remove espaços em branco e quebras de linhas
            print(cpf.strip())

print("_______________________")
print("1 - Adicionar CPFs")
print("2 - Ver CPFs")
print("3 - Sair")
pergunta = input("O que você deseja fazer? ")

while pergunta != "3":
    if pergunta == "1":
        cpf = input("Digite o CPF: ")
        nome = input("Digite o nome: ")
        adicionarCPF(cpf, nome)
    elif pergunta == "2":
        CPFs(nome_arquivo)
    else:
        print("Escolha inválida")
    pergunta = input("O que você deseja fazer? ")
close()