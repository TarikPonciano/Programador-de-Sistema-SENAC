def separarEquipes(lista, n):
    for i in range(0, len(lista), n):
        yield lista[i:i + n]


listaAlunos = []
qtdeAlunos = int(input("Digite a quantidade de alunos: "))
qtdeEquipe = int(input("Digite a quantidade de equipes: "))

listaAlunos = list(range(qtdeAlunos))
# for aluno in range(qtdeAlunos):
#     aluno = input("Digite o nome do aluno: ")
    
alunosPorEquipe = int(qtdeAlunos / qtdeEquipe)

print(list(separarEquipes(listaAlunos, alunosPorEquipe)))