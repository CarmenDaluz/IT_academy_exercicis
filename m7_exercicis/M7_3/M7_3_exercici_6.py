# Omple una llista amb 20 números random entre l'1 i el 50.

# Quan estigui ple, mostra la suma de tots els seus nombres parells i la suma de tots els seus números imparells.

import random


def añadirNumRandomLista():
    numeros: list = []
    for i in range(1, 20 + 1):
        num_random = random.randint(1, 50)
        numeros.append(num_random)

    return numeros

def paresImpares(numeros):
    sumaPares: int = 0
    sumaImpares: int = 0

    for numero in numeros:
        if numero % 2 == 0:
            sumaPares = sumaPares + numero
        else:
            sumaImpares = sumaImpares + numero

    return [sumaPares, sumaImpares]


numeros = añadirNumRandomLista()
sumaPares, sumaImpares = paresImpares(numeros)
print(f'La suma de todos los nº pares es {sumaPares} y la de los impares es {sumaImpares}')


