# Criar um site com 2 opções: Ver Pokemons e Inserir Pokemons

# Na página Ver Pokemons você deve mostrar uma lista de pokemons, de um banco de dados

# Na página Inserir Pokemons você deve criar um formulário e inserir o pokemon no banco de dados.




from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    
    return "Hello World"

@app.route('/home')
def home():
    
    return "Goodbye World"

if __name__ == "__main__":
    app.run(debug=True, port=5050)