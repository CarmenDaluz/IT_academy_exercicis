# 1- Demana a l'usuari/ària un nombre enter positiu.
# El programa ha de mostrar tots els nombres parells compresos entre 1
# i el nombre introduït, inclòs si correspon.

# Si el nombre introduït és 0 o negatiu, s'ha de mostrar un missatge indicant
# que el valor no és correcte.
 
num1: int = int(input('Elige un número entero positivo: '))
numList = []
if num1 <= 0:
    print('El valor no es correcto')
else:
    for i in range (1, num1 + 1):
        if i % 2 == 0:
            numList.append(i)
            
print(f'Los números pares comprendidos entre 1 y {num1} son: {numList}')

