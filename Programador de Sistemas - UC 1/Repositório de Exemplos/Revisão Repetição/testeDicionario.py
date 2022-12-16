sala_de_aula = {
    "assentos":22,
    "computadores":22,
    "alunos":22,
}

print(sala_de_aula)

sala_de_aula["assentos"] = 18

print(sala_de_aula)

sala_de_aula["ar condicionado"] = 2

print(sala_de_aula)

sala_de_aula.pop("ar condicionado")

print(sala_de_aula) 

del sala_de_aula["computadores"]

print(sala_de_aula)

