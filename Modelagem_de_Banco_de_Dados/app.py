from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    # Aqui você pode adicionar a lógica de login
    return render_template('login.html')  # Renderiza o template de login

if __name__ == '__main__':
    app.run(debug=True)
