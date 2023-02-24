# contador = 0

# while contador < 5:
#     print(contador)
#     contador = contador + 1

while True:

    cpf = input("Insira seu CPF:")

    if len(cpf) != 11:
        print("O CPF deve ter 11 digitos. Tente Novamente!")
    else:
        break

# cpfValido = False
# while cpfValido == False:

#     cpf = input("Insira seu CPF:")

#     if len(cpf) != 11:
#         print("O CPF deve ter 11 digitos. Tente Novamente!")
#     else:
#         cpfValido = True