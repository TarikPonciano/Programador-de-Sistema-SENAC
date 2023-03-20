class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def aumentarSalario(self, percentualDeAumento):
        self.salario = self.salario * (100 + percentualDeAumento)/100
        
    
harry = Funcionario("Harry", 25000)
harry.aumentarSalario(10)

print("Depois do aumento:", harry.salario)

harry.aumentarSalario(-20)

print(harry.salario)