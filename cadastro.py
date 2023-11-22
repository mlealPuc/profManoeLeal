# funcao para validar o cadastro de um novo usuario

def cadastrar_usuario(usuario, senha):
    # Verifica se o usuário existe e a senha está correta
    if usuario in usuarios:
        return False
    else:
        usuarios[usuario] = {'senha': senha}
        return True


def valida_senha(senha):
    if len(senha) < 8:
        return False
    else
        return True