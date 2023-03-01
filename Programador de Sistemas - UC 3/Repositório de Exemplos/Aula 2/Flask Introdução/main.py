from flask import Flask, render_template
import psycopg2

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/Pokemons")
def verPokemons():
    try:
        con = psycopg2.connect(database="Pokemon",user = "postgres",password = "postgres", host="localhost", port="5432")
        cursor = con.cursor()
        cursor.execute('''SELECT * FROM "Pokemons"
        ORDER BY "Id" ASC''')
        pokemons = cursor.fetchall()
        
        return render_template("pokemons.html", pokemons=pokemons)
    except(Exception, psycopg2.Error) as error:
        return f"Ocorreu um erro {error}"
    
@app.route("/Pokemons/Inserir")
def inserirPokemons():
    return render_template("inserirPokemons.html")

if __name__ == "__main__":
    app.run(debug=True)

