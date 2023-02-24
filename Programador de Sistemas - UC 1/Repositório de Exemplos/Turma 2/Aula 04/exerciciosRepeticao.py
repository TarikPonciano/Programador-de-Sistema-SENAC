#Questão 1 - Calcule a tabuada do 13.

def questao1():

    #Método For
    for i in range(1,11):
        tabuada = 13 * i
        print(f"13 x {i} = {tabuada}")

    #Método While
    contador = 1
    while contador <= 10:
        tabuada = 13 * contador
        print(f"13 x {contador} = {tabuada}")
        contador = contador + 1
#Questão 2 - Ler do teclado 10 números e imprima a quantidade de números entre 10 e 50.
def questao2():

    numerosNoIntervalo = 0

    for i in range(10):
        numero = float(input("Digite um número:"))

        if numero >= 10 and numero <= 50:
            numerosNoIntervalo = numerosNoIntervalo + 1
    
    print(f"Quantidade de numeros entre 10 e 50: {numerosNoIntervalo}")

#Ler do teclado uma lista com 5 inteiros e imprimir o menor valor

def questao3():
    
    for i in range(5):
        numero = int(input("Insira um número inteiro: "))

        if i == 0:
            menor = numero
        else:
            if numero < menor:
                menor = numero

        print("O menor número foi", menor)
        
def questao4():

    #Crie a variável soma
    #Faça um for de 1 a 101
    #Dentro desse for incremente a variável soma com i
    #Fora do for imprima a variável soma

    soma = 0

    for i in range(1,101):
        soma = soma + i

    print("Somatório de 1 até 100 é",soma)

#Questão 5 - Receba dois números inteiros correspondentes à largura e altura. Devolva uma
#cadeia de caracteres # que representa um retângulo com as medidas fornecidas.

def questao5():
    altura = int(input("Escreva a altura do retângulo:"))
    largura = int(input("Escreva a largura do retângulo:"))

    linha = ""

    for i in range(largura):
        linha = linha + "#"
    
    retangulo = ""

    for i in range(altura):
        retangulo = retangulo + "\n" + linha

    # linha = "#" * largura
    # retangulo = (linha + "\n") * altura

    print(retangulo)

questao5()