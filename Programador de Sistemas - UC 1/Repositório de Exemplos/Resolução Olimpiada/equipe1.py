# # Escreva uma palavra e escolha uma letra. Retorne o número de vezes que a letra aparece na palavra.
# palavra = input("Insira uma palavra: ")

# while (True):

#     letra = input("Insira apenas um caractere: ")
#     if (len(letra) == 1):
#         break
#     else:
#         print("Você inseriu mais que um caractere, insira novamente!")

# #Tem que fazer essa linha sem usar .count! checagem = palavra.lower().count(letra.lower())
# print(f"O caractere '{letra}' na palavra '{palavra}' apareceu {checagem} vezes")


def checarLetra(palavra,letra):
    contador = 0

    for caractere in palavra:
        if(caractere==letra):
            contador+=1

    return contador
        

palavraEscolhida = input("Digite uma palavra: ")
letraEscolhida = input("Digite uma letra: ")

print(checarLetra(palavraEscolhida,letraEscolhida))