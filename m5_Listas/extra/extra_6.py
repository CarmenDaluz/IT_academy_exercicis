# 5- Demana a l'usuari/ària un nombre enter positiu.
# El programa ha de calcular quantes xifres té el nombre sense convertir-lo a str.
# Per exemple:
# Introdueix un nombre: 5832
# El nombre té 4 xifres.
 
x = 0
y = 0 

num1 = x + y
num1: int = int(input('Elige un número entero positivo: '))

if num1 <= 0:
    print('El número no es correcto')
else:
    num_auxiliar: int = num1
    cantidad_cifras: int = 0

    while num_auxiliar > 0:
        num_auxiliar = num_auxiliar // 10
        cantidad_cifras += 1


print(f'El número {num1} tiene {cantidad_cifras} cifras')