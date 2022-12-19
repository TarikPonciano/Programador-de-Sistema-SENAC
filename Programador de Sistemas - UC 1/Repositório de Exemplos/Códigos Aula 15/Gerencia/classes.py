class Funcionario:
    def __init__ (self, nome, cpf, salario):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario

    def getNome(self):
        return self._nome
    def setNome(self, novoNome):
        self._nome = novoNome

    def getcpf(self):
        return self._cpf
    def setCpf(self, novoCpf):
        self._cpf = novoCpf

    def getSalario(self):
        return self._salario
    def setSalario(self, novoSalario):
        self._salario = novoSalario

class Gerente(Funcionario):
    def __init__(self, nome, cpf, salario,senha, listaFuncinarios):
        super().__init__(nome, cpf, salario)
        self._senha = senha
        self._listaFuncionarios = listaFuncinarios
    
    def adicionarFuncionario(self, funcionario):
        senha = input(f"Digite sua senha para adicionar o funcionario {funcionario.getNome()}: ")

        if(senha == self._senha):
            self._listaFuncionarios.append(funcionario)
            print(f"Você adicionou o funcionario {funcionario._nome}")

        else:
            print("Senha incorreta!")

    def removerFuncionario(self):
        nomeFuncionario = input("Digite o nome do funcionário que você quer remover: ")
        senha = input(f"Digite sua senha para remover o funcionario {nomeFuncionario}")

        if (senha == self._senha):
            for i in range(len(self._listaFuncionarios)):
                if self._listaFuncionarios[i].getNome() == nomeFuncionario:
                    self._listaFuncionarios.pop(i)
                    print("O funcionário foi removido")
                    return "Funcionário removido com sucesso"
            else:
                print("Funcionário não foi encotrado.")
        else:
            print("Senha incorreta!")

    def getListaFuncionarios(self):
        return self._listaFuncionarios
    
    def getNomesFuncionarios(self):
        nomesFuncionarios = []
        for n in self._listaFuncionarios:
            nomesFuncionarios.append(n.getNome())
        return nomesFuncionarios

if __name__ == "__main__":

    funcionario1 = Funcionario("Maria", "123123", 1500)
    funcionario2 = Funcionario("João", "123123", 1500)

    gerente = Gerente("Robson", "111.111.111-11", 3000, "1234", [funcionario1,funcionario2])
    print(gerente.getListaFuncionarios())
    print(gerente.getNomesFuncionarios())
    funcionario3 = Funcionario("Maxwel", "023012312", 2000)
    gerente.adicionarFuncionario(funcionario3)
    print(gerente.getListaFuncionarios())
    print(gerente.getNomesFuncionarios())
    gerente.removerFuncionario()
    print(gerente.getNomesFuncionarios())