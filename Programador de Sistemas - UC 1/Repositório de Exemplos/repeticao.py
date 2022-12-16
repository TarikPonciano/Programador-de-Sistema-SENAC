nomes = ["Pedro", "João", "Letícia", "Saulo", "Samuel"]
notas = [5, 7 , 8, 6.5, 9]

print(nomes)

for n in nomes:
    print(n)

for i in range(len(nomes)):
    print("Aluno:",nomes[i],"Notas:",notas[i])

print("A lista é:",nomes)
print("O tamanho da lista:", len(nomes))
x = range(len(nomes))
print("O range é:",x)

range(1,5) #[1,2,3,4]

range(1,6) #[1,2,3,4,5]

range(20,23) #[20,21,22]