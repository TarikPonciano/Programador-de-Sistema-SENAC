from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

@app.route("/Pokemons", methods=["GET"])
def verPokemons():
    if request.method == "GET":
        try:
            con = psycopg2.connect(database = "Pokemon", host="localhost", port="5432", user="postgres", password="postgres")
            cursor = con.cursor()
            
            cursor.execute('''SELECT * FROM "Pokemons"
            ORDER BY "Id" ASC''')

            resultado = cursor.fetchall()

            return jsonify(resultado)
        except(Exception, psycopg2.Error) as error:
            return f"Ocorreu um erro {error}"

@app.route("/Pokemons/Inserir", methods=["POST"])
def inserirPokemons():
    if request.method == "POST":
        try:

            
            print(request.get_json())
            

            return "OK"
        except(Exception, psycopg2.Error) as error:
            return f"Ocorreu um erro {error}"
        
if __name__ == "__main__":
    app.run(debug=True)
        