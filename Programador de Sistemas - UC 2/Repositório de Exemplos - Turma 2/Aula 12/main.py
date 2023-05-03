from Controle.classConexao import Conexao

def criarTabelas(con):
    listaSql =['''
    CREATE TABLE "Clientes"(
    "ID" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "Nome" varchar(255) NOT NULL,
    "CPF" char(11) NOT NULL UNIQUE
    )
    ''',
    '''
    CREATE TABLE "Livros"(
    "ID" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "Nome" varchar(255) NOT NULL,
    "Autor" varchar(255) NOT NULL
    )
    ''',
    '''
    CREATE TABLE "Alugueis"(
    "ID" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "ID_Cliente" int NOT NULL,
    "ID_Livro" int NOT NULL,
    "Data do Aluguel" timestamp default CURRENT_TIMESTAMP(2),
    CONSTRAINT fk_cliente
        FOREIGN KEY("ID_Cliente")
        REFERENCES "Clientes"("ID")
        ,
    CONSTRAINT fk_livro
        FOREIGN KEY("ID_Livro")
        REFERENCES "Livros"("ID")

    )
    '''
    ]

    for sql in listaSql:
        
        if con.manipularBanco(sql):
            print("Tabela criada.")
        else:
            print("Falha na criação")


conexaoBanco = Conexao("Biblioteca", "localhost", "5432", "postgres", "postgres")

criarTabelas(conexaoBanco)


