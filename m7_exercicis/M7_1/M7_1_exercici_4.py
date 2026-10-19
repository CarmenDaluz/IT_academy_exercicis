# El usuario/a debe introducir dos números, el programa devolverá “Uno de los dos números es negativo”, sólo si uno de los dos números es negativo.

#MANERA 1

num1: int = int(input('Escribe un número: '))
num2: int = int(input('Escribe otro número: '))

if (num1 < 0 or num2 < 0) and (num1 >= 0 or num2 >= 0):
    print('Uno de los dos números es negativo')
elif num1 < 0 and num2 < 0:
    print('Los dos números son negativos')

else: 
    print('No hay ningún número negativo')

