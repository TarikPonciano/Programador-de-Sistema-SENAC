class Funcionario:
    def __init__(self,id, nome, cpf, salario, cargo):
        self._id = id
        self._nome = nome
        self._cpf = cpf
        self._salario = salario
        self._cargo = cargo
    
    def getId(self):
        return self._id
    def setId(self, id):
        self._id = id
    
    def getNome(self):
        return self._nome
    def setNome(self, nome):
        self._nome = nome

    def getCpf(self):
        return self._cpf
    def setCpf(self, cpf):
        self._cpf = cpf

    def getSalario(self):
        return self._salario
    def setSalario(self,salario):
        self._salario = salario

    def getCargo(self):
        return self._cargo
    def setCargo(self, cargo):
        self._cargo = cargo

    def getLogin(self):
        return "Este usuário não possui login"

    def mostrarInformacoes(self):
        print(f"""
        ID: {self._id}
        Nome: {self._nome}
        Cpf: {self._cpf}
        Salário: R$ {self._salario}
        Cargo: {self._cargo}
        """)

class Gerente(Funcionario):
    def __init__(self, id, nome, cpf, salario, cargo, login, senha):
        super().__init__(id, nome, cpf, salario, cargo)
        self._login = login
        self._senha = senha
    
    def getLogin(self):
        return self._login
    def setLogin(self, login):
        self._login = login

    def getSenha(self):
        return self._senha
    def setSenha(self, senha):
        self._senha = senha
        