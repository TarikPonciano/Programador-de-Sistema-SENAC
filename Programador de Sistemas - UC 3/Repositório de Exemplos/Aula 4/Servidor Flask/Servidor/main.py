from flask import Flask, request, jsonify
from Controle.classConexao import Conexao
from Modelo.classPokemon import Pokemon

con = Conexao("Pokemon","localhost","5432","postgres","postgres")

app = Flask(__name__)

@app.route("/")
def home():
    return "Bem vindo a API de Pokemons"

@app.route("/Pokemons")
def verPokemons():

    resultado = con.consultarBanco('''Select * FROM "Pokemons"
    ORDER BY "Id" ASC''')

    if "Ocorreu um erro" in resultado:
        return resultado
    else:
        return jsonify(resultado)

@app.route("/Pokemons/<int:id_pokemon>")
def verPokemonEspecifico(id_pokemon):
    idPokemon = id_pokemon

    resultado = con.consultarBanco(f'''Select * FROM "Pokemons"
    WHERE "Id" = '{idPokemon}'
    ''')

    if "Ocorreu um erro" in resultado:
        return resultado
    elif resultado == []:
        return "Não há pokemons com este id."
    else:
        return jsonify(resultado)   
    
@app.route("/Pokemons/<int:id_pokemon>/update", methods=["Post"])
def atualizarPokemonEspecífico(id_pokemon):
    try:
        idPokemon = id_pokemon
        pokemon = request.get_json()
        con.manipularBanco(f'''Update "Pokemons"
        SET "Espécie" = '{pokemon[1]}' , "Altura" = '{pokemon[2]}', "Peso" = '{pokemon[3]}', "Tipo" = '{pokemon[4]}'
        WHERE "Id" = '{idPokemon}'
        
        ''')

        return "Ok"
    except:
        return "Not Ok"

@app.route("/Pokemons/<int:id_pokemon>/delete", methods=["Post"])
def deletarPokemonEspecífico(id_pokemon):
    
    idPokemon = id_pokemon

    
    con.manipularBanco(f'''DELETE FROM "Pokemons"
    WHERE "Id" = {idPokemon}''')

    return f"O pokemon de id {idPokemon} foi deletado"
    






if __name__ == "__main__":
    app.run(debug=True)