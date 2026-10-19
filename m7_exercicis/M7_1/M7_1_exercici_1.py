# Crea un programa en el que el usuario introduce tres notas y el programa calcule la media. 

# Si la media es inferior a 5 debe mostrar el siguiente mensaje por pantalla: "No has superado el curso. Tienes que recuperar".

# Si la media está entre 5 y 7 debe mostrar: "¡Enhorabuena! Has aprobado, pero deberías seguir practicando".

# Si la media es superior a 7 debe mostrar: "¡Enhorabuena! ¡Has superado el curso! ¡Pasa ya al siguiente nivel!"

print('Añade 3 notas para hacer la media')
sumaNotas: float = 0
num: float = 0
contador: int = 1

def media(num: float) -> float:
    for nota in range(1, 3 + 1):
        num: float = float(input(f'Nota nº {nota}: '))
        sumaNotas += num

    sumaNotas / 3
    return

if media(num) < 5:
    print('No has superado el curso. Tienes que recuperar')
elif media(num) >= 5 and media < 7:
    print('¡Enhorabuena! Has aprobado, pero deberías seguir practicando')
elif media(num) > 7:
    print('¡Enhorabuena! ¡Has superado el curso! ¡Pasa ya al siguiente nivel!')