nomes = []
idades = []

for n in range(5):
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    nomes.append(nome)
    idades.append(idade)

menorIdade = idades.index(min(idades))
maiorIdade = idades.index(max(idades))

print(f"menor idade: {nomes[menorIdade]}, {idades[menorIdade]} anos")
print(f"maior idade: {nomes[maiorIdade]}, {idades[maiorIdade]} anos")
print(f"Média das idades: {sum(idades) / len(idades)}")