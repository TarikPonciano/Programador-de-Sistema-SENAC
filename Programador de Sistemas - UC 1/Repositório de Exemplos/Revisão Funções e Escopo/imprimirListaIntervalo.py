import random


def checarIntervalo(l, min, max):
    listaFinal = []
    if (min > max):
        min, max = max, min
    for i in l:
        if (i >= min and i <= max):
            listaFinal.append(i)
            print(listaFinal)


while (True):
    listaNum = []

    for i in range(30):
        listaNum.append(random.randrange(300))

    listaNum.sort()

    numMin = input("Insira o intervalo mínimo: ")
    numMax = input("Insira o intervalo máximo: ")

    if (numMin.isnumeric() and numMax.isnumeric()):
        checarIntervalo(listaNum, int(numMin), int(numMax))
        check = input("Deseja continuar? 'Sim - 1// Não - 0: ")
        if (check == "0"):
            break
    else:
        print("Escreva valores válidos para o intervalo.")
