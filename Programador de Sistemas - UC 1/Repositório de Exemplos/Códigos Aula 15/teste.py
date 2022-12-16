class Pessoa:
    def __init__(self,idade):
        self.__idade = idade
    def getIdade(self):
        print(self.__idade)

p = Pessoa(20)

p.getIdade()