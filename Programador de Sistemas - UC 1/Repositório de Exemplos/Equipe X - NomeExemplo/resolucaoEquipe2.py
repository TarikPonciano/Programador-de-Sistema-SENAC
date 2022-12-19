#Faça um algoritmo para receber um número qualquer e informar na tela se é par ou
#ímpar. 

"""numero = int(input("Escreva um número: "))

if(numero % 2 == 0):
    print("O numero",numero,"é par.")
else:
    print("O numero "+str(numero)+" é impar.")"""

#Escrever um algoritmo que leia o nome e as três notas obtidas por um aluno durante o
#semestre. Calcular a sua média (aritmética), informar o nome e sua menção aprovado
#(media >= 7), Reprovado (media <= 5) e Recuperação (media entre 5.1 a 6.9)

nome = input("Escreva o nome do aluno: ")
nota1 = float(input("Escreva a nota 1: "))
nota2 = float(input("Escreva a nota 2: "))
nota3 = float(input("Escreva a nota 3: "))

media = (nota1+nota2+nota3)/3

print("Olá", nome+".","Seu resultado foi: ")
print("Nota 1:",nota1)
print("Nota 2:",nota2)
print("Nota 3:",nota3)
print(f"Media: {media:.2f}")

if (media >= 7):
    print("Resultado final: APROVADO")
elif (media<=5):
    print("Resultado final: REPROVADO")
elif (media>5 and media<7):
    print("Resultado final: RECUPERAÇÃO")
else:
    print("Notas inválidas")