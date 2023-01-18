import json

class Funcionario:
    def __init__(self, idFunc, nomeFunc, idDept):
        self.idFunc = idFunc
        self.nomeFunc = nomeFunc
        self.idDept = idDept

class Departamento:
    def __init__(self, idDept, nomeDept, idChefeDept ):
        self.idDept = idDept
        self.nomeDept = nomeDept
        self.idChefeDept = idChefeDept

with open("departamentos.json") as d:
    departamentosDados = json.load(d)

with open("funcionarios.json") as f:
    funcionariosDados = json.load(f)

funcionarios = []

for func in funcionariosDados:
    funcionarios.append(Funcionario(func["ID_Funcionario"], func["Nome_Funcionario"], func["ID_Departamento"]))

departamentos = []

for dept in departamentosDados:
    departamentos.append(Departamento(dept["ID_Departamento"], dept["Nome_Departamento"], dept["Chefe_Departamento"]))



print("Escolha o departamento")

# for i in range(len(departamentos)):

#     print(f"{i+1} - {departamentos[i].nomeDept}")

for dept in departamentos:
    print(f"{dept.idDept} - {dept.nomeDept}")

idDeptEscolhido = input("Digite o ID do departamento para ver os funcionários: ")

for dept in departamentos:
    if dept.idDept == int(idDeptEscolhido):
        deptEscolhido = dept

for func in funcionarios:
    if func.idDept == deptEscolhido.idDept:
        print(f"{func.idFunc} - {func.nomeFunc}")
    
    if deptEscolhido.idChefeDept == func.idFunc:
        chefeDepartamentoEscolhido = func

print(f"""O Chefe do departamento:
        ID - {chefeDepartamentoEscolhido.idFunc}
        Nome - {chefeDepartamentoEscolhido.nomeFunc}
        
                    """)
