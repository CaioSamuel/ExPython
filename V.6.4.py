# @cikey fc86fd6b8ea7c6291f0829f791a2dfa4
# @sid 20251174010007
# @aid V6.4
import random

#begin_inputs

#end_inputs

dado1 = random.randint(2, 12)
dado2 = random.randint(2, 12)

print("Dado 1: {} \nDado 2: {}".format(dado1, dado2))

if dado1 or dado2 == 7 or 11:
    print("Você ganhou!")
elif dado1 or dado2 == 2 or 3 or 12:
    print("Craps!")
elif dado1 or dado2 == 4 or 5 or 6 or 8 or 9 or 10:
    print("Seu ponto")