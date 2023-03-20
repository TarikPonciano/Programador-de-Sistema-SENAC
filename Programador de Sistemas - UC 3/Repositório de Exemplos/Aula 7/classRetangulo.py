class Retangulo:
    def __init__(self,altura,largura):
        self.altura = altura
        self.largura = largura

    def area(self):
        area = self.altura * self.largura

        return area
    
    def informacoes(self):

        print(f"Teste {self.altura} {self.largura}")