# Ejercicio 1 (funciones + listas)

# Crea una función contarPares(listNum) que reciba una lista de números, imprima cuántos pares hay y devuelva la suma de los impares. 
# En main(), usa la lista [4, 7, 10, 3, 8, 5] e imprime la suma que devuelve.

def contarPares(listNum: list[int]) -> int:
    contador: int = 0
    sumaImpares: int = 0
    for num in listNum:
        if num % 2 == 0:
            contador += 1
        else:
            sumaImpares += num

    print(f'Hay {contador} números pares')

    return sumaImpares

def main():
    finalListNum: list[int] = [4, 7, 10, 3, 8, 5]

    sumaImparesTotal = contarPares(finalListNum)
    print(f'La suma de los números impares es {sumaImparesTotal}')

main()