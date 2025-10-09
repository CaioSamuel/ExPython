# @cikey fc86fd6b8ea7c6291f0829f791a2dfa4
# @sid 20251174010007
# @aid V6.5
import random

num = random.randint(1, 100)

palp = int(input("Adivinhe o número: "))

while palp != num:
    if palp < num:
        print("O número é maior")
    else:
        print("O número é menor")
    palp = int(input("Tente novamente: "))

print("Parabéns! Você acertou, o número era: {}".format(num))