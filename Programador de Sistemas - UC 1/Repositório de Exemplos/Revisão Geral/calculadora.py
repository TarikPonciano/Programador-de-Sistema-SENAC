repetir = True

while (repetir):

    repetir = False

    num1 = input("Digite o primeiro número: ")

    #if (num1.isnumeric() and num2.isnumeric())

    if (num1.isnumeric()):

        num1 = float(num1)
        num2 = input("Digite o segundo número: ")

        if (num2.isnumeric()):
            num2 = float(num2)
            
            operador = input("Digite a operação ([+ ou SOMAR], [- ou SUBTRAIR], [/ ou DIVIDIR], [* ou MULTIPLICAR]): ")  
            
            if (operador == "+" or operador.lower() == "somar"):
                print("A soma é: ", num1+num2)
            elif (operador == "-" or operador.lower() == "subtrair"):

                print("A subtração é: ", num1-num2)
            elif (operador == "/" or operador.lower() == "dividr"):
                if (num2 == 0):
                    repetir = True
                    print("Você tentou dividir por 0, operação inválida!")
                else:
                    print("A divisão é: ", num1/num2)
            elif (operador == "*" or operador.lower() == "multiplicar"):

                print("A multiplicação é: ", num1*num2)
            else:
                repetir = True
                print("O operador que você digitou é inválido!")
                print("Tente novamente")
        else:
            repetir = True
            print("O número que você digitou não é válido.")
    else:
        repetir = True
        print("O número que você digitou não é válido.")
