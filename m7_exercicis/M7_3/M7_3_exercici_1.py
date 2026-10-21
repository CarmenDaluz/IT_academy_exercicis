# Realitzar un programa que tingui un menú on se li mostraran 4 opcions a l’usuari/ària per pantalla:

# 1.- Quadrat
# 2.- Triangle
# 3.- Rectangle
# 4.- Cercle
# 0.- Sortir del programa

# Segons l’opció escollida haurà d’introduir unes dades o altres perquè el programa mostri per pantalla l’àrea (el valor) del polígon escollit.
import math

def areaQuadrat():
    lado: int = int(input('Cuánto mide el lado: '))
    areaQuadrat = lado * lado

    print(f'El área del cuadrado es de {areaQuadrat:.2f}')  

def areaTriangle():
    base: int = int(input('Cuánto mide la base: '))
    altura: int = int(input('Cuánto mide la altura: '))
    areaTriangle = (base * altura) / 2

    print(f'El área del triángulo es de {areaTriangle:.2f}')  

def areaRectangle():
    base: int = int(input('Cuánto mide la base: '))
    altura: int = int(input('Cuánto mide la altura: '))
    areaRectangle = base * altura

    print(f'El área del rectangulo es de {areaRectangle:.2f}')

def areaCercle():
    radio: int = int(input('Cuánto mide el radio: '))
    areaCercle = math.pi * (radio * radio)

    print(f'El área del círculo es de {areaCercle:.2f}')


def areaPoligon():

    poligon: int = int(input('Qui poligon prefereixes 1)Quadrat, 2)Triangle, 3)Rectangle, 4)Circle: '))
    match poligon:
        case 1:
            areaQuadrat()
        case 2:
            areaTriangle()
        case 3:
            areaRectangle()
        case 4:
            areaCercle()
        case 0:
            print('Salimos del programa')
        case _:
            print('Error el número es válido')

def main():
    areaPoligon()

main()