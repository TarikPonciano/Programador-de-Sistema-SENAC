import psycopg2
import requests

#Atividade:

#   - Requisitar os 151 primeiros pokemons
#   - Guardar num banco de dados postgres
#   - Atributos: Espécie, Altura, Peso, Tipo, ID e Região

def createTablePokemon():
    cursor = con.cursor()
    cursor.execute('''
    Create TABLE "Pokedex"(
    "Número Pokedex" integer PRIMARY KEY,
    "Espécie" varchar(255),
    "Altura" varchar(255),
    "Peso" varchar(255),
    "Tipo" varchar(255),
    "Região" varchar(255)
    )
    
    ''')

    con.commit()
    cursor.close()

try:
    con = psycopg2.connect(dbname="Pokemons", host="localhost",port="5432", user="postgres",password="postgres")

    for i in range(1,152):

        pokemon = requests.get(f"https://pokeapi.co/api/v2/pokemon/{i}")

        pokemonDict = pokemon.json()

        cursor = con.cursor()

        regiao = requests.get(requests.get(f"{pokemonDict['species']['url']}").json()['generation']['url']).json()['main_region']['name']

        tipos = ""

        for tipo in pokemonDict["types"]:
            tipos = tipos + tipo["type"]["name"] + " "

        cursor.execute(f'''INSERT INTO "Pokedex"
        values('{pokemonDict["id"]}', '{pokemonDict["name"]}', '{pokemonDict["height"]}', '{pokemonDict["weight"]}', '{tipos}','{regiao}')
          
            ''')
        
        print(pokemonDict["name"], "foi inserido.")
        con.commit()
        cursor.close()
        
    con.close()
except(Exception,psycopg2.Error) as error:
    print(error)