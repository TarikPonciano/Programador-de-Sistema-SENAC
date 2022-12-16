# Write a Python program to get the Fibonacci series between 0 to 50.
# Note : The Fibonacci Sequence is the series of numbers :
# 0, 1, 1, 2, 3, 5, 8, 13, 21, ....
# Every next number is found by adding up the two numbers before it.
# Expected Output : 1 1 2 3 5 8 13 21 34

# sequencia = []

# ultimoDigito = 0

# while (ultimoDigito<50):
#     sequencia.append(ultimoDigito)

#     if((len(sequencia)-2) >= 0):
#         ultimoDigito = sequencia[len(sequencia)-1] + sequencia[len(sequencia)-2]
#     else:
#         ultimoDigito = 1

#     print(sequencia)

# while (ultimoDigito<50):
#     sequencia.append(ultimoDigito)
#     if ((len(sequencia)-2) >= 0):
#         ultimoDigito = sequencia[len(sequencia)-2] + sequencia[len(sequencia)-1]
#     else:
#         ultimoDigito = 1
    # print("Minha sequência Fibonacci é: {}".format(sequencia))

# x,y = 0,1

# while y<50:
#     print(y)
#     x,y = y,x+y


x,y = 0,1

while y<50:
    print(y)
    x,y = y, x+y

x = 0
y = 1


    