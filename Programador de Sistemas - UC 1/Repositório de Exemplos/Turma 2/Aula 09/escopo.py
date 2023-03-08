# def e(b):
    
#     a = b*b
#     return a

# a = 10

# e(a)
# e(a)

# print(e(a))
varGlobal = "Esta é uma variável global"

def potencia(base,expoente):

    resultado = 1
    print(varGlobal)

    for i in range(expoente):
        resultado = resultado * base

    return resultado

def main():
    a = potencia(2,10)
    b = 10 + potencia(3,5)
    print(a)
    print(potencia(10, 5))
    print(b)
    print(varGlobal)


main()