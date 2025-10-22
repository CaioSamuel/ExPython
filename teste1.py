from string import ascii_lowercase

#begin_inputs
letras = str(input("Digite uma letra: "))
#end_inputs

def letras_disponíveis(palpites):
    # Converte ascii_lowercase em conjunto e remove as letras já palpitadas
    return sorted(list(set(ascii_lowercase) - set(palpites)))

# Chamada da função e impressão do resultado
print(letras_disponíveis(letras))
