from Controle.classConexao import Conexao
from Modelo.classFuncionario import Funcionario

#Aplicar a estrutura Modelo, Visualização, Controle ao projeto Biblioteca das aulas 27-01 e 30-01
#Criar classe Livro, criar classe Conexão
#Replicar o código abaixo para atualizar Livros no seu banco de dados


import psycopg2

def mostrarFuncionarios(conexao):

    listaFuncionarios = conexao.consultarBanco('''
    SELECT "ID", "Nome" FROM "Funcionarios"
    ORDER BY "ID" ASC
    ''')
    print("ID | Nome")
    for func in listaFuncionarios:
        print(f"{func[0]} - {func[1]} \n")

def menuAlterarFuncionario(conexao):

    print('''
    Escolha o que deseja fazer:

    1. Atualizar funcionário

    2. Remover funcionário
    
    ''')

    opcoes = input("Digite o numero da opção desejada: ")

    match opcoes:
        case "1":
            funcionarioEscolhido = input("Escolha o id do funcionario que deseja alterar: ")
            funcionarioConsulta = conexao.consultarBanco(f'''
            SELECT * FROM "Funcionarios"
            WHERE "ID" = {funcionarioEscolhido}
            ''')[0]
            funcionario = Funcionario(funcionarioConsulta[0],funcionarioConsulta[1],funcionarioConsulta[2],funcionarioConsulta[3],funcionarioConsulta[4])
            opcoes = input("Você desejar alterar Informações básicas(1) ou o Departamento(2)?")
            match opcoes:
                case "1":
                    funcionario.nome = input("Digite o nome do funcionário: ")
                    while(True):

                        if(funcionario.setCpf(input("Digite o cpf: "))):
                            break
                        else:
                            pass
                    funcionario.salario = input("Digite o salario do funcionario:")
                    conexao.manipularBanco(funcionario.atualizarFuncionario("Funcionarios"))
                case "2":
                    funcionario.idDepartamento = input("Digite o id do departamento:")

                    conexao.manipularBanco(funcionario.atualizarDepartamentoFuncionario("Funcionarios"))

        case "2":
            funcionarioEscolhido = input("Escolha o id do funcionario que deseja remover: ")
            conexao.manipularBanco(f'''
            DELETE FROM "Funcionarios"
            WHERE "ID" = '{funcionarioEscolhido}'
            
            ''')
def pesquisarFuncionario(conexao):
    print('''
    Menu de Pesquisa:

    1. Pesquisar pelo Nome
    2. Pesquisar pelo Primeiro Nome
    3. Pesquisar pelo Salário
    4. Pesquisar pelo Salário maior que o escolhido
    
    ''')

    opcoes = input("Digite a opção desejada:")

    match opcoes:
        case "1":
            nomeEscolhido = input("Digite o nome que deseja pesquisar:")
            print(conexao.consultarBanco(f'''
            SELECT * FROM "Funcionarios"
            WHERE "Nome" = '{nomeEscolhido}'
            
            '''))
        case "2":
            nomeEscolhido = input("Digite o nome que deseja pesquisar:")
            print(conexao.consultarBanco(f'''
            SELECT * FROM "Funcionarios"
            WHERE "Nome" LIKE '{nomeEscolhido}%'
            
            '''))
        case "3":
            salarioEscolhido = input("Digite o salario que deseja pesquisar:")
            print(conexao.consultarBanco(f'''
            SELECT * FROM "Funcionarios"
            WHERE "Salário" = '{salarioEscolhido}'
            
            '''))
        case "4":
            salarioEscolhido = input("Digite o salario que deseja pesquisar:")
            print(conexao.consultarBanco(f'''
            SELECT * FROM "Funcionarios"
            WHERE "Salário" > '{salarioEscolhido}'
            
            '''))



                


                

    
            

def inserirFuncionario(conexao):
    funcionario = Funcionario(None,None,None,None,None)
    funcionario.nome = input("Digite o nome do funcionário: ")
    while(True):

        if(funcionario.setCpf(input("Digite o cpf: "))):
            break
        else:
            pass
    # while(True):
    #     funcionario.setCpf(input("Digite o CPF"))

    #     if funcionario.cpf != None:
    #         break
    #     else:
    #         pass
    funcionario.salario = input("Digite o salário do funcionário: ")
    funcionario.idDepartamento = input("Digite o id do departamento desse funcionario: ")

    print("Funcionário válido.")

    conexao.manipularBanco(funcionario.inserirFuncionario("Funcionarios"))

try:
    con = Conexao("Empresa", "localhost", "5432", "postgres", "postgres")

    print('''
    Bem vindo à empresa "Empresa"
    
    Menu:

    1. Ver funcionários
    2. Inserir um funcionário
    3. Ver departamentos (Não implementado)
    4. Inserir um departamento (Não implementado)
    5. Pesquisar Funcionarios
    0. Sair
    
    ''')

    opcoes = input("Digite o número da opção escolhida:")

    match opcoes:
        case "1":
            mostrarFuncionarios(con)
            menuAlterarFuncionario(con)
        case "2":
            inserirFuncionario(con)
        # case "3":
        #     mostrarDepartamentos(con)
        # case "4":
        #     inserirDepartamento(con)
        case "5":
            pesquisarFuncionario(con)
        case _: 
            print("Opção inválida")

    # 

    # print(funcionario.imprimirFuncionario())

    # mostrarFuncionarios(con)

    con._db.close()




    

except (Exception, psycopg2.Error) as error:
    print("Ocorreu um erro:", error)