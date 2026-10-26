# Dadas dos listas, encuentra los elementos que están en la primera lista pero no en la segunda.
# Crea una tercera lista con esos valores y muéstralos por pantalla




def comprobarNum(elemento: int, llista: list[int]) -> bool:

    for elementoLista in llista:
        if elementoLista == elemento:
            return False  

    return True

def numUnicos() -> None:
    llista1: list[int] = [1, 2, 3, 4, 5]
    llista2: list[int] = [3, 2, 6]
    result: list[int] = []

    for elemento in llista1:
        if comprobarNum(elemento, llista2) and comprobarNum(elemento, result):
            result.append(elemento)
    print(f'The numbers that are in {llista1} and not in {llista2} are {result}')

def main() -> None:             
    numUnicos()
    
main()
