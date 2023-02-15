pessoa = {"Idade": 20,"Nome": 'João', "Nacionalidade":'Brasileiro'}

print(pessoa.items())

del(pessoa["Idade"])

print(pessoa.items())

pessoa2 = pessoa.copy()

print(pessoa.items())
print(pessoa2.items())

pessoa2["Idade"] = 30

print(pessoa.items())
print(pessoa2.items())