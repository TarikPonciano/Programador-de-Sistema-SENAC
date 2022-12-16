# Escreva uma função que, dado o valor da conta 
# de um restaurante, calcule e exiba a gorjeta
# do garçom, considerando 10% do valor da conta.


# def gorjetaGarcom(valorConta):
#     gorjeta = valorConta * 0.1
#     return gorjeta

# valorGorjeta = gorjetaGarcom(300)
# print(valorGorjeta)


# def gorjetaGarcom(valorConta):
#     print(valorConta*0.1)

# valor = input("Digite o valor da conta: ")

# if (valor.isnumeric()):
#     gorjetaGarcom(float(valor))
# else:
#     print("O usuário não digitou um número")

def calcularGorjeta():
    valorDaConta = input("Escreva o valor da conta: ")
    print("O valor da gorjeta é: ", float(valorDaConta)*0.1)

operacao = input("Digite o que você quer fazer (1 = Calcular Gorjeta) ")

if (operacao=="1"):
    calcularGorjeta()