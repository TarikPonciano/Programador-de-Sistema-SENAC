notas = []
nota = 0


while(len(notas)<5):

    nota = float(input("Insira uma nota: "))

    if(nota<=10 and nota>=0):
        notas.append(nota)
    else:
        print("Valor invalido")
    
    print("Nossa lista de notas:", notas)


media = sum(notas)/len(notas)

print("Media: ", media)