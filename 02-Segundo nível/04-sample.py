def ttlg(pswrd):
    rstnt = 0
    chck = '12345'

    while rstnt < 3:
        if pswrd == chck:
            return 'Login efetuado com sucesso!'
        rstnt += 1

    return 'Tentativas de login excedidas.'

print(ttlg('123'))
