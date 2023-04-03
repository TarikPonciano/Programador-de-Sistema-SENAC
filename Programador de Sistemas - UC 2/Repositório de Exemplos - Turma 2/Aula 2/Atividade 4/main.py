import json

class Aluno:
    def __init__(self,nome, matricula, notas):
        self._nome = nome
        self._matricula = matricula
        self._notas = notas

    def gerarDicionario(self):

        dicionario = {
            "nome": self._nome,
            "matricula": self._matricula,
            "notas": self._notas
        }
        return dicionario

caminho = "Atividade 4/medias.json"

def salvarAlunoJson(novoAluno):

    listaAlunos = []

    with open(caminho,"r") as alunosJson:

        listaAlunos = json.load(alunosJson)

    novoAlunoDicionario = novoAluno.gerarDicionario()
    mediaAluno = sum(novoAluno._notas)/len(novoAluno._notas)
    novoAlunoDicionario["media"] = float(f"{mediaAluno:.2f}")

    listaAlunos.append(novoAlunoDicionario)

    with open(caminho,"w") as alunosJson:

        json.dump(listaAlunos, alunosJson, indent=2)


aluno1 = Aluno("José", "1234",[7,8,9.5])

salvarAlunoJson(aluno1)
