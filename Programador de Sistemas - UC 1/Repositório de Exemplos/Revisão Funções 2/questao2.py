def checarLetra(L, p):
    if (L in p):
        print(f"A letra '{L}' existe na palavra '{p}' ")
    else:
        print(f"A letra '{L}' não existe na palavra '{p}'")

checarLetra("a", "teste")

checarLetra("c", "cachorro")
