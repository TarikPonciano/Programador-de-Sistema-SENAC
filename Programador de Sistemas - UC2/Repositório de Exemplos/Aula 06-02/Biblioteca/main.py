#Aula 06-02
#Conteúdo: Revisão Geral de Implementação de Banco de Dados com Python
#Programa: Sistema de Gerenciamento de Biblioteca
#Objetivos:
#   - Criar modelo físico de dados
#   - Entidades: Livros e Clientes Relacionamentos: Aluguel
#   - Criar banco de dados e tabelas
#   - Integrar banco com Python e criar funções de manipulação das tabelas


def criarBancoDeDados(conexao):
    conexao.manipularBanco('''
    DROP DATABASE IF EXISTS "Biblioteca" ;
    CREATE DATABASE "Biblioteca";
    ''')

def criarTabelaCliente(conexao):
    conexao.manipularBanco('''
    DROP TABLE IF EXISTS "Cliente";
    CREATE TABLE "Cliente"(
        "ID" int GENERATED ALWAYS AS IDENTITY,
        "Nome" varchar(255) NOT NULL,
        "CPF" char(11) NOT NULL UNIQUE,
        Primary Key("ID")
    );
    ''')

def criarTabelaLivro(conexao):

    conexao.manipularBanco('''
    DROP TABLE IF EXISTS "Livro";
    CREATE TABLE "Livro(
        "ID" int GENERATED ALWAYS AS IDENTITY,
        "Nome" varchar(255) NOT NULL,
        "Autor" varchar(255) NOT NULL,
        Primary Key("ID")
    );
    ''')

def criarTabelaAluguel(conexao):

    conexao.manipularBanco('''
    DROP TABLE IF EXISTS "Aluguel";
    CREATE TABLE "Aluguel"(
        "ID" int GENERATED ALWAYS AS IDENTITY,
        "ID_Cliente" int NOT NULL,
        "ID_Livro" int NOT NULL,
        "Data_Aluguel" timestamp default current_timestamp,
        Primary Key("ID"),
        Constraint fk_cliente
            Foreign Key ("ID_Cliente")
            References "Cliente"("ID")
            ON DELETE CASCADE
            ON UPDATE NO ACTION
            ,
        Constraint fk_livro
            Foreign Key ("ID_Livro")
            Refereces "Livro"("ID")
            ON DELETE SET NULL
            ON UPDATE NO ACTION
            
    );
    ''')
