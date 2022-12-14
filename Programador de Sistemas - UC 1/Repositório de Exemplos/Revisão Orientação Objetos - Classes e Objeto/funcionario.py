class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def aumentarSalario(self, porcentualDeAumento):
        self.salario = self.salario * (1+(porcentualDeAumento/100))

funcionario1 = Funcionario("José", 30000)

print(f"Salário atual: {funcionario1.salario}")

funcionario1.aumentarSalario(20)

print(f"Salário depois do aumento: {funcionario1.salario}")