class Animal:

    def __init__(self, nome, cor):
        self._nome = nome
        self._cor = cor

    def comer(self):

        print(f"O {self._nome} está comendo!")

    def mover(self):
        print(f"O {self._nome} saiu correndo!")


class Cachorro(Animal):

    def __init__(self, nome, cor):
        super().__init__(nome, cor)

class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

class Coelho(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
    def mover(self):
        print(f"{self._nome} saiu pulando!")

if __name__ == "__main__":
    cachorro = Cachorro("Pluto","Amarelo")
    coelho = Coelho("Hannah", "Branco")
    gato = Gato("Xanim", "Preto")
    cachorro.comer()
    gato.comer()
    coelho.comer()
    cachorro.mover()
    coelho.mover()
    gato.mover()
