# Reloj de horas minutos y segundos de un día:

# def mostrarMin(): 
#     min = 60 
#     for i in range(min):
#         return i

# def mostrarHora(): 
#     hora = 60 
#     for x in range(hora):
#         return x 

# def mostrarDia(): 
#     dia = 24  
#     for y in range(dia):
#         return y 

# mostrarMin = mostrarMin()
# mostrarHora = mostrarHora()
# mostrarDia = mostrarDia()

# print(f'{mostrarDia}:{mostrarHora}:{mostrarMin}')


for i in range(24):
    for x in range(60):
        for y in range(60):
            print(f'{i}:{x:02d}:{y:02d}')