# @cikey fc86fd6b8ea7c6291f0829f791a2dfa4
# @sid 20251174010007
# @aid V5.1


#begin_inputs
#end_inputs
soma = 0
for p in range(7):
    peso = int(input("qual e o peso?: "))
    soma += peso
if soma > 500:
    print("Peso excedido")