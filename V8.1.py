# @cikey fc86fd6b8ea7c6291f0829f791a2dfa4
# @sid 20251174010007
# @aid V8.1

def escreverFrases(nome_arquivo):
    #with: forma de gerenciar recursos, abre e fecha automaticamente    
    #as: Dá nome ao recurso aberto pelo with
    with open(nome_arquivo, "a") as f: 
        f.write(input("Digite a frase: ") + "\n")

def verFrases(nome_arquivo):
    with open(nome_arquivo, "r") as f:
        frases = f.readlines()
        for frase in frases:
            #Strip: Método de String que remove espaços em branco e quebras de linhas
            print(frase.strip())

nome_arquivo = "frase.txt"

print("_______________________")
print("1 - Adicionar Frase")
print("2 - Ver Frases")
print("3 - Sair")
pergunta = input("O que você deseja fazer? ")

while pergunta != "3":
    if pergunta == "1":
        escreverFrases(nome_arquivo)
    elif pergunta == "2":
        verFrases(nome_arquivo)
    else:
        print("Escolha inválida")
    pergunta = input("O que você deseja fazer? ")