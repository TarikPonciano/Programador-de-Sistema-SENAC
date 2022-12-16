#.Ler do teclado 10 números e 
# imprima a quantidade de números entre 10 e 50.
"""
numeros = [None] * 5 #[None, None, None, None, None, None, None, None, None, None]
numerosValidos = []
contador = 0

for i in range(5):
    numeros[i] = int(input(f"Escreva o número {i+1}: "))
    print(numeros)
    #numero.append(int(input("Escreva o número",(i+1),":")))

for n in numeros:
    if(n>=10 and n<=50):
        numerosValidos.append(n)
        contador+=1

print(f"A quantidade de números entre 10 e 50 é: {contador} e os numeros foram {numerosValidos}")
"""

repetir = 10
contador = 0

for i in range(repetir):
    n = int(input(f"Escreva o número {i+1}: "))
    if (n>=10 and n<=50):
        contador += 1

print("A quantidade de números foi: ",contador)

