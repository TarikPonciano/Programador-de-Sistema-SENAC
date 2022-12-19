class Pessoa:
    def __init__(self, idade):
        self._idade = idade

pessoa1 = Pessoa(20)

print(pessoa1._idade)