numeros = []

for n in range(10):
    num = int(input("Digite o número: "))
    if num % 2 == 0:
        numeros.append(num)

print(numeros)