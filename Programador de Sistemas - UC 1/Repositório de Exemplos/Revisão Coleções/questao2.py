palavra = input("Escreva uma palavra")
#len(Tarik) > 5
palavraInvertida = ""
#palavra[4] > "e"
#len(palavra)-1
for i in range(len(palavra)):
    palavraInvertida += palavra[(len(palavra)-1)-i]
    
print(palavraInvertida)
    
