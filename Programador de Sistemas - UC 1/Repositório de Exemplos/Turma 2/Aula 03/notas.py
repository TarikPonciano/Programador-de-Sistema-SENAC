# Escrever um algoritmo que leia o nome e as três notas obtidas por um aluno durante o
# semestre. Calcular a sua média (aritmética), informar o nome e sua menção aprovado
# (media >= 7), Reprovado (media <= 5) e Recuperação (media entre 5.1 a 6.9)

nome = input("Digite seu nome:")
nota1 = float(input("Digite a nota 1:"))
nota2 = float(input("Digite a nota 2:"))
nota3 = float(input("Digite a nota 3:"))

soma = nota1 + nota2 + nota3

media = soma/3


if media >= 7:
    print(f"{nome} você foi aprovado com {media}!")
elif media <=5:
    print(f"{nome} você foi reprovado com {media}!")
elif media<7 and media>5:
    print(f"{nome} você está de recuperação com {media}!")
else:
    print("Inválido")

