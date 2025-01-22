def tentarLogin(senha):
    tentativas = 0
    senhaCorreta = '12345'

    while tentativas < 3:
        if senha == senhaCorreta:
            return 'Login efetuado com sucesso!'
        tentativas += 1

    return 'Tentativas de login excedidas.'

print(tentarLogin('123'))
