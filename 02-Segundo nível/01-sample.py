def dsc(p):
    return p - (p * 0.15)


abcde = dsc(100)
print(f'Preço com desconto: ', abcde)
print(f'Preço com desconto: R${abcde}')
