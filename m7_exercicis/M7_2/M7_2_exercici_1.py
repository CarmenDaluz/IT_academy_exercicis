def introducirNumero():
    esPrimo: bool = False
    num:int  = int(input("Escoge un número: "))

    if num > 1:
        esPrimo = comprobarPrimo(num)

    print(esPrimo)


def comprobarPrimo(num):
    esPrimo: bool = True
    i: int = 2

    for i in range(2, num):
        if num % i == 0:
            return False
        i += 1
    return True



introducirNumero()