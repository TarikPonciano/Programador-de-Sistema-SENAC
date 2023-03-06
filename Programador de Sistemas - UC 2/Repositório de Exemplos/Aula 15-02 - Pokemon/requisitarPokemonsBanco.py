import psycopg2
import requests

def criarDB(conexao):

    cursor = conexao.cursor()

    cursor.execute('''
    CREATE DATABASE "Pokemon"
    ''')

    conexao.commit()
    cursor.close()

def criarTabelaPokemons(conexao):

    cursor = conexao.cursor()

    cursor.execute(f'''
    CREATE TABLE "Pokemons"(
        "Id" int UNIQUE NOT NULL,
        "Espécie" varchar(255) NOT NULL,
        "Peso" float,
        "Altura" float,
        "Tipo" varchar(255) NOT NULL,
        Primary Key ("Id")
    );
    ''')
    conexao.commit()
    cursor.close()
    

def consultarBanco(conexao,sql):

    cursor = conexao.cursor()

    cursor.execute(sql)

    resultado = cursor.fetchall()

    cursor.close()

    return resultado

def manipularBanco(conexao,sql):

    cursor = conexao.cursor()

    cursor.execute(sql)

    conexao.commit()

    cursor.close()


    



try:
    con = psycopg2.connect(host="localhost",port="5432",database ="Pokemon",user="postgres",password="postgres")
    
    for i in range(1,152):
        try:
            requisicao = requests.get(f"https://pokeapi.co/api/v2/pokemon/{i}")

            pokemon = requisicao.json()

            tipos = "" #pokemon['types'][0]['type']['name']

            for tipo in pokemon['types']:
                tipos = tipos + '/' + tipo['type']['name']
            
            consulta = f'''
            INSERT INTO "Pokemons"
            Values('{pokemon['id']}','{pokemon['name']}', '{pokemon['weight']}', '{pokemon['height']}', '{tipos}')
            
            
            '''


            manipularBanco(con,consulta)

            print(requisicao.json())
        except:
            print("O pokemon já existe")

    con.close()

except(Exception,psycopg2.Error,requests.ConnectionError,requests.JSONDecodeError) as error:
    print("Ocorreu um erro - ", error)