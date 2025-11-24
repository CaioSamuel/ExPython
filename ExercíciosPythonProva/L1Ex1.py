precoProd = int(input("Digite o preço do produto: "))
valorDado = int(input("Digite o valor dado: "))

if valorDado < precoProd:
    print(f"Faltou {precoProd - valorDado} reais")
else:
    print(f"O troco é {valorDado - precoProd} reais")