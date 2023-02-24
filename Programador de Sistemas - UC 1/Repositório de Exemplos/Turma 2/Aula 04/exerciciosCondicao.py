#Questão 4 - Escreva um algoritmo que leia três valores inteiros e diferentes e mostre-os em ordem
#decrescente. 

def questao4Simples():
    num1 = int(input("Escreva o número 1: "))
    num2 = int(input("Escreva o número 2: "))
    num3 = int(input("Escreva o número 3: "))

    lista = [num1,num2,num3]
    lista.sort(reverse=True)

    print(lista)

def questao4Complexa():

    num1 = int(input("Escreva o número 1: "))
    num2 = int(input("Escreva o número 2: "))
    num3 = int(input("Escreva o número 3: "))

    primeiro = None
    segundo = None
    terceiro = None

    if (num1 != num2 and num1 != num3 and num2 != num3):

        if(num1 > num2 and num1 > num3):
            primeiro = num1
            if (num2 > num3):
                segundo = num2
                terceiro = num3
            else:
                segundo = num3
                terceiro = num2

        elif (num2 > num1 and num2 > num3):
            primeiro = num2
            if (num1 > num3):
                segundo = num1
                terceiro = num3
            else:
                segundo = num3
                terceiro = num1

        else:
            primeiro = num3
            if (num1 > num2):
                segundo = num1
                terceiro = num2
            else:
                segundo = num2
                terceiro = num1
        
        print(primeiro,segundo,terceiro)
    

    else:
        print("Você escreveu números iguais.")

questao4Complexa()