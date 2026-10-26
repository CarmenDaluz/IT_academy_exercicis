# Un/a profesor/a quiere calcular las medias de las notas de toda la clase. 
# Crea una aplicación donde el usuario introducirá un número por pantalla 
# (el número corresponde al número de notas que desea introducir) y el programa le pedirá 
# que introduzca las notas de todos los alumnos/as.

# Una vez las notas han sido introducidas, el programa devuelve lo siguiente:

# Si la nota media es menor que 5: "La nota media de la clase está suspendida. 
# Los alumnos/as deberían preguntar sus dudas y trabajar más" .

# Si la nota es inferior a 7: "La nota media de la clase es buena, 
# pero los alumnos/as deberían mejorar el trabajo personal" .

# Para el resto de casos, el mensaje debe ser: 
# "¡Enhorabuena! La nota media de la clase se corresponde con el esfuerzo realizado" .


def pedirNotas(numNotas: int) -> float:
    total: int = 0
    for nota in range(1, numNotas + 1):
        numNota: float = float(input(f'Nota nº {nota}: '))
        total += numNota

    return total

def mediaNotas(total: float, numNotas: int) -> int:
    media = total / numNotas

    return media

def main():
    numNotas: int = int(input(f'Qué número de notas quieres introducir: '))

    total =pedirNotas(numNotas)
    media = mediaNotas(total, numNotas)

    if media < 5:
        print(f'La nota media de la clase es {media}, está suspendida. Los alumnos/as deberían preguntar sus dudas y trabajar más')
    elif media <= 7:
        print(f'La nota media de la clase es {media}, es buena, pero los alumnos/as deberían mejorar el trabajo personal')
    else:
        print(f'¡Enhorabuena! La nota media de la clase es {media}, se corresponde con el esfuerzo realizado')

main()

