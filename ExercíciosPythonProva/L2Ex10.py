temps = []

def pedirTemperatura(mes, temp):
    temps.append(f"{mes}:{temp}")

'''for n in range(12):'''
mes = input("Digite o mês: ")
temp = int(input("Digite a temperatura: "))
pedirTemperatura(mes, temp)

print(temps)