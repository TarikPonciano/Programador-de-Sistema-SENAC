from Controle.classConexao import Conexao
from Modelo.classFuncionario import Funcionario

import psycopg2

try:
    con = Conexao("Empresa", "localhost", "5432", "postgres", "postgres")


    listaFuncionarios = con.consultarBanco('''
    SELECT * FROM "Funcionarios"
    ORDER BY "ID" ASC
    ''')
    print("ID | Nome")
    for func in listaFuncionarios:
        print(f"{func[0]} - {func[1]} \n")

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
    print(con.consultarBanco('''Select * from "Funcionarios"'''))



    con._db.close()




    

except (Exception, psycopg2.Error) as error:
    print("Ocorreu um erro:", error)