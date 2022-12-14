# 1. Classe Triangulo: Crie uma classe que modele um triangulo:
# – Atributos: LadoA, LadoB, LadoC
# – Métodos: calcular Perímetro, getMaiorLado;
# Crie um programa que uFlize esta classe. Ele deve pedir ao usuário que informe as
# medidas de um triangulo. Depois, deve criar um objeto com as medidas e imprimir
# sua área e maior lado.

class Triangulo:
    def __init__(self, ladoA, ladoB, ladoC):
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC
        self.maiorLado = ""

    def calcularPerimetro(self):

        perimetro = self.ladoA + self.ladoB + self.ladoC
        return perimetro
    
    def getMaiorLado(self):

        if(self.ladoA >= self.ladoB and self.ladoA >= self.ladoC):
            self.maiorLado = self.ladoA
        elif(self.ladoB >= self.ladoA and self.ladoB >= self.ladoC):
            self.maiorLado = self.ladoB
        elif(self.ladoC >= self.ladoA and self.ladoC >= self.ladoB):
            self.maiorLado = self.ladoC
        else:
            self.maiorLado = "Alguns lados são iguais."

triangulo1 = Triangulo(8,8,7)

print(triangulo1.calcularPerimetro())

triangulo1.getMaiorLado()
print(triangulo1.maiorLado)
