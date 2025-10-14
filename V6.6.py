# @cikey fc86fd6b8ea7c6291f0829f791a2dfa4
# @sid 20251174010007
# @aid V6.6
import random

num = random.randint(1, 100)
tent_total = 3
tent = 0

print("Tente adivinhar o numero entre 1 e 100. Voce tem 3 tentativas.")

while tent < tent_total:
    palp = int(input(f"Tentativa {tent + 1}: "))

    tent += 1

    if palp == num:
        print(f"Parabens! Voce acertou, o numero era: {num}")
        break
    elif palp < num:
        print("O numero e maior.")
    else:
        print("O numero e menor.")

    if tent == tent_total:
        print(f"Suas tentativas acabaram. O numero era: {num}")

