# @cikey fc86fd6b8ea7c6291f0829f791a2dfa4
# @sid 20251174010007
# @aid V6.4
import random

#begin_inputs

#end_inputs

dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)
soma = dado1 + dado2

if soma in (7, 11):
    print("Voce ganhou!")
elif soma in (2, 3, 12):
    print("Voce perdeu!")
else:
    print()