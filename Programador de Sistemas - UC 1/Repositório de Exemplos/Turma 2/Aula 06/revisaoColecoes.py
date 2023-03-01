# Questão Slide 1 - Dado o nome de uma pessoa, retorne o número de letras do 
# nome e a primeira letra do nome.

def questaoSlide1():
    nome = input("Digite o seu nome:")

    numeroDeLetras = len(nome) - nome.count(" ")
    print(numeroDeLetras)

    print(nome[0])

# Questão Slide 2 - Dada uma palavra, retorna a palavra invertida


def questaoSlide2():
    palavra = input("Digite uma palavra:")

    print(palavra[::-1])

    palavraInvertida = ""

    for i in range(len(palavra)):
        
        palavraInvertida = palavraInvertida + palavra[len(palavra)-1-i]
        print(palavraInvertida)

    invertido = list(reversed(palavra))

    print(*invertido)

    outroInvertido = list(palavra)

    outroInvertido.reverse()

    print("".join(outroInvertido))


# Questão Slide 3 - Dada uma palavra, retorna os caracteres nas posições
# ímpares

def questaoSlide3():

    palavra = input("Digite uma palavra:")

    letraImpar = []

    for i in range(len(palavra)):

        if i % 2 == 0:

            print(f"{i+1} {palavra[i]}")
            letraImpar.append(palavra[i])

    print(letraImpar)

#Questão 7 Listas - Escreva um programa Python para remover duplicatas de uma lista.

def questao7Listas():

    lista = [2,2,2,"a",4,5,5,"a","a","b","b",2,3,3,4,"a"]

    contador = 0

    while contador < len(lista):

        for i in range(len(lista)):
            if contador != i:
                if i < len(lista):
                    if lista[contador] == lista[i]:
                        print(lista)
                        print(f"Elemento observado: pos - {contador} {lista[contador]}")
                        print(f"Duplicata removida: pos - {i} {lista[i]}")
                        lista.pop(i)
                        #input()

        contador += 1

    print(lista)

#Questao 6 Listas - Escreva um programa Python para obter uma lista, 
# classificada em ordem crescente 
# pelo último elemento em cada tupla de uma determinada lista de tuplas não vazias.

def questao6Listas():

    lista = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

    novaLista=[]

    elementosPosicaoDois = []

    listaPosicoes = []

    

    for i in range(len(lista)):

        elementosPosicaoDois.append(lista[i][1])

    elementosPosicaoDois.sort(reverse=True)

    while len(listaPosicoes) < len(lista):

        for x in reversed(list(range(len(elementosPosicaoDois)))):
            for i in range(len(lista)):
                if x < len(elementosPosicaoDois):
                    if elementosPosicaoDois[x] == lista[i][1]:
                        print(elementosPosicaoDois)
                        print(i)
                        elementosPosicaoDois.pop(x)
                        listaPosicoes.append(i)

    for pos in listaPosicoes:
        novaLista.append(lista[pos])


    
    print(listaPosicoes)
    
    print(novaLista)

    print(sorted(lista))

questao6Listas()
