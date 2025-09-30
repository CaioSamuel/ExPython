# @cikey fc86fd6b8ea7c6291f0829f791a2dfa4
# @sid 20251174010007
# @aid V5.1

soma = 0
#begin_inputs
for p in range(7):
    peso = int(input("Qual é o peso?: "))
    soma += peso
#end_inputs

if soma > 500:
    print("Peso excedido")

print(soma)