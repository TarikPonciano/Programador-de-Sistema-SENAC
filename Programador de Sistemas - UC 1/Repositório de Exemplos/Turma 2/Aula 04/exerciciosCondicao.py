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

#Questão Lanchonete - Escrever um algoritmo que leia o código do item pedido, a quantidade e
#calcule o valor a ser pago por aquele lanche. Considere que a cada
#execução somente será calculado um item.
def questaoLanchonete():

    while True:
        print('''
        
        Especificação Preço unitário
        100 Cachorro quente 1,10
        101 Bauru simples 1,30
        102 Bauru c/ovo 1,50
        103 Hamburger 1,10
        104 Cheeseburger 1,30
        105 Refrigerante 1,00
        
        
        ''')
        codigos = ("100","101","102","103","104","105")
        codigo = input("Insira o código do produto escolhido: ")
        
        

        if codigo in codigos:
            
            quantidade = int(input("Quantos deseja comprar: "))
            if codigo == "100":
                nome = "Cachorro Quente"
                preco = 1.10
            elif codigo == "101":
                nome = "Bauru Simples"
                preco = 1.30
            elif codigo == "102":
                nome = "Bauru c/ ovo"
                preco = 1.50
            elif codigo == "103":
                nome = "Hamburguer"
                preco = 1.10
            elif codigo == "104":
                nome = "Cheeseburguer"
                preco = 1.30
            elif codigo == "105":
                nome = "Refrigerante"
                preco = 1.00

            valorTotal = preco * quantidade
            print(f"Você comprou {quantidade} {nome} por R$ {valorTotal}")
            break
        else:
            print("Insira um código válido")

        # match codigo:
        #     case "100":
        #         nome = "Cachorro Quente"
        #         preco = 1.10
        #     case "101":
        #         nome = "Bauru Simples"
        #         preco = 1.30
        #     case "102":
        #         nome = "Bauru c/ ovo"
        #         preco = 1.50
        #     case "103":
        #         nome = "Hamburguer"
        #         preco = 1.10
        #     case "104":
        #         nome = "Cheeseburguer"
        #         preco = 1.30
        #     case "105":
        #         nome = "Refrigerante"
        #         preco = 1.00
        

questaoLanchonete()
