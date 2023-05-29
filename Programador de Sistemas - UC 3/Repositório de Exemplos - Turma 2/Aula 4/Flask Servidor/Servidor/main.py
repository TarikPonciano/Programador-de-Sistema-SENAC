from flask import *
from Controle.classConexao import Conexao
import env

conexaoBanco = Conexao(env.databaseName, env.hostName,
                       env.port, env.userName, env.password)

app = Flask(__name__)

@app.route('/', methods=("GET", "POST"))
def index():

    if request.method == "GET":

        return jsonify({"instruções":"Converse com essa api enviando um JSON"})
    
    if request.method == "POST":

        resposta = request.get_json()

        resposta["mensagem"] = resposta["mensagem"] + "Prova de que deu certo"

        return jsonify(resposta)

@app.route('/pokemons', methods=("GET", "POST"))
def pokemons():
    if request.method == "GET":

        pokemons = conexaoBanco.consultarBanco('''
        SELECT * FROM "Pokemons"
        ORDER BY "Id" ASC ''')
        if pokemons:
            return jsonify(pokemons)
        else:
            return jsonify({'mensagem':'Deu ruim'})
        
    if request.method == "POST":
        
        pokemon = request.get_json() 

        resultado = conexaoBanco.manipularBanco(f'''
        INSERT INTO "Pokemons"
        values('{pokemon["meuPokemon"]["ID"]}','{pokemon["ESPECIE"]}', '{pokemon["PESO"]}', '{pokemon["ALTURA"]}', '{pokemon["TIPO"]}')
        
        ''')

        if resultado:
            return jsonify({'mensagem':"Deu certo"})
        else:
            return jsonify({'mensagem':"Deu errado"})
        

    


    
if __name__ == "__main__":
    app.run(debug=True, port=1234)