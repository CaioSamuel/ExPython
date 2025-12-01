import os

# Corrigir nome do arquivo para corresponder ao arquivo existente
arquivo_estoque = "listaEstoque.txt"
arquivo_funcionarios = "listaFuncionario.txt"  # removido o 's' extra

# Usar caminho absoluto para garantir que está salvando no lugar correto
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
arquivo_estoque = os.path.join(BASE_DIR, arquivo_estoque)
arquivo_funcionarios = os.path.join(BASE_DIR, arquivo_funcionarios)

#funções

def adicionarEstoque(produto, prUnit, qtd):
    try:
        with open(arquivo_estoque, "a", encoding="utf-8") as e:
            e.write("{}; {}; {}\n".format(produto, prUnit, qtd))
        print(f"Dados salvo em: {arquivo_estoque}")
    except Exception as exc:
        print("Erro ao salvar estoque:", exc)
def lerEstoque(arquivo_estoque):
    try:
        with open(arquivo_estoque, "r", encoding="utf-8") as e:
            for linha in e:
                print(linha.strip())
    except FileNotFoundError:
        print("Arquivo de estoque não encontrado.")

# corrigido para receber somente o caminho do arquivo
def adicionarFuncionarios(nome, idade, funcao):
    try:
        with open(arquivo_funcionarios, "a", encoding="utf-8") as f:
            f.write("{}; {}; {}\n".format(nome, idade, funcao))
            f.flush()  # força escrita no disco
            os.fsync(f.fileno())  # garante que OS salvou no disco
        print(f"Funcionário salvo em: {arquivo_funcionarios}")
        print("Dados salvos com sucesso!")
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
def buscarProduto(arquivo_estoque):
    nome_busca = input("Digite o nome do produto: ").strip().lower()
    encontrado = False
    try:
        with open(arquivo_estoque, "r", encoding="utf-8") as e:
            for linha in e:
                dados = linha.split(";")
                nome_produto = dados[0].strip().lower()
                if nome_produto == nome_busca:
                    print(f"Nome: {dados[0].strip()}")
                    print(f"Valor: R$ {dados[1].strip()}")
                    print(f"Quantidade: {dados[2].strip()}")
                    encontrado = True
                    break
        if not encontrado:
            print("Produto não encontrado!")
    except FileNotFoundError:
        print("Arquivo não encontrado!")
<<<<<<< Updated upstream
<<<<<<< Updated upstream
def buscarFuncionario(arquivo_funcionarios):
    nome_busca = input("Digite o nome do funcionário: ").strip().lower()
    encontrado = False
    try:
        with open(arquivo_funcionarios, "r", encoding="utf-8") as e:
            for linha in e:
                dados = linha.split(";")
                nome_funcionario = dados[0].strip().lower()
                if nome_funcionario == nome_busca:
                    print(f"Nome: {dados[0].strip()}")
                    print(f"Idade: {dados[1].strip()} anos")
                    print(f"Função: {dados[2].strip()}")
                    encontrado = True
                    break
        if not encontrado:
            print("Funcionário não encontrado!")
    except FileNotFoundError:
        print("Arquivo não encontrado!")

=======

    
>>>>>>> Stashed changes
=======

    
>>>>>>> Stashed changes
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
        print("\n")
        print("________________")
        print("\n")
        produto = input("Digite o nome do produto: ")
        prUnit = input("Digite o preço unitário: ")
        qtd = input("Digite a quantidade de produtos no estoque: ")
        adicionarEstoque(produto, prUnit, qtd)
        print("________________")

    elif pergunta == "2":
        print("\n")
        print("____________")
        print("\n")
        print("1 - Ver produto específico")
        print("2 - Ver lista de produtos completa")
        pergunta2 = input("Digite o que você deseja fazer: ")
        if pergunta2 == "1":
            buscarProduto(arquivo_estoque)
        elif pergunta2 == "2":
            lerEstoque(arquivo_estoque)
        print("____________")

    elif pergunta == "3":
        print("\n")
        print("_________________")
        print("\n")
        nome = input("Digite o nome do funcionário: ")
        idade = input("Digite a idade do funcionário: ")
        funcao = input("Digite a função do funcionário: ")
        adicionarFuncionarios(nome, idade, funcao)
        print("_________________")

    elif pergunta == "4":
        print("\n")
        print("__________")
        print("1 - Ver funcionário específico")
        print("2 - Ver lista de funcionários completa")
        pergunta3 = input("Digite o que você deseja fazer: ")
        if pergunta3 == "1":
            buscarFuncionario(arquivo_funcionarios)
        elif pergunta3 == "2":
            verFuncionarios(arquivo_funcionarios)
        print("__________")

    elif pergunta == "5":
        break

    else:
        print("Escolha inválida")