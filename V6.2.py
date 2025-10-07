# @cikey fc86fd6b8ea7c6291f0829f791a2dfa4
# @sid 20251174010007
# @aid V6.2

#begin_inputs
n = int(input("digite um numero: "))
#end_inputs

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end='   ')
    print()