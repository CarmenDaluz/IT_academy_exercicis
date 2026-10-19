# El usuario debe introducir un número y el programa debe mostrar por pantalla si el número es par o impar.


def parImpar(num: int) -> None:
    if num % 2 == 0:
        print(f'El número {num} es par')
    else:
        print(f'El número {num} es impar')

#PROGRAMA PRINCIPAL
def main() -> None:
    num: int = int(input('Escribe un número para saber si es par o impar: '))
  