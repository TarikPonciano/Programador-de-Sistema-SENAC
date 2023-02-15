# Faça um dicionário que contenha os dados de uma pessoa, são os
# seguintes dados: (Preencha os dados iniciais como preferir)
# - Nome
# - Ultimo Nome
# - Idade
# - Curso
# - Endereço
# a) Imprima o dicionário completo
# b) Imprima cada um dos 5 itens separadamente
# c) Exclua a chave CURSO do dicionário
# d) Altere o ULTIMO NOME para Lopes
# e) Imprima novamente o dicionário completo
# f) Imprima apenas o endereço
# g) Crie uma cópia do dicionário e altere Nome e Idade
# h) Imprima o segundo dicionário completo

pessoa = {"Nome":"Mariano", "Último Nome":"Sérgio", "Idade": 25, "Curso": "Programador de Sistemas", 
"Endereço": "Caucaia"}

print(pessoa.items())

print(pessoa["Nome"])
print(pessoa["Último Nome"])
print(pessoa["Idade"])
print(pessoa["Curso"])
print(pessoa["Endereço"])

del(pessoa["Curso"])

pessoa["Último Nome"] = "Lopes"

print(pessoa.items())

print(pessoa["Endereço"])

pessoa2 = pessoa.copy()
pessoa2["Nome"] = "Junim"
pessoa2["Idade"] = 18

print(pessoa2.items())