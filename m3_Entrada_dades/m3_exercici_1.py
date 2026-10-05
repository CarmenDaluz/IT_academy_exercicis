
#Fer un programa que li demani a l’usuari/ària aquestes dades: Nom, Cognom, Edat.
#Un cop l’usuari/ària hagi acabat d’introduir les dades, aquestes s’han de mostrar per pantalla.

name: str = str(input('¿Cuál es tu nombre: '))
lastName: str = str(input('¿Cuál es tu apellido: '))
age: int = int(input('¿Cuál es tu edad: '))

print(f'Mi nombre es {name} {lastName} y tengo {age} años')
