#EXERCICI 3

# L’exercici consisteix a què l’usuari/ària ha d'endevinar el número escollit aleatòriament pel programa.

# El programa, demana números a l’usuari/ària fins que aquest encerti el número aleatori generat pel programa.

# Un cop l’usuari/ària ha endevinat el número, es mostrarà per pantalla el següent missatge: “Enhorabona, el número era X”.

print('Will you guess what random number will apear?')
number: int = int(input('Choose a number: '))

import random
num_random: int = random.randint(1, 10)


while number != num_random:
    print('No has acertado ¿Vuelves a probar?')
    number: int = int(input('Choose a number: '))

print(f'Enhorabona, el número era {num_random}')
