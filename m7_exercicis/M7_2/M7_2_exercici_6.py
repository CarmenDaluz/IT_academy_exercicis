# L’usuari/ària ha d’introduir números fins que introdueixi un nombre primer. 

# En el moment que l’usuari/ària introdueixi un nombre primer, el programa ha de treure per pantalla el següent missatge: “Exacte, el número “x” és primer!”


def comprobarPrimo(number: int) -> bool:
   
    if number < 2:
        return False
    
    for i in range(2, number):
        if number % i == 0:
            return False
       
    return True

# PROGRAMA PRINCIPAL
num:int  = int(input("Escriu un nombre: "))

while not comprobarPrimo(num):
    num:int  = int(input(f"{num} No és primer, prova amb un altre: "))

print(f'Exacte, el número {num} és primer!')

 


