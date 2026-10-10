# # es un while

# Un edifici té 10 plantes.
# L'ascensor es troba inicialment a la planta 0.
# Demana a l'usuari/ària a quina planta vol anar.
# El programa ha de mostrar totes les plantes per les quals passa l'ascensor fins arribar a la destinació.
# Per exemple:
# Planta actual: 0
# A quina planta vols anar? 4
 
# Planta 1
# Planta 2
# Planta 3
# Planta 4
# Has arribat a la planta 4.
# També ha de funcionar si l'ascensor es mou cap avall.
# Després d'arribar a una planta, ha de tornar a preguntar una nova destinació.
# El programa finalitza quan l'usuari/ària introdueix -1.
# Només són vàlides les plantes entre 0 i 10.
 

#floor: int = int(input('¿A qué planta quieres ir 1-10?: '))

current_floor = 0
destination_floor = 0
i = 0

while i < 10:
    destination_floor: int = int(input('¿A qué planta quieres ir 1-10?: '))

    if destination_floor == -1:
        print('EXIT')
        break
        
    elif destination_floor < 0 or destination_floor >10:
        destination_floor: int = int(input('No existe. ¿A qué planta quieres ir 1-10?: '))

    else:    
        if current_floor != destination_floor:
            if current_floor < destination_floor:
                print('Subiendo')
                for i in range(current_floor, destination_floor + 1):
                    print(f'Planta {i}')
                    if destination_floor == i:
                        print(f'Has llegado a la planta {destination_floor}')
                        current_floor = destination_floor

            if current_floor > destination_floor:
                print('Bajando')
                for i in range(current_floor, destination_floor - 1, -1):
                    print(f'Planta {i}')
                    if destination_floor == i:
                        print(f'Has llegado a la planta {destination_floor}')
                        current_floor = destination_floor



