from Controle.classConexao import Conexao
import dotenv #pip install python-dotenv
import os

dotenv.load_dotenv()

conexaoBanco = Conexao(os.getenv("DBNAMEDB"), os.getenv("HOSTDB"), os.getenv("PORTDB"), os.getenv("USERNAMEDB"), os.getenv("PASSWORDDB"))

print(conexaoBanco.consultarBanco('''SELECT version()'''))