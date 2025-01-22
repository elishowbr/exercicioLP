def sal(horast, vlrHr, func):
    salbase = horast * vlrHr

    salbonus = 0
    if func == 'gerente':
        salbonus = salbase + 1000
    elif func == 'supervisor':
        salbonus = salbase + 500
    else:
        salbonus = salbase + 200

    saldesc = salbonus - 300

    salfinal = 0

    if saldesc > 5000:
        salfinal = saldesc - (saldesc * 0.27)
    elif (saldesc > 3000):
        salfinal = saldesc - (saldesc * 0.18)
    else:
        salfinal = saldesc - (saldesc * 0.11)

    return salfinal


salario = sal(160, 25, 'gerente')
print(f'O salário final é: {salario}')
