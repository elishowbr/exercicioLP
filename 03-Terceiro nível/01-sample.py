def calcularDesconto(preco):
    return preco - (preco * 0.15)


precoFinal = calcularDesconto(100)
print(f'Preço com desconto: ${precoFinal}')
