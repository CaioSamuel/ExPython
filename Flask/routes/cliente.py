from flask import Blueprint

cliente_route = Blueprint('cliente', __name__)

'''
Rota de Clientes

    - /clientes/ [GET] - listar os clientes
    - /clientes/ [POST] - Inserir um cliente no servidor
    - /clientes/new [GET] - renderizar o formulário para criar um cliente
    - /clientes/<id> [GET] - obter os dados de um cliente
    - /cliente/<id>/edit [GET] - renderizar um formulário para editar um cliente
    - /clientes/<id>/update [PUT] - atualiza os dados do cliente
    - /clientes/<id>/delete [DELETE] - deleta um usuário
'''

@cliente_route.route('/')
def lista_clientes():
    pass


@cliente_route.route('/<int:cliente_id>')
def obter_clientes(cliente_id):
    pass