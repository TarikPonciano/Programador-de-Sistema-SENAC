import classeAnimal

class Coelho(classeAnimal.Animal):
    def __init__(self, nome, cor):
        super().__init__(nome,cor)
    def correr(self):
        print(f"O {self._nome} está pulando.")

class Cachorro(classeAnimal.Animal):
    def __init__(self, nome, cor):
        super().__init__(nome,cor)
    def comer(self):
        print(f"O cachorro {self._nome} está comendo")

class Gato(classeAnimal.Animal):
    def __init__(self, nome, cor):
        super().__init__(nome,cor)
