from Controle.classConexao import Conexao
from Modelo.classFuncionario import Funcionario

#Aplicar a estrutura Modelo, Visualização, Controle ao projeto Biblioteca das aulas 27-01 e 30-01
#Criar classe Livro, criar classe Conexão
#Replicar o código abaixo para atualizar Livros no seu banco de dados


import psycopg2

def mostrarFuncionarios(conexao):

    listaFuncionarios = conexao.consultarBanco('''
    SELECT * FROM "Funcionarios"
    ORDER BY "ID" ASC
    ''')
    print("ID | Nome")
    for func in listaFuncionarios:
        print(f"{func[0]} - {func[1]} \n")

try:
    con = Conexao("Empresa", "localhost", "5432", "postgres", "postgres")

    mostrarFuncionarios(con)

    funcionarioEscolhido = input("Escolha o id do funcionario que deseja alterar: ")

    funcionarioConsulta = con.consultarBanco(f'''
    SELECT * FROM "Funcionarios"
    WHERE "ID" = '{funcionarioEscolhido}'
    ''')
    funcionario = Funcionario(funcionarioConsulta[0][0], funcionarioConsulta[0][1], funcionarioConsulta[0][2], funcionarioConsulta[0][3], funcionarioConsulta[0][4])

    print("Funcionario escolhido foi:")
    print(funcionario.imprimirFuncionario())

    opcoes = input("Você deseja alterar as informações basicas(1) ou o departamento(2)?")

    match opcoes:
        case "1":
            funcionario.nome = input("Escreva o novo nome: ")
            funcionario.cpf = input("Escreva o novo cpf: ")
            funcionario.salario = input("Escreva o novo salário: ")

            con.manipularBanco(funcionario.atualizarFuncionario("Funcionarios"))
        case "2": 
            funcionario.idDepartamento = input("Insira o id do novo Departamento")
            con.manipularBanco(funcionario.atualizarDepartamentoFuncionario("Funcionarios"))

    print(funcionario.imprimirFuncionario())

    mostrarFuncionarios(con)

    con._db.close()




    

except (Exception, psycopg2.Error) as error:
    print("Ocorreu um erro:", error)