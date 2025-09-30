# @cikey fc86fd6b8ea7c6291f0829f791a2dfa4
# @sid 20251174010007
# @aid V4.2

#begin_inputs
maiores = 0
for n in range(10):
    idade = int(input("Digite a idade da pessoa: "))
#end_inputs
    if idade > 18:
        maiores += 1
print(maiores)
