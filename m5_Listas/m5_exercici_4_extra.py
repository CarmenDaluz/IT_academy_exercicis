
print("Endevinaràs quin nombre a l'atzar apareixerà?")
number: int = int(input('Tria un nombre: '))
intento: int = 1 
maxIntento: int = 5

import random
num_random = random.randint(1, 10)


while number != num_random and intento < maxIntento: 
    if  number < num_random:
        print('El nombre es massa petit')
    elif number > num_random:
        print('El nombre es massa gran')

    number: int = int(input(f'Tria un altre nombre: '))
    intento += 1
   
if number == num_random:
    print(f"Enhorabona, el número es {num_random}")     
else:      
    print(f'Has utilitzat massa intents! El número és {num_random}')


