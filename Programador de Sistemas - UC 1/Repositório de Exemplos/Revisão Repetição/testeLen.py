vogais = ("a","e","i","o","u")

texto = "TESTANDO"

print("A frase 'Testando' tem",len(texto),"caracteres")

print(texto[3])

v = 0

for c in texto:
    for x in vogais:
        if(c.lower()==x):
            v+=1

print("O texto contém ",v," vogais")
print(f"Texto original = {texto} // Texto usando lower = {texto.lower()}")


