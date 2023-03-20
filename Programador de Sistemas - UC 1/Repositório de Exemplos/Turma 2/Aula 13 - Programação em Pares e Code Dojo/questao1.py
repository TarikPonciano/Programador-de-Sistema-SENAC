class Triangulo:
    def __init__(self, ladoA, ladoB, ladoC):
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC

    def calcularPerimetro(self):
        perimetro = self.ladoA + self.ladoB + self.ladoC
        return perimetro
    
    def getMaiorLado(self):
        #lados = [self.ladoA, self.ladoB, self.ladoC]
        #maior = max(lados)

        maior = self.ladoA

        if self.ladoB >= maior and self.ladoB >= self.ladoC:
            maior = self.ladoB
        elif self.ladoA >= self.ladoB and self.ladoA >= self.ladoC:
            maior = self.ladoA
        elif self.ladoC >= self.ladoB and self.ladoC >= maior:
            maior = self.ladoC

        return maior
    
lado1 = float(input("Digite o lado A"))
lado2 = float(input("Digite o lado B"))
lado3 = float(input("Digite o lado C"))

triangulo1 = Triangulo(lado1, lado2, lado3)

print("Perímetro",triangulo1.calcularPerimetro())

print("Maior lado", triangulo1.getMaiorLado())