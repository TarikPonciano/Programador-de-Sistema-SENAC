#Fazer um programa onde seja inserido nomes de alunos e a quantidade de equipes.
#Esses alunos tem que ser organizados na equipe com quantidades iguais.

alunos = list(range(20))

numeroDeEquipes = int(input("Insira o número de equipes: "))

equipes = []

if (len(equipes)!=numeroDeEquipes):
    for i in range(numeroDeEquipes):
        equipes.append([])
    print(equipes)

while(len(alunos)>0):

    for i in range(len(equipes)):
        if(len(alunos)>0):
            equipes[i].append(alunos[0])
            alunos.pop(0)
            print(equipes)
    

