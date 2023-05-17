class Treinador:

    def __init__(self, nome, listaPokemons):
        self.nome = nome
        self.listaPokemons = listaPokemons

    def capturar(self, pokemon):

        self.listaPokemons.append(pokemon)

        print("Você escolheu o", self.listaPokemons[-1].especie)
        meuPokemonInicial = self.listaPokemons[-1]
        print(f'''
        Número da Pokedex: {meuPokemonInicial.numero}
        Nome: {meuPokemonInicial.especie}
        Level: {meuPokemonInicial.level}
        HP: {meuPokemonInicial.hp}
        Atk: {meuPokemonInicial.atk}
        ''')

    def verPokemons(self):

        print("Seus pokemons:")
        if len(self.listaPokemons)>=1:
            for pokemon in self.listaPokemons:

                print(f'''
            Número da Pokedex: {pokemon.numero}
            Nome: {pokemon.especie}
            Level: {pokemon.level}
            HP: {pokemon.hp}
            Atk: {pokemon.atk}

    _____________________________________________________
            ''')
        else:
            print("Você não tem pokemons. Vá capturar algum.")

    def batalhaPokemon(self, pokemonInimigo):

        if len(self.listaPokemons) >= 1:
            print("Escolha um Pokemon para batalhar:")
            for i,pokemon in enumerate(self.listaPokemons):
                print(i,pokemon.especie)

            pokemonEscolhido = self.listaPokemons[int(input("Digite o pokemon escolhido:"))]

            resultado = pokemonEscolhido.batalhar(pokemonInimigo)

            print("Você", resultado)
        else:
            print("Você não tem pokemons. Vá capturar algum.")

