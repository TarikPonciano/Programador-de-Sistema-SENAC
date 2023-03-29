class Funcionario:
    def __init__(self,nome,salario):
        self._nome = nome
        self._salario = salario

    def getSalario(self, senha, cifrao):
        if senha == "12345":
            if cifrao:
                return f"R$ {self._salario}"
            else:
                return self._salario
        else:
            return "Senha inválida"
        
    def getNome(self):
        return self._nome
    
    def setSalario(self,novoSalario):
        self._salario = novoSalario
    
funcionario1 = Funcionario("Mario", 5000)

funcionario1._salario = 3000