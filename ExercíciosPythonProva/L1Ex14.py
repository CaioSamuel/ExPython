viagens = 0
total = 0

pergunta = input(":")

while pergunta != "0":
    if pergunta == "1":
        pergunta2 = input("Você fez alguma viagem?: ")
        if pergunta2 == 's':
            viagens += 1
            valor = int(input("Valor da viagem: "))
            total += valor
        elif pergunta2 == 'n':
            break
    else:
        print("ERROR!")

print(f"Viagens: {viagens}")
print(f"Total: {total}")