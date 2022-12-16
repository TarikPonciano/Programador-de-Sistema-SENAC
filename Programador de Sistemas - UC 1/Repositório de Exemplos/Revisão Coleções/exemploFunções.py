def calcular_pagamento(horas_trabalhadas,valor_hora):

    horas = float(horas_trabalhadas)
    taxa = float(valor_hora)

    if horas <= 40:
        salario = horas * taxa
    else:
        hora_extra = horas - 40
        salario = (40*taxa) + (hora_extra*(1.5*taxa))

    return salario

# str_hora = input("Escreva as horas trabalhadas: ")
# str_taxa = input("Escreva sua taxa de trabalho: ")


funcionarios = {"1": 0,
                "2": 0, 
                "3": 0}

str_horas = input("Insira as horas: ")
str_taxa = input("Insira a taxa de trabalho: ")

for i in funcionarios:

    total_salario = calcular_pagamento(str_horas, str_taxa)
    funcionarios[i] = total_salario

print(funcionarios)
