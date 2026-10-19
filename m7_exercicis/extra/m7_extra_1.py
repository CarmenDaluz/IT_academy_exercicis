# Crea un programa que permeti introduir les notes de 5 alumnes, validant que estiguin entre 0 i 10, i guardar-les en una llista.
# Després, mostra un menú que permeti calcular la mitjana de les notes o consultar quants alumnes han aprovat i quants han suspès. Cal validar l'opció seleccionada.
# Funcions: demanarNotes(), calcularMitjana(), comptarAprovats() i main().

notesList = []
aprovats = []
suspes = []

MAX_INTENTO= 5

def demanarNotes():
    intento = 1
    for intento in range(1, MAX_INTENTO + 1): 
        note:int  = int(input(f"¿Alumno nº{intento} cuál es tu nota?: "))
        if note >= 0 and note <= 10:
            notesList.append(note)
            intento += 1
        else:
            print('La nota no es válida')


def mostrarMenu():
    menu:int  = int(input(f"Selecciona: 1) Calcular la media 2) Cuántos alumnos han aprovado o suspendido: "))
    if menu == 1:
        calcularMitjana()
    elif menu == 2:
        comptarAprovats()
    else:
        print('El número introducido no corresponde')

def calcularTotal():
    total: int = 0
    for i in notesList:
        total += i
    return total

def calcularMitjana():
    total = calcularTotal()
    print(f'La media de las notas es: {total/len(notesList)}') 

def comptarAprovats():
    for i in notesList:
        if i >= 5:
            aprovats.append(i)
        else:
            suspes.append(i)
    print(f'Hay {len(aprovats)} alumnos aprobados, y {len(suspes)} suspensos')


def main():
    demanarNotes()
    mostrarMenu()
    
main()