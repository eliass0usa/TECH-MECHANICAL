from flask import Flask, render_template, request, redirect, url_for
from connection import criar_usuario, ler_usuarios, atualizar_senha, deletar_usuario

app = Flask(__name__, static_url_path = '/static')

# ROTA PARA A PAGINA INICIAL
@app.route('/')
def index():
    return render_template('index.html')

# CADASTRO DE USUÁRIO
@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    nome = request.form['nome']
    email = request.form['email']
    senha = request.form['senha']
    criar_usuario(nome, email, senha)
    return redirect(url_for('index'))

# LISTAR USUÁRIOS
@app.route('/usuarios')
def listar_usuarios():
    usuarios = ler_usuarios()
    return render_template('usuarios.html', usuarios=usuarios)

# LIDAR COM ATUALIZAÇÃO DE SENHA
@app.route('/atualizar_senha', methods=['POST'])
def atualizar_senha_usuario():
    email = request.form['email']
    nova_senha = request.form['nova_senha']
    atualizar_senha(email, nova_senha)
    return redirect(url_for('listar_usuarios'))

# EXCLUSÃO DE USUARIO
@app.route('/deletar_usuario', methods=['POST'])
def deletar_usuario_route():
    email = request.form['email']
    deletar_usuario(email)
    return redirect(url_for('listar_usuarios'))

if __name__ == '__main__':
    app.run(debug=True)
