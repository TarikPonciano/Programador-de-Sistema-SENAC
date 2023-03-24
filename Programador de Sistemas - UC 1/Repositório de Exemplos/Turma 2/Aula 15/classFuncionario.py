class Funcionario:
    def __init__(self, nome, cpf, salario):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario
    
    def getCpf(self):

        return self._cpf
    
    def setCpf(self, novoCpf):

        valido = self._validarCpf(novoCpf)
        
        if(valido):
            print("CPF Válido")
            self._cpf = novoCpf
        else:
            print("CPF Inválido")
    
    def _validarCpf(self, cpf):

        if len(cpf) != 11:
            return False
        else:
            return True

        

if __name__ == "__main__":
    novoFuncionario = Funcionario("José","123456",4000)
    
    novoFuncionario.setCpf("123450")

    print(novoFuncionario.getCpf())

    