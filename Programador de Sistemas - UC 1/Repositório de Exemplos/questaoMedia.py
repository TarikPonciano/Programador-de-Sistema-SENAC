nome = input("Nome do aluno:")
notas = []
nota = 0

while (len(notas) < 3):
    nota = float(input("Escreva uma nota: "))

    if (nota <= 10 and nota >= 0):
        notas.append(nota)
    else:
        print("Valor invalido")

    print("Nossa lista de notas:", notas)

media = sum(notas)/len(notas)
print("A média do aluno é:",media)
if (media >= 7):
    print("Resultado final: APROVADO")
elif (media <= 5):
    print("Resultado final: REPROVADO")
elif (media > 5 and media < 7):
    print("Resultado final: RECUPERAÇÃO")
else:
    print("Notas inválidas")
