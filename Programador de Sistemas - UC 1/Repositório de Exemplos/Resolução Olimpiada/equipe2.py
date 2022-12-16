# crie um programa que receba uma senha de no mínimo 4 digitos e no máximo 8,
# utilizando somente números. O programa deve repetir até o usuário gerar uma senha válida
def checarSenha(s):
    if (s.isnumeric()):
        if (len(s) >= 4 and len(s) <= 8):
            print("Sua senha é válida.")
            global repetir
            repetir = False
        else:
            print(
                f"Sua senha tem {len(s)} digitos. Escreva uma senha entre 4 e 8 digitos!")
    else:
        print(f"Você usou caracteres que não são números.")

repetir = True

while (repetir):

    senha = input(
        "Insira uma senha entre 4 e 8 digitos, que utilize apenas números: ")

    checarSenha(senha)
