class Funcionario:
    def __init__(self, nome, cpf, salario):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario

    def getNome(self):
        return self._nome
    
    def setNome(self, novoNome):
        self._nome = novoNome

    def getSalario(self):
       
        return self._salario
    
    def setSalario(self,novoSalario):

        if novoSalario < 0:
            print("Salário digitado está abaixo do mínimo")

        else:
            self._salario = novoSalario



funcionario1 = Funcionario("Jefferson", "111222333444", 5000)


funcionario1.setSalario(-7000)

print(funcionario1.getSalario())