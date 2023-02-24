idade = int(input("Escreva sua idade: "))

if idade >= 10 and idade < 20:
    print("Você é adolescente.")
else:
    if idade >= 20 and idade < 30:
        print("Você é jovem")
    else:
        if idade>= 30 and idade < 100:
            print("Você é adulto")
        else:
            print("Valor não encontrado")
continuar = True
while continuar:
    numero = input("Digite um número: ")
    
    if numero == "0":
        continuar = False
    else:
        print(numero)

nomes = ["Pedro", "Paulo", "João"]

nome = "Josué"

if nome in nomes:
    print(nome,"está em nomes")
else:
    print(nome,"não está em nomes")


