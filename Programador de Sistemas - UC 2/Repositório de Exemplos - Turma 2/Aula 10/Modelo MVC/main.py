from Controle.classConexao import Conexao
from Modelo.classCliente import Cliente
from Modelo.classCompra import Compra
from Modelo.classProduto import Produto

#Cenário: Biblioteca

# Construir um sistema de cadastro de aluguéis de livros.

# - Deve conter um banco com as seguintes tabelas: Clientes, Aluguéis e Livros
# - Deve conter as seguintes funcionalidades: Cadastro de Clientes, Cadastro de Aluguéis, Cadastro de Livros e Visualização dos dados das 3 tabelas.


import psycopg2

conexaoBanco = Conexao("Loja Fictícia", "localhost", "5432", "postgres", "postgres")

def criarTabelas():

    conexaoBanco.manipularBanco('''
    CREATE TABLE "Clientes"(
    "Id" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "Nome" varchar(255) NOT NULL
    )
    
    ''')

    conexaoBanco.manipularBanco('''
    CREATE TABLE "Produtos"(
    "Id" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "Nome" varchar(255) NOT NULL,
    "Preço" numeric(2) NOT NULL default 0,
    "Estoque" int NOT NULL default 0
    )
    
    ''')

    conexaoBanco.manipularBanco('''
    CREATE TABLE "Compras"(
    "Id" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "Id_Cliente" int,
    "Id_Produto" int,
    "Quantidade" int NOT NULL default 1,
    "Valor Total" numeric(2) NOT NULL,
    "Horário" timestamp default CURRENT_TIMESTAMP(0),
    CONSTRAINT fk_cliente
        FOREIGN KEY("Id_Cliente")
        REFERENCES "Clientes"("Id")
        ,

    CONSTRAINT fk_produto
        FOREIGN KEY("Id_Produto")
        REFERENCES "Produtos"("Id")

    )
    
    
    ''')

    print("Tabelas cadastradas!")

def cadastrarCliente():
    print("Cadastro de Cliente")

    cliente = Cliente(None, input("Digite o nome do cliente: "))

    conexaoBanco.manipularBanco(cliente.sqlInserirCliente())

    print("Cliente Cadastrado")

def cadastrarProduto():
    print("Cadastro de Produto")

    novoProduto = Produto(None, input("Digite o nome do produto: "),input("Digite o preço do produto:"), input("Digite o estoque do produto:"))

    conexaoBanco.manipularBanco(novoProduto.sqlInserirProduto())

    print("Produto Cadastrado")

def cadastrarCompra():
    print("Cadastro de Compra")

    novaCompra = Compra(None, input("Digite o id do Cliente:"), input("Digite o id do Produto:"), input("Digite quantos produtos serão comprados:"), None, None)

    produtoEscolhido = conexaoBanco.consultarBanco(f'''
    SELECT * FROM "Produtos"
    WHERE "Id" = {novaCompra._idProduto}
    ''')[0]

    produto = Produto(produtoEscolhido[0], produtoEscolhido[1], produtoEscolhido[2], produtoEscolhido[3])

    if int(produto._estoque) < int(novaCompra._quantidade):
        print("Não há estoque suficiente.")
        return "Não há estoque suficiente."
    else: 
        produto._estoque = int(produto._estoque) - int(novaCompra._quantidade)

    novaCompra._valorTotal = float(produto._preço) * float(novaCompra._quantidade)

    conexaoBanco.manipularBanco(novaCompra.sqlInserirCompra())

    conexaoBanco.manipularBanco(produto.sqlAtualizarProduto())

    print(f"Compra de {novaCompra._quantidade} {produto._nome} por R$ {novaCompra._valorTotal} foi cadastrada")


while True:
    try:
        print('''Bem vindo a Loja FICTÍCIA: Onde tudo é de mentira
        
        Menu:

            1. Cadastrar Cliente
            2. Cadastrar Produto
            3. Cadastrar Compra
            0. Sair
        
        
        ''')    
        op = input("Digite uma das opções:")
        
        match op:
            case "1":
                cadastrarCliente()
            case "2":
                cadastrarProduto()
            case "3":
                cadastrarCompra()
            case "0":
                print("Saindo...")
                break
            case _:
                print("Opção inválida!")

        input("Digite Enter para continuar.")

    except(Exception, psycopg2.Error) as error:
        print(error)