class Carro:

    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def informacoes(self):
        mensagem = f"{self.marca} - {self.modelo} - {self.ano}"
        return mensagem
    
    def acelerar(self, velocidade):

        print(f"O carro {self.marca} {self.modelo} acelerou para {velocidade}km/h")
        

meuCarro = Carro("Fiat","Uno",2000)

print(meuCarro.informacoes())

meuCarro.acelerar(80)