from flask import Blueprint, render_template

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
    ''' listar os clientes'''
    return render_template('lista_clientes.html')


@cliente_route.route('/', methods=['POST'])
def inserir_clientes():
    ''' Inserir os dados do cliente '''
    pass


@cliente_route.route('/new', methods=['GET'])
def form_cliente():
    ''' Formulário para cadastrar um cliente'''
    return render_template('form_cliente.html')


@cliente_route.route('/<int:cliente_id>')
def detalhe_cliente(cliente_id):
    ''' exibir detalhes de um cliente  '''
    return render_template('detalhe_cliente.html')


@cliente_route.route('/<int:cliente_id>/edit')
def form_edit_cliente(cliente_id):
    ''' formulario para editar um cliente  '''
    return render_template('form_edit_cliente.html')


@cliente_route.route('/<int:cliente_id>/update', methods=['PUT'])
def atualizar_cliente(cliente_id):
    ''' atualizar informações do cliente '''
    pass


@cliente_route.route('/<int:cliente_id>/delete', methods=['DELETE'])
def deletar_cliente(cliente_id):
    ''' deletar informações do cliente '''
    pass