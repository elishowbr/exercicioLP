def calcularSalarioFuncionario(horasTrabalhadas, valorHora, cargo):
    salarioBase = horasTrabalhadas * valorHora

    salarioComBonus = 0
    if cargo == 'gerente':
        salarioComBonus = salarioBase + 1000
    elif cargo == 'supervisor':
        salarioComBonus = salarioBase + 500
    else:
        salarioComBonus = salarioBase + 200

    salarioComDesconto = salarioComBonus - 300

    salarioFinal = 0

    if salarioComDesconto > 5000:
        salarioFinal = salarioComDesconto - (salarioComDesconto * 0.27)
    elif (salarioComDesconto > 3000):
        salarioFinal = salarioComDesconto - (salarioComDesconto * 0.18)
    else :
        salarioFinal = salarioComDesconto - (salarioComDesconto * 0.11)

    return salarioFinal


salario = calcularSalarioFuncionario(160, 25, 'gerente')
print(f'O salário final é: ${salario}')
