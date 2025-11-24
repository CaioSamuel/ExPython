candidato1 = 0
candidato2 = 0

for n in range(15):
    voto = int(input("Digite em quem você vai votar(1 ou 2): "))
    if voto == 1:
        candidato1 += 1
    elif voto == 2:
        candidato2 += 1
    else:
        print("voto inválido")

if candidato1 > candidato2:
    print(f"Candidato 1 ganhou com: {candidato1} votos")
elif candidato1 < candidato2:
    print(f"Candidato 2 ganhou com: {candidato2} votos")
else:
    print("ERROR!")