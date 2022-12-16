class Animal:
    def __init__(self,nome,cor):
        self._nome = nome
        self._cor = cor
    
    def comer(self):
        print(f"O {self._nome} está comendo")