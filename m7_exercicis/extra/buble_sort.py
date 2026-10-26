# crea una función que reciba una lista de enteros y la ordene de menor a mayor


# def definirLista():
#     num: int = int(input('Añade nº a una lista: '))
#     lista: list = []

#     for 

def bubble_sort(numeros: list[int]) -> None:
    n: int = len(numeros)
   
    
    for j in range(n -1):
        if numeros[j] > numeros[j + 1]:
                auxiliar: int = numeros[j]
                numeros[j] = numeros[j + 1]
                numeros[j + 1] = auxiliar
                print(numeros)


def main() -> None:
    numeros: list = [4,6,7,5,1]
    bubble_sort(numeros)
    print(numeros)

main()