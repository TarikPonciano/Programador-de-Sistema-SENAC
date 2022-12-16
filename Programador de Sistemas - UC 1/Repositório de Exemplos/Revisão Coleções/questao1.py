#Dado o nome de uma pessoa, retorne o número de letras do nome e a primeira
#letra do nome.
letras = ("a","b","c","d","e","f","g","h","i","j","k","l")

nome = input("Escreva seu nome:")

totalDeLetras = 0

for caracter in letras:

 totalDeLetras += nome.lower().count(caracter)


print("Tota de letras:",totalDeLetras)
print(nome[0])