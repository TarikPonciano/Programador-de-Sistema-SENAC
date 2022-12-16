# def inverter(n):
#     inverso = str(n)
#     print(inverso[::-1])

# inverter(569484)

def inverter(n):
    inverso = ""
    
    for i in range(len(n)):
        
        inverso += n[(len(n)-1)-i]
        print(inverso)
    
    print("O número invertido é", inverso)

    

numero = 12345678


inverter(str(numero))