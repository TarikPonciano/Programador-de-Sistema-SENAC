def potencia(a,b):
    resultado = 1

    while(b>0):
        resultado = resultado * a
        b -= 1
    
    return resultado

base = input("Digite a base:")

expoente = input("Digite expoente:")

print(potencia(int(base),int(expoente)))

