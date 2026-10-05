# EXERCICI 3:
# El programa demana a l'usuari/ària que introdueixi 3 notes i el programa mostra la mitjana de les 3 notes per pantalla.

number1: int = int(input('Introduce tu nota nº1: '))
number2: int = int(input('Introduce tu nota nº2: '))
number3: int = int(input('Introduce tu nota nº3: '))

media: float = float(number1 + number2 + number3) / 3

print(f'Tu nota media es de {media:.2f}')