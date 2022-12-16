"""palavra = input("Digite uma palavra")

#Palavra - Texto

impares = []

for i in range(len(palavra)):

    if(i%2 == 0):
        impares.append(palavra[i])
        print(impares)
        """

palavra = input("Escrever uma palavra")

i = 0
impares = []

while(i<(len(palavra)-1)):
    impares.append(palavra[i+1])
    i+=2

print(impares)
