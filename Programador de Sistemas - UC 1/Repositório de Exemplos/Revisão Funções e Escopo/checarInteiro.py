def checarInteiro(n):
    if(n.isnumeric()):
        print("Parabéns você escreveu um número inteiro.")
        global repetir
        repetir = False
    else:
        print("Você escreveu algo diferente de um número inteiro.") 
        print("Por favor escreva novamente!")
        

repetir = True

while(repetir):
    num = input("Digite um número inteiro: ")
    checarInteiro(num)

# while(True):
#     num = input("Por favor escreva um número inteiro: ")

#     if(num.isnumeric()):
#         print("O texto que você digitou é um número inteiro.")
#         break
#     else:
#         print("Você não escreveu um número inteiro :(")
        