import random

class Pokemon:
    def __init__(self, especie, ataque, defesa, hp):
        self.especie = especie
        self.ataque = ataque
        self.defesa = defesa
        self.hp = hp

        match self.especie:
            case "Charmander":
                self.tipo = "Fogo"
            case "Bulbasauro":
                self.tipo = "Grama"
            case "Squirtle":
                self.tipo = "Água"
            case _:
                self.tipo = "Normal"

    def batalhaSimples(self, oponente):

        vantagem = 1
        
        if self.tipo == "Fogo":
            match oponente.tipo:
                case "Fogo":
                    vantagem = 1
                case "Água":
                    vantagem = 0.5
                case "Grama":
                    vantagem = 2
                case _:
                    vantagem = 1
        elif self.tipo == "Grama":
            match oponente.tipo:
                case "Fogo":
                    vantagem = 0.5
                case "Água":
                    vantagem = 2
                case "Grama":
                    vantagem = 1
                case _:
                    vantagem = 1
        else:
            match oponente.tipo:
                case "Fogo":
                    vantagem = 2
                case "Água":
                    vantagem = 1
                case "Grama":
                    vantagem = 0.5
                case _:
                    vantagem = 1

        

        poder = (self.ataque + self.defesa + self.hp) * vantagem
        poderOponente = oponente.ataque + oponente.defesa + oponente.hp

        if poder > poderOponente:
            print(f"{self.especie} ganhou com {poder}")
        elif poder < poderOponente:
            print(f"{oponente.especie} ganhou com {poderOponente}")
        else:
            print("Empate")

pokemon1 = Pokemon("Charmander", 100,50,300)
pokemon2 = Pokemon("Bulbasauro", 150,20,400)
pokemon3 = Pokemon("Squirtle", 200, 60, 250)


print('''Escolha seu pokemon
1. Charmander
2. Bulbasauro
3. Squirtle


''')

opcoes = input("Digite o número do pokemon escolhido:")

match opcoes:
    case "1":
        pokemonEscolhido = pokemon1
    case "2":
        pokemonEscolhido = pokemon2
    case "3":
        pokemonEscolhido = pokemon3
    case _:
        print("Digite uma opção válida")

print("Você escolheu", pokemonEscolhido.especie)

pokemonOponente = random.choice([pokemon1,pokemon2,pokemon3])

print("O oponente escolheu", pokemonOponente.especie)

pokemonEscolhido.batalhaSimples(pokemonOponente)



