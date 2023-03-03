#Questão 6 Lista - Escreva um programa Python para obter uma lista, 
# classificada em ordem crescente pelo último elemento em cada tupla 
# de uma determinada lista de tuplas não vazias.

#Lista de amostras: [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

#[(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

def questao6ListaSolucao1():

    # 1. Receber uma lista
    # 2. Guardar o segundo elemento de cada tupla dessa lista
    # 3. Ordernar essa lista de segundos elementos
    # 4. Comparar lista de segundo elemento com o segundo elementos das tuplas
    # da lista original
    # 5. Usar a lista de posições para adicionar em uma nova lista os elementos
    # da lista original na ordem correta

    lista = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1), (5,5),(1,3)]

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
    
    for pos in reversed(listaPosicoes):
        novaLista.append(lista[pos])

    
    print(novaLista)

def questao6ListaSolucao2():
    #1. Receber uma lista
    #2. Inverter as tuplas dentro dessa lista
    #3. Usar a função sorted pra colocar essas listas na ordem
    #4. Inverter novamente as tuplas dentro dessa lista

    lista = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1), (5,5), (10,100),(2,2)]

    novaLista = []

    for tupla in lista:
        novaLista.append(tupla[::-1])
        
    novaLista.sort()

    lista.clear()
    
    for tupla in novaLista:
        lista.append(tupla[::-1])

    print(lista)

def questao6ListaSolucao3():
    # 1. Receber a lista
    # 2. Criar as variáveis menor e novaLista
    # 3. Criar um laço de repetição que repete de acordo com o tamanho da lista original
    # 4. Checar cada tupla, se a tupla checada tiver o segundo elemento menor que a tupla anterior salva
    #    e a tupla ainda não tiver sido adicionada em novaLista
    #    guardar a tupla checada na variável menor
    # 5. Se a variável menor ainda não estiver presente em novaLista,
    #    guardar essa tupla em novaLista
    lista = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
    menor = None
    novaLista = []

    for x in range(len(lista)):
        for tupla in lista:
            if ((menor == None or tupla[1]<menor[1]) and tupla not in novaLista):
                menor = tupla
        if menor not in novaLista:
            novaLista.append(menor)
        menor = None
    
    print(novaLista)

questao6ListaSolucao3()