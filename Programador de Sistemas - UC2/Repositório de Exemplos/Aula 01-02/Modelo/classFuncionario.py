class Funcionario:
    def __init__(self, id, nome, cpf, salario, idDepartamento):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.salario = salario
        self.idDepartamento = idDepartamento

    def imprimirFuncionario(self):

        print(f'''
        Informações do Funcionário:
        ID - {self.id}
        Nome - {self.nome}
        CPF - {self.cpf}
        Salario - {self.salario}
        ID Departamento - {self.idDepartamento}
        ''')

    def inserirFuncionario(self,tabela):
        codigoSql = f'''
        INSERT INTO "{tabela}"
        Values(default, '{self.nome}', '{self.cpf}', 
        '{self.salario}', '{self.idDepartamento}')
        '''
        return codigoSql
        