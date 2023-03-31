"""https://github.com/TarikPonciano/Programador-de-Sistema-SENAC
Criar software de gerenciamento de funcionários

1. Modelar a classe Funcionário e a classe Gerente com base no 
modelo disponível em banco.json. Fazer os metodos get e set

2. Modelar a classe Empresa:
    - Deve conter um atributo lista de funcionarios
    - Deve conter um atributo funcionario logado
    - Métodos para:
        * Login do gerente
        * Visualizar lisa de funcionarios
        * Visualizar informações de funcionario específico
        * Adicionar novo funcionário
        * Atualizar informações de um usuário
        * Remover funcionário
        
    - Os métodos Adicionar, Atualizar e Remover só podem ser executados
    se a senha digitada for a mesma do gerente logado

3. Realizar a entrada no sistema no início do programa com login e senha

4. Imprimir Menu com as opções de interação possíveis. Ver os métodos da classe Empresa.

"""
import json
from classEmpresa import Empresa
from classFuncionario import Funcionario, Gerente

with open("banco.json") as f:
    dados = json.load(f)

funcionarios = []

for func in dados:
    if func["Cargo"] == "Gerente":
        funcionarios.append(Gerente(func["ID"],func["Nome"],func["CPF"],func["Salario"],func["Cargo"],func["Login"],func["Senha"]))
    else: 
        funcionarios.append(Funcionario(func["ID"],func["Nome"],func["CPF"],func["Salario"],func["Cargo"]))


empresa = Empresa(funcionarios)
print("Bem vindo a Empresa CATEQ")
print("Faça seu login.")

usuarioLogin = input("Escreva seu login: ")

usuarioSenha = input("Escreva sua senha: ")

empresa.loginFuncionario(usuarioLogin,usuarioSenha)

print(vars(empresa.getFuncionarioLogado()))
empresa.imprimirFuncionarios()