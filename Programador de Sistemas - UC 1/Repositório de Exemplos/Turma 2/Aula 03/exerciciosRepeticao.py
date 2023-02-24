#Questão 1 - Calcule a tabuada do 13

def questao1():

    for i in range(1,11):
        calculo = i*13
        print(f"{i}. {i}x13 = {calculo}" )


# Questão 2 Ler do teclado 10 números e imprima a quantidade de números entre 10 e 50.

def questao2():
    quantidade = 0

    for i in range(10):
        numero = int(input("Insira um numero"))

        if numero >= 10 and numero <=50:
            quantidade = quantidade + 1
        
    print("Quantidade de numeros dentro do intervalo é", quantidade)

#Questão 3 - Ler do teclado uma lista com 5 inteiros e imprimir o menor valor.

def questao3():
    menor = 0

    for i in range(5):
        numero = int(input("Digite um inteiro:"))

        if menor == 0:
            menor = numero

        elif numero <= menor:
            menor = numero

    print("O menor numero inserido foi:",menor)

