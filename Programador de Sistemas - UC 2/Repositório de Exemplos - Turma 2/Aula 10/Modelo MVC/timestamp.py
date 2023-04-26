from Controle.classConexao import Conexao

conexaoBanco = Conexao("Loja Fictícia", "localhost", "5432", "postgres", "postgres")

listaCompras = conexaoBanco.consultarBanco('Select * FROM "Compras"')

for compra in listaCompras:

    print(f'''
    Id - {compra[0]}
    Quantidade - {compra[3]}
    Valor Total - R$ {compra[4]}
    Hora da Transação - {str(compra[5])}
    
    ''')