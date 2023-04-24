# Funcionarios:

# Func_id - int GENERATED ALWAYS AS IDENTITY PRIMARY KEY
# Func_nome - varchar(255)
# Func_cpf - char(11) #UNIQUE NOT NULL#
# Func_salario - money
# Dept_id - int
# CONSTRAINT fk_departamento
#   FOREIGN KEY ("ID_Dept")
#   REFERENCES "Departamento"("ID")
#   ON DELETE CASCADE, SET NULL, SET DEFAULT, NO ACTION
#   ON UPDATE NO ACTION

# Departamentos:

# Dept_id - int GENERATED ALWAYS AS IDENTITY PRIMARY KEY
# Dept_nome - varchar(255)

'''Atividade para casa:
Crie uma banco de dados de uma Biblioteca que deverá conter a seguinte tabela:

Livros:

Livro_id (PK)
Livro_nome
Livro_paginas
Livro_anoLançamento
Livro_autor (FK)

Autores:

Autor_id (PK)
Autor_nome

Conecte as duas tabelas usando a chave Livro_autor como chave estrangeira.
Dica: Se você já tiver criado a tabela Livros, use o comando ALTER

'''