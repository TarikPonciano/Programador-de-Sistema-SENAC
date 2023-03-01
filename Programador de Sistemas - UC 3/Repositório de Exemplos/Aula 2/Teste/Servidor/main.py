from flask import Flask, render_template
import json
import psycopg2



app = Flask(__name__)


@app.route("/")
def index():

    try:
        con = psycopg2.connect(database = "Pokemon", host = "localhost", port="5432", user= "postgres", password = "postgres")
        cursor = con.cursor()

        cursor.execute('''
        Select * FROM "Pokemons"
        ORDER BY "Id" ASC
        ''')

        resultado = cursor.fetchall()

        return render_template("index.html",pokemons=resultado)
    except(Exception,psycopg2.Error) as error:

        return f"Aconteceu um erro {error}"

@app.route("/Pokemons")
def verPokemons():

    try:
        con = psycopg2.connect(database = "Pokemon", host = "localhost", port="5432", user= "postgres", password = "postgres")
        cursor = con.cursor()

        cursor.execute('''
        Select * FROM "Pokemons"
        ORDER BY "Id" ASC
        ''')

        resultado = cursor.fetchall()

        return json.dumps(resultado)
    
    except(Exception,psycopg2.Error) as error:

        return f"Aconteceu um erro {error}"


if __name__ == "__main__":
    app.run()
