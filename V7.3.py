# @cikey fc86fd6b8ea7c6291f0829f791a2dfa4
# @sid 20251174010007
# @aid V7.3
import random

numMax = 25
listaNumsSorteados = []

def sorteio():
    while len(listaNumsSorteados) < numMax:
        numSorteado = random.randint(1, 40)
        if numSorteado not in listaNumsSorteados:
            listaNumsSorteados.append(numSorteado)

sorteio()
print(sorted(listaNumsSorteados))