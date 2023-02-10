class Funcionario:

    def __init__(self,id,nome,cpf,idade):
        self._id = id
        self._nome = nome
        self._cpf = cpf
        self._idade = idade

    def inserirFuncionario(self, tabela):
        sql = f'''
        INSERT INTO "{tabela}"
        Values({self._id},'{self._nome}','{self._cpf}','{self._idade}')
        '''

        return sql