# @cikey fc86fd6b8ea7c6291f0829f791a2dfa4
# @sid 20251174010007
# @aid V8.1

def escreverFrases(f):
    f.write(input("Digite a frase: "))

def verFrases(f):
    frases = f.readlines()
    print(frases)

nome_arquivo = "frase.txt"

f = open(nome_arquivo, mode="r+")

print("_________________________")
print("1 - Adicionar Frase")
print("2 - Ver Frases")
print("3 - Sair")
pergunta = input("O que você deseja fazer? ")

while pergunta != "3":
    if pergunta == "1":
        escreverFrases()
    elif pergunta == "2":
        verFrases()
    else:
        print("Escolha inválida")