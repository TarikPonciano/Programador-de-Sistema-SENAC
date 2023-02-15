#Questão 1 - Faça um algoritmo que leia os valores A, B, C e imprima na tela se a soma de A + B é
#menor que C. 

def questao1():

    A = int(input("Digite o valor A: "))
    B = int(input("Digite o valor B: "))
    C = int(input("Digite o valor C: "))

    soma = A+B
    
    if soma < C:
        print("A soma é menor que C")
    else:
        print("A soma é maior ou igual a C")

#Questão 2 - Faça um algoritmo para receber um número qualquer e informar na tela se é par ou
#ímpar.

def questao2():

    num = int(input("Digite um número inteiro: "))

    if num%2 == 0:

        print("O número é par")

    else:

        print("O número é ímpar") 

#Questão 3 - Faça um algoritmo que leia dois valores inteiros A e B se os valores forem iguais
# deverá somar os dois, caso contrário multiplique A por B. Ao final de qualquer um dos
# cálculos deve-se atribuir o resultado para uma variável C e mostrar seu conteúdo na
# tela

def questao3():

    A = int(input("Insira o inteiro A:"))
    B = int(input("Insira o inteiro B:"))

    if A == B:
        C = A+B
        print("A soma foi",C)
    else:
        C = A*B
        print("A multiplicação foi", C)


#Questão 4 -Escreva um algoritmo que leia três valores inteiros e diferentes e mostre-os em ordem
#decrescente. 

def questao4():

    # valores = [30,50,20,100,200,23,10,11,40]
    # valores.sort(reverse=True)

    # print(valores)

    A = int(input("Digite o valor A: "))
    B = int(input("Digite o valor B: "))
    C = int(input("Digite o valor C: "))

    primeiro = A
    segundo = B
    terceiro = C

    if A==B or A==C or B==C:

        print("Eles são iguais")

    elif(A>=B and A>=C):
        primeiro = A
        if(B>=C):
            segundo = B
            terceiro = C
        else:
            segundo = C
            terceiro = B
    
    elif(B>=A and B>=C):
        primeiro = B
        if(A>=C):
            segundo = A
            terceiro = C
        else:
            segundo = C
            terceiro = A
    
    elif(C>=B and C>=A):
        primeiro = C
        if(B>=A):
            segundo = B
            terceiro = A
        else:
            segundo = A
            terceiro = B

    else:
        print("Algo deu errado")

    print(primeiro,segundo,terceiro)

questao4()












# lista = [20,50,10]
# lista.sort(reverse=True)
# print(lista)

# a = int(input("Digite um número: "))
# b = int(input("Digite um número: "))
# c = int(input("Digite um número: "))

# primeiro = a
# segundo = a
# terceiro = a

# if a == b or a == c:
#     print("Os números são iguais.")

# elif(a>=b and a>=c):
#     primeiro = a
#     if b>=c:
#         segundo = b
#         terceiro = c
#     else:
#         segundo = c
#         terceiro = b

# elif(b>=a and b>=c):
#     primeiro = b
#     if a>=c:
#         segundo = a
#         terceiro = c
#     else:
#         segundo = c
#         terceiro = a

# elif(c>=a and c>=b):
#     primeiro = c
#     if b>=a:
#         segundo = b
#         terceiro = a
#     else:
#         segundo = a
#         terceiro = b

# print(primeiro,segundo,terceiro)
