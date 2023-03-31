class Empresa:
    def __init__(self, listaFuncionarios):
        self._listaFuncionarios = listaFuncionarios
        self._funcionarioLogado = "Nenhum usuário logado"

    def getListaFuncionarios(self):
        return self._listaFuncionarios
    def setListaFuncionarios(self,listaFuncionarios):
        self._listaFuncionarios = listaFuncionarios

    def getFuncionarioLogado(self):
        return self._funcionarioLogado
    def setFuncionarioLogado(self, funcionarioLogado):
        self._funcionarioLogado= funcionarioLogado

    def loginFuncionario(self, login, senha):
        for funcionario in self._listaFuncionarios:
            if funcionario.getLogin() == login:
                if funcionario.getSenha() == senha:
                    self.setFuncionarioLogado(funcionario)
                    print(f"Logado como {self.getFuncionarioLogado().getNome()}")
                    return True
                else:
                    print(f"Você tentou logar como {login}, mas a senha está incorreta!")
                    return False
        else:
            print(f"Você tentou logar como {login} mas ele não existe")
            return False
        


    def imprimirFuncionarios(self):
        print("Método de impressão com contador")
        for i in range(len(self._listaFuncionarios)): #Método com contador
            
            print(f"{i+1} - {self._listaFuncionarios[i]._nome}")


        # print("Método de impressão percorrendo lista")
        # for func in self._listaFuncionarios: #Método percorrendo a lista
        #     print(f"{func._id} - {func._nome}")
    
    def visualizarFuncionario(self, idFuncionario):
        for func in self._listaFuncionarios:
            if str(func.getId()) == idFuncionario:
                func.mostrarInformacoes() #Tente fazer isto
                return "Funcionário Encontrado"
        else:
            print("O ID não existe na lista de funcionários.")

                