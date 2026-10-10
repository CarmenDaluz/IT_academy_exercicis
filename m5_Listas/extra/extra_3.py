# 2- Demana al usuario/ària un nombre enter positiu.
# Calcula cuantos múltiplos de 3 hi ha entre 1 i aquest nombre
# Calculo también la suma de asuntos múltiples.
# Por ejemplo, entre 1 y 10 y tres múltiples de 3: 3, 6 y 9.

num1: int = int(input('Elige un número entero positivo: '))
numList = []
contadorSuma = 0

if num1 <= 0:
    print('Número no válido')
else:
    for i in range(3, num1 + 1, 3):
        numList.append(i)
        contadorSuma = contadorSuma + i #es lo mismo que contadorSuma += i
   
print(f'Hay {len(numList)} múltiplos de 3 en {num1} y son: {numList}')
print(f'La suma es: {contadorSuma}')

