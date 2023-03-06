#Questão 1 Slide - Escreva uma função que, 
#dado o valor da conta de um restaurante, calcule e 
#exiba a gorjeta
#do garçom, considerando 10% do valor da conta.

# def calculaGorjeta(valorConta):
#     gorjeta = valorConta *0.1
#     print("O valor da gorjeta é R$",gorjeta)

# calculaGorjeta(200)

# def calculaGorjeta(valorConta):

#     gorjeta = float(valorConta) * 0.1

#     return gorjeta

# conta = input("Digite o valor da conta: ")

# gorjetaConta = calculaGorjeta(conta)

# totalConta = float(conta) + gorjetaConta

# print("Valor da gorjeta R$", gorjetaConta)
# print("Valor total da conta R$", totalConta)

#Questão 2 Slides - Crie uma função que permita contar o 
#número de vezes que aparece uma letra em uma
#string.

# def contaLetras(palavra,letra):
#     contador = 0
    
#     for l in palavra:
#         if l.lower() == letra.lower():
#             contador +=1

#     return contador

# pal = input("Digite uma palavra:")
# let = input("Digite uma letra:")

# contagem = contaLetras(pal,let)


# print(f"A letra {let} aparece {contagem} vezes na palavra {pal}")

#Questão 3 Slides - Faça uma função que receba uma lista de números armazenados 
#de forma crescente, e
#dois valores ( limite inferior e limite superior), 
#e exiba a sublista cujos elementos são
#maiores ou iguais ao limite inferior e menores ou iguais ao limite superior.

def listaIntervalo(lista,limiteInf,limiteSup):
    
    novaLista = []

    for n in lista:
        if n>=limiteInf and n <= limiteSup:
            novaLista.append(n)

    return novaLista

listaNumero = [10,20,25,30,44,32,11,15,27,39,100,48,67,89]

listaNumero.sort()

listaNovaNumero = listaIntervalo(listaNumero,50,100)

print(f'''Lista antiga: {listaNumero}
Nova Lista: {listaNovaNumero}
      ''')
