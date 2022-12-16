# Escreva um codigo que leia um mumero de até 4 digitos e consiga determinar
# quantas unidades, dezenas, centenas e
# unidades de milhar o numero tem, e repita enquanto o usuario nao digitar um numero válido

# while (True):
#     numero = input("Escreva um número inteiro de até 4 digitos: ")
#     if (numero.isnumeric()):
#         if (len(numero) <= 4):
#             numero = int(numero) # 6575
#             m = numero // 1000 # 6
#             c = (numero - (1000*m)) // 100 # (6575 - 6000) //100 = 5
#             d = ((numero - (1000*m)) - (100*c)) // 10 # 7
#             u = (((numero - (1000*m)) - (100*c)) - (10*d)) # 5
#             print(f"""
#             Unidades = {u}
#             Dezenas = {d}
#             Centenas = {c}
#             Milhares = {m}
#             """)
#             break
#         else:
#             print("Você deve escrever um número de até 4 digitos!")
#     else:
#         print("Você escreveu digitos que não são números!")

# unidades = ("unidade","dezena","centena","milhar","dezena de milhar","centena de milhar","milhão")

# while(True):

#     numero = input("Escreva um número inteiro de até 7 digitos: ")
#     #numeroInvertido = []

#     if (numero.isnumeric()):
#         if (len(numero) <= 7):

#             for i in range(len(numero)):
#                 print(f"{unidades[-i-1]} = {numero[i]}") # 1234567

#             break

#         else:
#             print("Você deve escrever um número de até 7 digitos!")
#     else:
#         print("Você digitou algum caractere que não é número.")

    
numero = int(input("Insira um numero de até 4 digitos: "))

resposta = numero

m = 0
c = 0
d = 0
u = 0

while(resposta!=0):
    if(resposta>=1000):
        resposta -= 1000
        m += 1
    elif (resposta>=100):
        resposta -= 100
        c += 1
    elif (resposta>=10):
        resposta -= 10
        d += 1
    elif (resposta>=1):
        resposta -= 1
        u += 1
    else: break

print(f"""Número inicial {numero} 
Milhares {m} 
Centenas {c}
Dezenas {d}
Unidades {u} """)








