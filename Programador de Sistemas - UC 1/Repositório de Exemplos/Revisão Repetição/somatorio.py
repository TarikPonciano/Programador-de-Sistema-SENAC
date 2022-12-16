#Calcule o somatório dos números de 1 a 100 e imprima o resultado.
intervaloValido = 0

while(intervaloValido == 0):

    numMin = int(input("Digite o início do intervalo: "))
    numMax = int(input("Digite o final do intervalo: "))

    if(numMin<=numMax):
        
        print("Você digitou um intervalo válido.")
        print(f"Intervalo digitado: {numMin} - {numMax}")
        intervaloValido=1

    else:
        print("Você digitou um intervalo inválido, digite novamente.")
        print(f"Intervalo digitado: {numMin} - {numMax}")
        intervaloValido=0

soma = 0

for i in range(numMin,(numMax+1)):
    soma += i

print(f"O somatório de {numMin} até {numMax} é: {soma}")