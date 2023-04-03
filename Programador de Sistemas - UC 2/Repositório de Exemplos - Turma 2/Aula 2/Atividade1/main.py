import json

class Pessoa:
    def __init__(self,nome,idade):
        self._nome = nome
        self._idade = idade

caminho = "Atividade1/pessoa.json"

def salvarPessoaJson(novaPessoa):

    with open(caminho, "r") as pessoasJson:
        
        listaPessoas = json.load(pessoasJson)
        
    
    listaPessoas.append({'nome':novaPessoa._nome, 'idade':novaPessoa._idade})

    with open(caminho, "w") as pessoasJson:

        json.dump(listaPessoas,pessoasJson,indent=2)

def recuperarPessoasJson():

    with open(caminho, "r") as pessoasJson:
        
        listaPessoas = json.load(pessoasJson)

    listaObjetos = []

    for pessoa in listaPessoas:
        listaObjetos.append(Pessoa(pessoa['nome'],pessoa['idade']))

    return listaObjetos

pessoa1 = Pessoa("Sérgio", 35)

salvarPessoaJson(pessoa1)

listaDeObjetos = recuperarPessoasJson()

for pessoaObjeto in listaDeObjetos:
    print(pessoaObjeto._nome)
