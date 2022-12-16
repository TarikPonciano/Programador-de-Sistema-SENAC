nome = input("Nome do aluno:")
notas = []

soma = 0

for i in range(3):

    nota = float(input("Digite a nota "+str(i)+": "))

    if(nota<=10 and nota>=0):
        notas.append(nota)
        soma += nota
    else:
        print("Valor inválido.")
    
    print(notas)

media = soma/len(notas)

if (media >= 7):
    print("Resultado final: APROVADO")
elif (media <= 5):
    print("Resultado final: REPROVADO")
elif (media > 5 and media < 7):
    print("Resultado final: RECUPERAÇÃO")
else:
    print("Notas inválidas")
