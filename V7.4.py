# @cikey fc86fd6b8ea7c6291f0829f791a2dfa4
# @sid 20251174010007
# @aid V7.4

contatos = []

def adicionar_contato(nome, telefone):
    contatos.append({'nome': nome, 'telefone': telefone})

def consultar_telefone(nome):
    for contato in contatos:
        if contato['nome'] == nome:
            return contato['telefone']
    return "Contato não encontrado."

adicionar_contato("Russell Harrison", "(940) 211-3349")
print(consultar_telefone("Russell Harrison"))