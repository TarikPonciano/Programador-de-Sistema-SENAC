import json

class Funcionario:
    def __init__(self, id, nome, salario):
        self._id = id
        self._nome = nome
        self._salario = salario

def adicionarFuncionario():
    novoNome = input("Digite o nome do funcionario novo:")
    novoSalario = float(input(f"Digite o salario de {novoNome}:"))
    novoFuncionario = Funcionario(len(funcionarios)+1,novoNome,novoSalario)
    funcionarios.append(novoFuncionario)
    print(f"{novoFuncionario._nome} adicionado com sucesso!\n")

def salvarBanco(listaFuncionarios):
    novoBanco = []

    for f in listaFuncionarios:
        novoBanco.append({"ID": f._id, "Nome": f._nome, "Salario": f._salario})
    
    with open("C:/Trabalho/Senac/UC2 - Banco de Dados/Atividades/Exemplo 1/banco.json", 'w') as nb:
        json.dump(novoBanco, nb, indent=2)

    print("Banco salvo")


with open("C:/Trabalho/Senac/UC2 - Banco de Dados/Atividades/Exemplo 1/banco.json") as b:
    # C:\Trabalho\Senac\UC2 - Banco de Dados\Atividades\Exemplo 1
    banco = json.load(b)

funcionarios = []

for funcionario in banco:
    funcionarios.append(Funcionario(funcionario["ID"], funcionario["Nome"], float(funcionario["Salario"])))

for i in range(len(funcionarios)):
    print(f"{funcionarios[i]._id} - {funcionarios[i]._nome}")

while(True):
    menu = input(f"""Escolha uma das opções:
        1. Ver Funcionarios
        2. Ver salário de Funcionario
        3. Adicionar Funcionario
        0. Sair da aplicação e Salvar
        \n
    
    """)
    

    
    match menu:
        case "1":
            for i in range(len(funcionarios)):
                print(f"{funcionarios[i]._id} - {funcionarios[i]._nome}")
            input("Insira qualquer tecla para continuar")
        case "2":
            op = int(input("Digite o id do funcionario que deseja ver o salário:"))
            print(f"O salário do {funcionarios[op-1]._nome} é R$ {funcionarios[op-1]._salario} \n")
            input("Insira qualquer tecla para continuar")
        case "3":
            adicionarFuncionario()
            input("Insira qualquer tecla para continuar")
        case "0":
            salvarBanco(funcionarios)
            print("Aplicação finalizada e dados salvos")
            break
        case _:
            print("Opção inválida")

    