# Criar um programa calculadora
    # Recebe dois números e uma operação (+,-,/,*)
    # Dependendo da operação escolhida, passa os números
    # para uma das funções
    # No final imprime o resultado e a função escolhida

# Criar função para soma
# Criar função para subtração
# Criar função para multiplicação
# Criar função para divisão

# Adapte sua calculadora, para pedir novamente as informações
# caso o usuário tenha escolhido opções inválidas


def main():
    while True:
        numero1 = input("Digite o número 1: ")
        operacao = input("Digite a operação: ")
        numero2 = input("Digite o número 2: ")
        
        calculo = calculadora(numero1, numero2,operacao)
        print(calculo)
        if "Error" in calculo:
            pass
        else:
            break

def calculadora (num1, num2, op):

    try:
        n1 = float(num1)
        n2 = float(num2)
       
        

        if op == "+":
            resultado = f"{n1} {op} {n2} = {soma(n1,n2):.2f}" 
            
        elif op == "-":
            resultado = f"{n1} {op} {n2} = {subtracao(n1,n2):.2f}" 
            
        elif op == "/":
            
            resultado = f"{n1} {op} {n2} = {divisao(n1,n2)}" 
            
        elif op == "*":
            resultado = f"{n1} {op} {n2} = {multiplicacao(n1,n2):.2f}" 
            
        else:
            return "Error - Você escolheu uma operação errada"
        
        return resultado

    except:
        return "Error - Você inseriu números inválidos"
    
def soma(n1,n2):
    return n1+n2

def subtracao(n1,n2):
    return n1-n2

def divisao(n1,n2):
    if n2 == 0:
        resultado = "Error - N2 é 0, não é possível dividir por 0"
        
    else:
        calculo = n1/n2
        resultado = f"{calculo:.2f}"
        

    return resultado

def multiplicacao(n1,n2):
    return n1*n2


main()