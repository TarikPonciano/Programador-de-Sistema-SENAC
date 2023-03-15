class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo
        self.departamento = 10

    def dizerOla(self, codigo):
        print("Olá, meu nome é",self.nome,"e meu salário é", self.salario, codigo)

    def dizerAdeus(self):
        pass



funcionario1 = Funcionario("Jonas", "+ de 8000","Assistente")

funcionario2 = Funcionario("Marcos",2000, "Vendedor")

funcionario3 = Funcionario(cargo="Advogado", salario= 5000, nome="João")

funcionario1.dizerOla(300)

funcionario2.dizerOla(200)
        