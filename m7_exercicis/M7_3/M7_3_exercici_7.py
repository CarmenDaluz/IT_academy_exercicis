# Intersecció de dues llistes. Troba els elements comuns entre dues llistes i guarda'ls en una llista nova. La llista resultant no ha de tenir duplicats.

# Exemple:

# Per aquestes dues llistes: llista1 = [1, 2, 3, 3, 4, 5], llista2 = [3, 4, 6, 7, 5]

# El resultat és: resultat = [3, 4, 5]

def numExist(lista: list[int], elementSearched: int) -> bool:
    
    for element in lista:
        if element == elementSearched:
            return True
        
    return False

def findNumbers(lista1: list[int], lista2: list[int]) -> list[int]:

    result: list[int] = []
    
    for element in lista1:
        if numExist(lista2, element) and not numExist(result, element):
            result.append(element)

    return result

#  PROGRAMA PRINCIPAL

def main():
    lista1: list = [1, 2, 3, 3, 4, 5]
    lista2: list = [3, 4, 6, 7, 5]

    resultat = findNumbers(lista1, lista2)
    
    print(f'The same numbers that exists in both lists are {resultat}')

main()