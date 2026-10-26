# Crea un programa en el que el usuario introduce tres notas y el programa calcule la media. 

# Si la media es inferior a 5 debe mostrar el siguiente mensaje por pantalla: "No has superado el curso. Tienes que recuperar".

# Si la media está entre 5 y 7 debe mostrar: "¡Enhorabuena! Has aprobado, pero deberías seguir practicando".

# Si la media es superior a 7 debe mostrar: "¡Enhorabuena! ¡Has superado el curso! ¡Pasa ya al siguiente nivel!"


def calcularMedia(nota1: int, nota2: int, nota3: int) -> float:
    
    media: float = (nota1 + nota2 + nota3) / 3

    return media


def main():
    print('Escribe tres notas para saber la media.')
    nota1: int = int(input('Nota nº1: '))
    nota2: int = int(input('Nota nº2: '))
    nota3: int = int(input('Nota nº3: '))
    
    mediaNotas = calcularMedia(nota1, nota2, nota3) 

    if mediaNotas > 0 and mediaNotas < 5:
        print(f'Has sacado una media de {mediaNotas:.2f}. No has superado el curso. Tienes que recuperar')
    elif mediaNotas >= 5 and mediaNotas <= 7:
        print(f'Has sacado una media de {mediaNotas:.2f}. ¡Enhorabuena! Has aprobado, pero deberías seguir practicando')
    else:
        print(f'Has sacado una media de {mediaNotas:.2f}. ¡Enhorabuena! ¡Has superado el curso! ¡Pasa ya al siguiente nivel!')
main()