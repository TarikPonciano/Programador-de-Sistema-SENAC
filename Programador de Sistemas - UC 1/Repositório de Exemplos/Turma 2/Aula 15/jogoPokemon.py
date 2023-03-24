from classPokemon import *

meuCharmander = PokemonFogo("Charmander", "Fogo", 200, "Lança Chamas")
meuSquirtle = PokemonAgua("Squirtle", "Água", 300, "Jato d'água")
meuBulbasauro = PokemonGrama("Bulbasauro","Grama",400,"Chicotada")
meuCharmander.fazerBarulho()
meuCharmander.batalha(meuSquirtle)
meuSquirtle.batalha(meuCharmander)
meuBulbasauro.batalha(meuCharmander)