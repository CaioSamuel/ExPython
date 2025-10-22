# @cikey fc86fd6b8ea7c6291f0829f791a2dfa4
# @sid 20251174010007
# @aid V7.1

from string import ascii_lowercase

#begin_inputs
letras = str(input("Digite uma letra: "))
#end_inputs

def letras_disponíveis(palpites):
    return sorted(list(set(ascii_lowercase) - set(palpites)))

print(letras_disponíveis(letras))