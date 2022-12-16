# def hello(meu_nome, minha_idade):
    
#     print("Olá,", meu_nome)
#     print("Sua idade é", minha_idade)


# nome = input("Digite seu nome: ")
# idade = input("Digite sua idade: ")

# hello(nome, idade)


def calcular_pagamento(qtd_horas, valor_hora):
    horas = float(qtd_horas)
    taxa = float(valor_hora)

    if horas <= 40:
        salario = horas * taxa
    else:
        h_ext = horas - 40
        salario = 40*taxa + h_ext*(1.5*taxa)

    return salario

horasTrabalhadas = input("Quantas horas você trabalhou? ")
valorDaHora = input("Quanto custa sua hora? ")

salarioRecebido = calcular_pagamento(horasTrabalhadas,valorDaHora)

print(f"Você recebeu R${salarioRecebido}")



