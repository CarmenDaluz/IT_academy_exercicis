#EXERCICI EXTRA 1:

# Realitzar un joc per endevinar un nombre aleatori N, entre 1 i 500.

# Si la distància entre el nombre a endevinar i el de l'usuari/ària és de 50 o més, el programa haurà de dir:

# “Fred, fred: el teu número és més gran “ o “Fred, fred: el teu número és més petit “

# Si la distància entre el nombre a endevinar i el de l'usuari/ària està entre 15 i 50, el programa haurà de dir:

# “Tebi, Tebi: el teu número és més gran “ o “Tebi, Tebi: el teu número és més petit “ 

# I si la distància entre el nombre a endevinar i el de l'usuari/ària i si la distància és menor a 15, el programa haurà de dir:

# “Calent, calent: el teu número és més gran “ o “Calent, calent: el teu número és més petit “

# El procés acaba quan l'usuari/ària encerta.



print("Endevinaràs quin nombre a l'atzar apareixerà?")
number: int = int(input('Tria un nombre: '))


import random
num_random = random.randint(1, 500)


while number != num_random: 
    if  number < num_random:
        if number > num_random - 50 or number > num_random - 15:
            print('Tebi, Tebi: el teu número és més petit') 
        else:
            print('Fred, fred: el teu número és més petit')

    elif  number > num_random:
        if number < num_random + 50 or number < num_random + 15: 
            print('Tebi, Tebi: el teu número és més gran') 
        else:
            print('Fred, fred: el teu número és més gran')

    number: int = int(input(f'Tria un altre nombre: '))
   
if number == num_random:
    print(f"Enhorabona, el número es {num_random}")     



