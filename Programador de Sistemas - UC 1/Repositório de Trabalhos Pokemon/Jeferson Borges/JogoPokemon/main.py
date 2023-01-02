from pokedex import pokemons
from random import randint
import classPokemon

treinadorInimigo = []
pokemonsJogador = []
opcao = ''
vencedor = False

def pokemonsInimigos(treinadorInimigo):   #Laço for pra gerar a lista de 6 pokemons de cada treinador inimigo 
    for p in range(0, 3):
        pokemonAleatorio = pokemons[randint(0, 149)]        
        treinadorInimigo.append(classPokemon.adicionarClassePokemon(pokemonAleatorio))
    print(f'''Os pokemons do seu Inimigo são:
            1- {treinadorInimigo[0].getNome()}
            2- {treinadorInimigo[1].getNome()}
            3- {treinadorInimigo[2].getNome()}
            ''')
    return treinadorInimigo

def escolherPokemons(pokemonsJogador): #Função Jogador escolher seus pokemons!
    for p in range(0, 3):
        pokemonJogador = input(f'Digite o {p + 1}º pokemon da sua equipe: ').capitalize()
        for pokemon in pokemons:
            if pokemonJogador == pokemon['nome']:
                pokemonsJogador.append(classPokemon.adicionarClassePokemon(pokemon))                      
    
    while(len(pokemonsJogador) < 3):
        pokemonsJogador.clear()
        print("Algum dos pokemons não foi digitado corretamente!Escolha Novamente!")        
        escolherPokemons(pokemonsJogador)

    return pokemonsJogador

def evase(pokemonJogador, pokemonAdversario):
    sorteJogador = randint(0, 10)
    sorteInimigo = randint(0, 10)
    if sorteJogador > sorteInimigo:
        pokemonJogador.checarVantagem(pokemonAdversario)
    else:
        print("Errou o ataque!")

def escolherPokemon():
    controle = 0    
    while controle == 0:        
        pokemonEscolhido = input(f'''
        Escolha qual pokemon usar:
        1- {pokemonsJogador[0].getNome()}
        2- {pokemonsJogador[1].getNome()}
        3- {pokemonsJogador[2].getNome()}        
        4- Fugir
        ''')
        if pokemonEscolhido == '1' or pokemonEscolhido == '2' or pokemonEscolhido == '3':
            if pokemonsJogador[int(pokemonEscolhido) - 1]._hp == 0:
                print(f"{pokemonsJogador[int(pokemonEscolhido) - 1].getNome()} está desmaiado, não pode ser usado!")
            else:
                controle = 1
        elif pokemonEscolhido == '4':
            print("Você fugiu!")
            break        
        else:
            print("Opção Inválida!")
        
    return int(pokemonEscolhido)
            

def batalhaPokemon(pokemonInimigo):
    pokemonEscolhido = escolherPokemon()       
    while True:
        if pokemonEscolhido == 4:
            break
        pokemonEscolhido = pokemonsJogador[pokemonEscolhido - 1]     
        print(f"Você escolheu {pokemonEscolhido.getNome()}")
        opcao = ''    
        while(pokemonInimigo._hp > 0 or pokemonEscolhido._hp > 0):
            while opcao != '1' or opcao != '2':
                opcao = input('''
                        O que deseja realizar?
                        1- Atacar
                        2- Defender
                        ''')
                if opcao == '1':                
                    print(f"{pokemonEscolhido.getNome()} atacou {pokemonInimigo.getNome()}!")
                    evase(pokemonEscolhido, pokemonInimigo)                    
                    if pokemonInimigo._hp > 0:                
                        print(f"O HP de {pokemonInimigo.getNome()} é {pokemonInimigo._hp}")
                        break
                    else:
                        pokemonInimigo._hp = 0
                        print(f"O HP de {pokemonInimigo.getNome()} é {pokemonInimigo._hp}")
                        global vencedor                    
                        vencedor = True                    
                        return print("Você venceu!")
                elif opcao == '2':
                    print("Você vai tentar defender!")                
                else:
                    print("Opção inválida!")            
            print("Seu Inimigo está preparando para atacar...")    
            print(f"{pokemonInimigo.getNome()} atacou {pokemonEscolhido.getNome()}!")
            evase(pokemonInimigo, pokemonEscolhido)            
            if pokemonEscolhido._hp > 0:
                print(f"O HP de {pokemonEscolhido.getNome()} é {pokemonEscolhido._hp}")
            else:
                pokemonEscolhido._hp = 0
                print(f"O HP de {pokemonEscolhido.getNome()} é {pokemonEscolhido._hp}")                
                vencedor = False                
                return print("Você Perdeu!")  
                       
    
def batalhaInimigo(pokemonsJogador, treinadorInimigo):
    treinadorInimigo = []    
    pokemonsInimigos(treinadorInimigo)
    inimigoEscolhido = treinadorInimigo[randint(0, 2)]
    print(f"O Pokemon que seu inimigo escolhe é: \n{inimigoEscolhido.getNome()}")    
    batalhaPokemon(inimigoEscolhido)


def centroPokemon(pokemonsJogador):
    for p in range(0, 3):
        for pokemon in pokemons:
            if pokemonsJogador[p].getNome() == pokemon['nome']:
                pokemonsJogador[p]._hp = pokemon['hp']


def menu():
    opcaoMenu = ''
    while(opcaoMenu != '5'):
        opcaoMenu = input('''
        Digite a opção desejada: 
        1- Capturar Pokemon
        2- Procurar batalha pokemon
        3- Exibir seus pokemons
        4- Curar pokemons
        5- Sair
        ''')
        if opcaoMenu ==  '1':
            print("Caçando Pokemon...")
            pokemonSelvagem = pokemons[randint(0, 149)]
            pokemonSelvagem = classPokemon.adicionarClassePokemon(pokemonSelvagem)                       
            print(f"{pokemonSelvagem.getNome()} apareceu!")
            batalhaPokemon(pokemonSelvagem)
            if vencedor == True:
                print(f"Você capturou {pokemonSelvagem.getNome()}")
        elif opcaoMenu == '2':            
            print("Procurando Treinador pokemon...")
            print("Inimigo: - Prepara-se para batalha!")                        
            batalhaInimigo(pokemonsJogador, treinadorInimigo)
        elif opcaoMenu == '3':
            print(f'''
            Estes são os seus pokemons:
            1- {pokemonsJogador[0].getNome()}
            2- {pokemonsJogador[1].getNome()}
            3- {pokemonsJogador[2].getNome()}
            ''')
        elif opcaoMenu == '4':
            print("Curando pokemons...")
            centroPokemon(pokemonsJogador)
            print("Pokemons Curados!")
            print(f'''
            {pokemonsJogador[0].getNome()}: {pokemonsJogador[0]._hp}
            {pokemonsJogador[1].getNome()}: {pokemonsJogador[1]._hp}
            {pokemonsJogador[2].getNome()}: {pokemonsJogador[2]._hp}
            ''')
            
        elif opcaoMenu == '5':
            print("Fim de programa")            
        else:
            print("Opção Inválida! Tente novamente.")

                    
escolherPokemons(pokemonsJogador)

print(f'''
    Você escolheu:
    1- {pokemonsJogador[0].getNome()}
    2- {pokemonsJogador[1].getNome()}
    3- {pokemonsJogador[2].getNome()}
    ''')

menu()           