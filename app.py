# app.py
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'chave_secreta'

usuarios = [
    {'usuario': 'usuario1', 'senha': 'senha1'},
    {'usuario': 'usuario2', 'senha': 'senha2'}
]

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    usuario_digitado = request.form['usuario']
    senha_digitada = request.form['senha']

    for usuario in usuarios:
        if usuario['usuario'] == usuario_digitado and usuario['senha'] == senha_digitada:
            flash(f'Bem-vindo, {usuario["usuario"]}!', 'success')
            return redirect(url_for('index'))

    flash('Credenciais inválidas. Tente novamente.', 'error')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
