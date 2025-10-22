# @cikey fc86fd6b8ea7c6291f0829f791a2dfa4
# @sid 20251174010007
# @aid V7.2

def advinhou_palavra(palavra, palpites):
    for letras in palpites:
        if letras not in palavra:
            return False
    return True
#begin_inputs
palavra = str(input("Digite a palavra secreta: "))
letras = str(input("Digite uma letra: "))
#end_inputs

print(advinhou_palavra(palavra, letras))