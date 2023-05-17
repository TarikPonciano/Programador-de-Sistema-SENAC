class Pokemon:

    def __init__(self, numero, especie, level, hp, atk):
        self.numero = numero
        self.especie = especie
        self.level = level
        self.hp = hp
        self.atk = atk

    def batalhar(self, pokemonInimigo):

        hpAtual = self.hp
        hpAtualInimigo = pokemonInimigo.hp

        while True:
            
            hpAtualInimigo = hpAtualInimigo - (0.1*self.atk)
            print(f"{self.especie} causou {self.atk} de dano em {pokemonInimigo.especie}")
            print(f"{pokemonInimigo.especie} tem {hpAtualInimigo} hp restante")    

            if hpAtualInimigo<=0:
                return "Venceu"

            hpAtual = hpAtual - (0.1 * pokemonInimigo.atk)
            print(f"{pokemonInimigo.especie} causou {pokemonInimigo.atk} de dano em {self.especie}")
            print(f"{self.especie} tem {hpAtual} restante") 

            if hpAtual<=0:
                return "Perdeu"
            
            input("Digite enter para continuar")
            
        

            

        


