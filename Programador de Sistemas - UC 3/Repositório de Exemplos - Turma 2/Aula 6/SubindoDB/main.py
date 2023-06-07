from Controle.classConexao import Conexao
import dotenv #pip install python-dotenv
import os

dotenv.load_dotenv()

conexaoBanco = Conexao(os.getenv("DBNAMEDB"), os.getenv("HOSTDB"), os.getenv("PORTDB"), os.getenv("USERNAMEDB"), os.getenv("PASSWORDDB"))

caminho = "C:\Tarik\Github\Programador-de-Sistema-SENAC\Programador de Sistemas - UC 3\Repositório de Exemplos - Turma 2\Aula 6\pokemonNovo.sql"

# conexaoBanco.manipularBanco(open(caminho, "r").read())

print("Upload Concluído")

print(conexaoBanco.consultarBanco('''SELECT * FROM "Pokedex"'''))