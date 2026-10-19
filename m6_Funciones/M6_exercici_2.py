# Aquest programa calcula l'edat mitjana d'un número de persones introduït per teclat.

# S'ha de crear una funció que s'encarregui de demanar les edats a l'usuari/ària i de calcular l'edat mitjana.


# La funció rebrà per paràmetre el núm. de persones a qui ha de demanar l'edat.
# L'edat de les persones només serà vàlida si està compresa entre 0 i 120 anys.
# La mitjana de les edats introduïdes s'ha de retornar per la funció (return).
# personasList = []

# def edadMedia(numPersonas: int, edadPersonas: int):
#     numPersonas: int = int(input('Escribe un número de personas: '))
#     numPersonas = len(personasList)

#     while numPersonas > 0:
#         edadPersonas: int = int(input(f'Qué edad tiene la persona número {numPersonas}: '))

#         if edadPersonas > 0 and edadPersonas <= 120:
#             return
        
# print(edadMedia)

def edadMedia(numPersonas: int) -> float:
    sumaEdats: int = 0
    contadorPersonas: int = 0

    EDAD_MIN: int = 0
    EDAD_MAX: int = 120

    while contadorPersonas < numPersonas:
        edad: int = int(input(f'Qué edad tiene la persona número {numPersonas}: '))

        if edad < EDAD_MIN or edad > EDAD_MAX:
            print('Error, la edad ha de estar entre 0 y 120')
        else:
            sumaEdats = sumaEdats + edad
            contadorPersonas = sumaEdats + 1
    media: float =  sumaEdats / numPersonas
    return media

numPersonas: int = int(input('Escribe un número de personas: '))
edad
print(edadMedia)
