# Dados de exemplo de usuários (em um ambiente de produção, você usaria um banco de dados)
usuarios = {
    'usuario1': {'senha': 'senha1', 'nome': 'Usuário 1'},
    'usuario2': {'senha': 'senha2', 'nome': 'Usuário 2'}
}

# Função de login
def fazer_login(usuario, senha):
    # Verifica se o usuário existe e a senha está correta
    if usuario in usuarios and usuarios[usuario]['senha'] == senha:
        return True, usuarios[usuario]['nome']
    else:
        return False, None

# Exemplo de uso
usuario_input = input('Digite seu nome de usuário: ')
senha_input = input('Digite sua senha: ')

autenticado, nome_usuario = fazer_login(usuario_input, senha_input)

if autenticado:
    print(f'Bem-vindo, {nome_usuario}!')
else:
    print('Usuário ou senha incorretos.')
