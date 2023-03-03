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



if __name__ == "__main__":
    app.run(debug=True)