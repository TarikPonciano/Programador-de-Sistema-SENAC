
numMin = int(input("Escreva o começo do intervalo: "))
numMax = int(input("Escreva o fim do intervalo: "))
soma = 0


if (numMin<=numMax):
    for i in range(numMin,numMax+1):
        soma += i 
        print("Número",i,":",soma)

else: 
    print("Você escreveu um intervalo inválido!")




