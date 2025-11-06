import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
nome_arquivo = os.path.join(BASE_DIR, "listaEstoque.txt")
arquivo_funcionarios = os.path.join(BASE_DIR, "listaFuncionario.txt")

#funções

def adicionarEstoque(produto, prUnit, qtd):
    try:
        with open(nome_arquivo, "a", encoding="utf-8") as e:
            e.write("{}; {}; {}\n".format(produto, prUnit, qtd))
        print(f"Estoque salvo em: {nome_arquivo}")
    except Exception as exc:
        print("Erro ao salvar estoque:", exc)

def lerEstoque(nome_arquivo):
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as e:
            for linha in e:
                print(linha.strip())
    except FileNotFoundError:
        print("Arquivo de estoque não encontrado.")

# corrigido para receber somente o caminho do arquivo
def adicionarFuncionarios(nome, idade, funcao):
    try:
        with open(arquivo_funcionarios, "a", encoding="utf-8") as f:
            f.write("{}; {}; {}\n".format(nome, idade, funcao))
        print(f"Funcionário salvo em: {arquivo_funcionarios}")
    except Exception as exc:
        print("Erro ao salvar funcionário:", exc)

# corrigido para receber somente o caminho do arquivo
def verFuncionarios(arquivo):
    try:
        with open(arquivo, "r", encoding="utf-8") as f:
            for linha in f:
                print(linha.strip())
    except FileNotFoundError:
        print("Arquivo de funcionários não encontrado.")

#funcionamento do sistema (menu dentro do loop)
while True:
    print("_______________________")
    print("1 - Adicionar Estoque")
    print("2 - Ver Estoque")
    print("3 - Adicionar Funcionário")
    print("4 - Ver Funcionários")
    print("5 - Sair")
    pergunta = input("O que você deseja fazer? ").strip()

    if pergunta == "1":
        produto = input("Digite o nome do produto: ")
        prUnit = input("Digite o preço unitário: ")
        qtd = input("Digite a quantidade de produtos no estoque: ")
        adicionarEstoque(produto, prUnit, qtd)
    elif pergunta == "2":
        lerEstoque(nome_arquivo)
    elif pergunta == "3":
        nome = input("Digite o nome do funcionário: ")
        idade = input("Digite a idade do funcionário: ")
        funcao = input("Digite a função do funcionário: ")
        adicionarFuncionarios(nome, idade, funcao)
    elif pergunta == "4":
        verFuncionarios(arquivo_funcionarios)
    elif pergunta == "5":
        break
    else:
        print("Escolha inválida")