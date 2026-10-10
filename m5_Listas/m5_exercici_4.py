#EXERCICI 4

# Has de modificar el programa anterior per afegir una nova funcionalitat: establir un número màxim de 5 intents.

# Si l’usuari/ària encerta el número escollit pel programa abans d'aquests 5 intents, el programa mostra el següent missatge per pantalla: “Enhorabona, el número és X i has necessitat Y intents per encertar-lo”.

# Si no encerta el número abans de 5 intents, el programa mostra per pantalla: “Has utilitzat massa intents! El número és X”.

print('Will you guess what random number will apear?')
number: int = int(input('Choose a number: '))
intento = 1 

import random
num_random = random.randint(1, 10)


while number != num_random and intento < 5:
    print('No has acertado ¿Vuelves a probar?')
    number: int = int(input(f'Elige un número. Tienes {5 - intento} intentos: '))
    intento += 1
        
if number == num_random:
    print(f"Has utilitzat massa intents! El número és {num_random}")     
else:      
    print(f'Enhorabona, el número es {num_random} y has necesitado {intento} intentos para acertarlo')


