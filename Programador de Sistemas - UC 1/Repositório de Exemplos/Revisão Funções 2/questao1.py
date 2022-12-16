def comparaPalavras(pal1, pal2):
    if (len(pal1) > len(pal2)):
        print(f"A palavra '{pal1}' é maior que a palavra '{pal2}'")
    elif (len(pal1) < len(pal2)):
        print(f"A palavra '{pal2}' é maior que a palavra '{pal1}'")
    elif (len(pal1) == len(pal2)):
        print(f"As palavras '{pal1}' e '{pal2}' tem o mesmo tamanho.")
    else:
        print("Algo deu errado")
while (True):
    palavra1 = input("Insira uma palavra: ")
    palavra2 = input("Insira uma palavra: ")

    comparaPalavras(palavra1,palavra2)
