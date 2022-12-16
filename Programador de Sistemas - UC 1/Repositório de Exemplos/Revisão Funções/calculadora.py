def soma(numero1, numero2):
    return float(numero1) + float(numero2)


def subtracao(numero1, numero2):
    return float(numero1) - float(numero2)


def divisao(numero1, numero2):
    if (numero2 == "0"):
        global repetir
        repetir = True
        return "O número 2 não pode ser 0"
    else:
        return float(numero1) / float(numero2)


def multiplicacao(numero1, numero2):
    return float(numero1) * float(numero2)


def calculadora(n1, n2, op):

    if (op == "+"):
        print(soma(n1, n2))
    elif (op == "-"):
        print(subtracao(n1, n2))
    elif (op == "/"):
        print(divisao(n1, n2))
    elif (op == "*"):
        print(multiplicacao(n1, n2))
    else:
        print("O usuário digitou uma operação inválida")
        global repetir
        repetir = True


repetir = True

while (repetir == True):

    num1 = input("Escreva o número 1: ")

    if (num1.isnumeric()):
        num2 = input("Escreva o número 2: ")
        if (num2.isnumeric()):
            repetir = False
            operador = input("Escreva o operador (+,-,/,*)")
            calculadora(num1, num2, operador)
        else:
            print("O número 2 é inválido. Tente novamente!")
            
    else:
        print("O número 1 é inválido. Tente novamente!")
        
