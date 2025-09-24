id1 = int(input("Digite a idade: "))
id2 = int(input("Digite a idade: "))
id3 = int(input("Digite a idade: "))
id4 = int(input("Digite a idade: "))
id5 = int(input("Digite a idade: "))
id6 = int(input("Digite a idade: "))
id7 = int(input("Digite a idade: "))
id8 = int(input("Digite a idade: "))
id9 = int(input("Digite a idade: "))
id10 = int(input("Digite a idade: "))

lista = [id1, id2, id3, id4, id5, id6, id7, id8, id9, id10]
maiores = 0
for idade in lista:
    if idade >= 18:
        maiores += 1