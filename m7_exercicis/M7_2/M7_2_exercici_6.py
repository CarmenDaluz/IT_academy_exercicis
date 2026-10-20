# L’usuari/ària ha d’introduir números fins que introdueixi un nombre primer. 

# En el moment que l’usuari/ària introdueixi un nombre primer, el programa ha de treure per pantalla el següent missatge: “Exacte, el número “x” és primer!”


def comprobarPrimo(number):
    esPrimo: bool = True
    i: int = 2

    for i in range(2, number):
        if number % i == 0:
            return False
        i += 1
    return True

# PROGRAMA PRINCIPAL
num:int  = int(input("Escribe un número: "))

while not comprobarPrimo(num):
    num:int  = int(input(f"{num} No es un nº primo, prueba con otro: "))

print(f'Exacte, el número {num} és primer!')

 


