import mysql.connector

def conectar():
    conexao = mysql.connector.connect(
        host='localhost',
        username='root',
        password='123456',
        database='tech-mechanical'
    )
    return conexao

def criar_usuario(nome, email, senha):
    conexao = conectar()
    cursor = conexao.cursor()
    sql = 'INSERT INTO usuario (nome, email, senha) VALUES (%s, %s, %s)'
    valores = (nome, email, senha)
    cursor.execute(sql, valores)
    conexao.commit()
    conexao.close()

def ler_usuarios():
    conexao = conectar()
    cursor = conexao.cursor()
    sql = 'SELECT * FROM usuario'
    cursor.execute(sql)
    usuarios = cursor.fetchall()
    conexao.close()
    return usuarios

def atualizar_senha(email, nova_senha):
    conexao = conectar()
    cursor = conexao.cursor()
    sql = 'UPDATE usuario SET senha = %s WHERE email = %s'
    valores = (nova_senha, email)
    cursor.execute(sql, valores)
    conexao.commit()
    conexao.close()

def deletar_usuario(email):
    conexao = conectar()
    cursor = conexao.cursor()
    sql = 'DELETE FROM usuario WHERE email = %s'
    valores = (email,)
    cursor.execute(sql, valores)
    conexao.commit()
    conexao.close()
