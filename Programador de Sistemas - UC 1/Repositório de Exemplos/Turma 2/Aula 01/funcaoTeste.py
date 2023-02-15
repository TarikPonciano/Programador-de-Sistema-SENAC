def cadastroEstoque():
    nomeItem = input("Digite o nome do Produto: ")
    qtdItem = input(f"Digite a quantidade de {nomeItem}: ")
    
    return f"A quantidade de {nomeItem} foi {qtdItem}"
msg = ""

for i in range(5):
    msg = msg + "\n" + cadastroEstoque()

print(msg)