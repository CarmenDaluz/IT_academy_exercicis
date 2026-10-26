# Ejercicio 2 (validación + bucle + función)

# Crea una función pedirNumero() que pida un número al usuario hasta que esté entre 1 y 10 (ambos incluidos) y lo devuelva. En main(), llámala y muestra la tabla de multiplicar de ese número del 1 al 10.


def pedirNumero() -> int:

    num: int = int(input('Escribe un número entre 1 y 10: '))
    while num < 1 or num > 10:
        num: int = int(input('Error. El número debe estar entre el 1 y 10. Escribe otro número: '))

    return num

def main():
    number = pedirNumero()

    for i in range(1, 10 + 1):
        print(f'{number} x {i} = {number * i}')

main()