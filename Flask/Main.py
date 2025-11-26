from flask import Flask, url_for, render_template, request, redirect


arquivo = "dados.txt"

#Inicialização
app = Flask(__name__)

#Rotas
@app.route('/')
def gerencia_usuarios():
    titulo = "Gestão de Usuários"
    usuarios = [
        {"nome": "Guilherme", "membro_ativo": True},
        {"nome": "João", "membro_ativo": False},
        {"nome": "Maria", "membro_ativo": False},
    ]
    return render_template('index.html', titulo=titulo, usuarios=usuarios)

@app.route('/sobre')
def pagina_sobre():
    return 'Página Sobre'

@app.route('/formulario')
def formulario():
    return render_template('formulario.html')

@app.route('/enviar', methods=['POST'])
def enviar():
    nome = request.form['nome']
    email = request.form['email']

    try: 
        with open(arquivo, 'a') as f:
            f.write(f"Nome: {nome}; Email: {email} \n")
        print(f"Dados salvo em: {arquivo}")
    except Exception as exc:
        print("Erro ao salvar estoque:", exc)

    return f"Dados recebidos! Nome: {nome}, Email: {email}"

#Execução
app.run(debug = True)