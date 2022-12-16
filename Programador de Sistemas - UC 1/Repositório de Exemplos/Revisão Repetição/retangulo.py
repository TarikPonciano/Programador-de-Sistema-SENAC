#Receba dois números inteiros correspondentes à largura e altura. 
# Devolva uma cadeia de caracteres # que representa um retângulo 
# com as medidas fornecidas.

"""largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))

linha = ""

for l in range(largura):
    linha += "# "

print("Minha linha: ",linha)
print("-------------------------------------------")

for a in range(altura):
    print(linha)
"""

largura = int(input("Digite a largura:"))
altura = int(input("Ditite a altura: "))

print((("# "*largura)+"\n")*altura)