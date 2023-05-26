# Criar um site com 2 opções: Ver Pokemons e Inserir Pokemons

# Na página Ver Pokemons você deve mostrar uma lista de pokemons, de um banco de dados

# Na página Inserir Pokemons você deve criar um formulário e inserir o pokemon no banco de dados.

# --> Visualizar pokemons individualmente

# --> Faça um CRUD (Atualizar e Remover) os pokemons

# Recursos úteis:

#  - https://testdriven.io/tips/24431240-a8bf-437d-82ba-72507d4fb5a0/
#  - https://medium.com/trainingcenter/o-que-%C3%A9-uuid-porque-us%C3%A1-lo-ad7a66644a2b
#  - https://pythonexamples.org/python-flask-if-statement-in-html-template/
#  - https://stackoverflow.com/questions/7478366/create-dynamic-urls-in-flask-with-url-for


# from flask import *
# import psycopg2
# from Controle.classConexao import Conexao


# app = Flask(__name__)
# conexaoBanco = Conexao("Pokemon", "localhost", "5432", "postgres", "postgres")

# @app.route('/home')
# @app.route('/')
# def index():

#     return render_template("index.html")

# @app.route('/pokemons')
# def verPokemons():


#     pokemons = conexaoBanco.consultarBanco('''SELECT * FROM "Pokemons"
#     Order BY "Id" ASC ''')

#     if pokemons:

#         return render_template("pokemons.html", listaPokemons = pokemons)

#     else:
#         return "Ocorreu um erro"


# @app.route("/pokemons/inserir", methods=("GET","POST"))
# def inserirPokemons():

#     if request.method == "GET":

#         return render_template("inserirPokemon.html")

#     if request.method == "POST":


#         idPokemon = request.form['ID']
#         especiePokemon = request.form['ESPECIE']
#         pesoPokemon = request.form['PESO']
#         alturaPokemon = request.form['ALTURA']
#         tipoPokemon = request.form['TIPO']

#         resultado = conexaoBanco.manipularBanco(f'''INSERT INTO "Pokemons"
#         values('{idPokemon}','{especiePokemon}','{pesoPokemon}','{alturaPokemon}','{tipoPokemon}')''')

#         if resultado:
#             return redirect(url_for("verPokemons"))
#         else:
#             return "Erro na inserção"


# if __name__ == "__main__":
#     app.run(debug=True, port=5050)

from flask import *
from Controle.classConexao import Conexao
import env

conexaoBanco = Conexao(env.databaseName, env.hostName,
                       env.port, env.userName, env.password)

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/pokemons")
def verPokemons():
    resultado = conexaoBanco.consultarBanco('''Select * FROM "Pokemons"
    Order BY "Id" ASC''')

    if resultado:
        # return jsonify(resultado)
        return render_template("pokemons.html", listaPokemons=resultado)

    else:

        return "Ocorreu um erro", resultado


@app.route("/pokemons/inserir", methods=("GET", "POST"))
def inserirPokemon():

    if request.method == "GET":
        return render_template("inserirPokemon.html")

    if request.method == "POST":

        
        resultado = conexaoBanco.manipularBanco(f'''
            INSERT INTO "Pokemons"
            values('{request.form['ID']}', '{request.form['ESPECIE']}', '{request.form['PESO']}', '{request.form['ALTURA']}', '{request.form['TIPO']}'  )
            ''')
        
        if resultado:

            return redirect(url_for("verPokemons"))
        else:
            return "Erro na inserção"
        
@app.route("/pokemons/<int:idPokemon>")
def verPokemonEspecifico(idPokemon):
    
        resultado = conexaoBanco.consultarBanco(f'''SELECT * FROM "Pokemons"
        WHERE "Id" = '{idPokemon}' ''')

        if resultado:
            # return jsonify(resultado)

            return render_template("verPokemon.html",pokemon = resultado[0])
        
        else:

            return "Ocorreu um erro"



if __name__ == "__main__":

    app.run(debug=True, port=5050)
