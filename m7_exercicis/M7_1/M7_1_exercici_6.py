# Taula de multiplicar.

# L’usuari/ària introduirà un número (de l'1 al 10) per pantalla, i utilitzant un bucle, el programa li mostrarà la taula de multiplicar d’aquell número


num:int = int(input('Introduce un nº del 1 al 10: '))

if num < 1 or num > 10:
    print('Error')
else:
    for i in range(1, 10 + 1):
        print(f'{num} x {i} = {num * i}')


