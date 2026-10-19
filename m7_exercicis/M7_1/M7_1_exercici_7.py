# Hacer un programa en el que el usuario introduce por pantalla un carácter y un número. El programa imprime por pantalla un cuadrado con el tamaño y el carácter introducidos por el usuario/a.

caracter:str = (input('Introduce un caracter: '))
primerCaracter = caracter[0]

num:int = int(input('Introduce un número: '))


if num > 0 and num < 10:
    for fila in range(num):
        for columna in range(num):
            print(primerCaracter, end=' ')
        print()

else:
    print('Número no válido')


