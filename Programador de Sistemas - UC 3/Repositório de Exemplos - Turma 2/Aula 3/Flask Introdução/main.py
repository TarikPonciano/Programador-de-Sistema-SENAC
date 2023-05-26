# Criar um site com 2 opções: Ver Pokemons e Inserir Pokemons

# Na página Ver Pokemons você deve mostrar uma lista de pokemons, de um banco de dados

# Na página Inserir Pokemons você deve criar um formulário e inserir o pokemon no banco de dados.

# --> Visualizar pokemons individualmente

#Recursos úteis:

#  - https://testdriven.io/tips/24431240-a8bf-437d-82ba-72507d4fb5a0/
#  - https://medium.com/trainingcenter/o-que-%C3%A9-uuid-porque-us%C3%A1-lo-ad7a66644a2b
#  - https://pythonexamples.org/python-flask-if-statement-in-html-template/
#  - https://stackoverflow.com/questions/7478366/create-dynamic-urls-in-flask-with-url-for


from flask import *
import psycopg2

class Conexao:

    def __init__(self, dbname, host, port, user, password):
        self._dbname = dbname
        self._host = host
        self._port = port
        self._user = user
        self._password = password

    def consultarBanco(self, sql):
        try:
            con = psycopg2.connect(dbname=self._dbname, host=self._host, port = self._port, user = self._user, password = self._password)
            cursor = con.cursor()

            cursor.execute(sql)

            resultado = cursor.fetchall()

            

            cursor.close()
            con.close()


            return resultado
        except(Exception, psycopg2.Error) as error:
            print("Ocorreu um erro no objeto Conexão:", error)

            return False
        
    def manipularBanco(self, sql):
        try:
            con = psycopg2.connect(dbname=self._dbname, host=self._host, port = self._port, user = self._user, password = self._password)
            cursor = con.cursor()

            cursor.execute(sql)
            

            con.commit()

            cursor.close()
            con.close()

            return True
        except(Exception, psycopg2.Error) as error:
            print("Ocorreu um erro:", error)

            return False


app = Flask(__name__)
conexaoBanco = Conexao("Pokemon", "localhost", "5432", "postgres", "postgres")

@app.route('/')
def index():
    
    return render_template("index.html")

@app.route('/pokemons')
def verPokemons():


    pokemons = conexaoBanco.consultarBanco('''SELECT * FROM "Pokemons"
    Order BY "Id" ASC ''')

    if pokemons:

        return render_template("pokemons.html", listaPokemons = pokemons)
    
    else:
        return "Ocorreu um erro"
    
@app.route("/pokemons/inserir", methods=("GET","POST"))
def inserirPokemons():

    if request.method == "GET":

        return render_template("inserirPokemon.html")
    
    if request.method == "POST":

        
        idPokemon = request.form['ID']
        especiePokemon = request.form['ESPECIE']
        pesoPokemon = request.form['PESO']
        alturaPokemon = request.form['ALTURA']
        tipoPokemon = request.form['TIPO']

        resultado = conexaoBanco.manipularBanco(f'''INSERT INTO "Pokemons"
        values('{idPokemon}','{especiePokemon}','{pesoPokemon}','{alturaPokemon}','{tipoPokemon}')''')

        if resultado:
            return redirect(url_for("verPokemons"))
        else:
            return "Erro na inserção"


if __name__ == "__main__":
    app.run(debug=True, port=5050)