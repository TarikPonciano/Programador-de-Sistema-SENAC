"""
Write a Python program to count the number of characters in a string. 
Sample String : 'google.com'
Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}

"""
texto = input("Insira seu texto: ")

contagem = {}

#textoMinusculo = texto.lower()

for letra in texto:
    #texto = "Texto"
    #contagem = {'T': 1}
    contagem[letra] = texto.count(letra)

    print(texto,contagem)

# from collections import Counter

# texto = input("Escreva meu texto: ")

# print(Counter(texto))
