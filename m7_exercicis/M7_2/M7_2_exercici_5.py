# Realitzar un programa on l’usuari/ària introdueix un número i el programa crida a un mètode que retorna el factorial del número introduït.

# El factorial d'un nombre n (enter, no negatiu) és el producte de tots els nombres enters positius inferiors o iguals a n. 


def devolverFactorial(num: int) -> int:
    factorial: int = 1
    for i in range(2, num + 1): #para evitar el 1x1 y evitar la primera vuelta
        factorial = i * factorial
    return factorial

# PROGRAMA PRINCIPAL
num:int  = int(input("Escribe un número: "))
while num < 0:
    num:int  = int(input("Error introduce un nº positivo: "))

resultat: int = devolverFactorial(num)
print(f'El factorial de {num} es: {resultat}')
