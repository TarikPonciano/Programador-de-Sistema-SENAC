item1Nome = input("Digite o nome do item 1: ")
item2Nome = input("Digite o nome do item 2: ")
item3Nome = input("Digite o nome do item 3: ")
item4Nome = input("Digite o nome do item 4: ")
item5Nome = input("Digite o nome do item 5: ")

item1Qtd = int(input("Digite a quantidade do "+item1Nome))
item2Qtd = input(f"Digite a quantidade do {item2Nome}: ")
item3Qtd = input(f"Digite a quantidade do {item3Nome}: ")
item4Qtd = input(f"Digite a quantidade do {item4Nome}: ")
item5Qtd = input(f"Digite a quantidade do {item5Nome}: ")

print(item1Nome,item1Qtd)

print(f'''
{item1Nome} - {item1Qtd}
{item2Nome} - {item2Qtd}
{item3Nome} - {item3Qtd}
{item4Nome} - {item4Qtd}
{item5Nome} - {item5Qtd}
''')