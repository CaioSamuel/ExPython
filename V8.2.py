# @cikey fc86fd6b8ea7c6291f0829f791a2dfa4
# @sid 20251174010007
# @aid V8.2

file = "frase.txt"

with open(file, "r") as f:
    linhas = f.readlines()
    numLinhas = len(linhas)
    print(numLinhas, "linhas")