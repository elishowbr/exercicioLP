def verificarSePodeDirigir(idade):
    if idade >= 18:
        return 'Pode dirigir'
    else:
        return 'Não pode dirigir'

print(verificarSePodeDirigir(16))