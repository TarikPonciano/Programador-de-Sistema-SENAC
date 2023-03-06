def calcular_pagamento(qtd_horas, valor_hora):
    horas = float(qtd_horas)
    taxa = float(valor_hora)

    if horas <= 40:
        salario = horas * taxa
    else:
        horas_extras = horas-40
        salario = 40*taxa + (horas_extras*1.5*taxa)
    
    return salario

# horasTrabalhadas = input("Digite quantas horas trabalhou: ")
# taxaDeTrabalho = input("Digite o quanto ganha por hora: ")

# salarioFinal = calcular_pagamento(horasTrabalhadas,taxaDeTrabalho)

# print("Seu salário foi R$", salarioFinal)

print("Funcionário 1", calcular_pagamento(20,20))
print("Funcionario 2", calcular_pagamento(100,20))
print("Funcionario 3", calcular_pagamento(20,40))

print(f'''
Funcionário 1 - {calcular_pagamento(20,20)}
Funcionário 2 - {calcular_pagamento(100,20)}
Funcionário 3 - {calcular_pagamento(20,40)}
''')

