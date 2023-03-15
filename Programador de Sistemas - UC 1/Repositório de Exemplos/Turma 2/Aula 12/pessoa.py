class Pessoa:
    def __init__(self, nome, genero, cpf, ativo):
        self.nome = nome
        self.genero = genero
        self.cpf = cpf
        self.ativo = ativo
    
    def desativar(self):
        self.ativo = False
        print("A pessoa foi desativada com sucesso.")

    def setCpf(self, novoCpf):
        #Validar CPF
        self.cpf = novoCpf

pessoa1 = Pessoa("Julin", "M", "12345", True)

pessoa1.setCpf(123456)

print(pessoa1.ativo)

pessoa1.desativar()
