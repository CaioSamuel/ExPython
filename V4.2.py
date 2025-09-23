# @cikey fc86fd6b8ea7c6291f0829f791a2dfa4
# @sid 20251174010007
# @aid V4.2

#begin_inputs
idades = []
for i in range(10):
    idade = int(input(f"Digite a idade da pessoa {i+1}: "))
    idades.append(idade)
#end_inputs

maiores = 0
for idade in idades:
    if idade >= 18:
        maiores += 1

print(maiores)
