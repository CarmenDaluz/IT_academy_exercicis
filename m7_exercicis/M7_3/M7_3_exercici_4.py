# El usuario/a debe introducir un DNI y el programa debe decir si la letra es correcta o no con el número de DNI. Si la letra no es correcta, debe decir qué letra es la correcta.

# Para calcular la letra DNI debes tomar el número de DNI a verificar y dividirlo entre 23. El resto se reemplaza por una letra que ya está asignada a ese número mediante la tabla adjunta: 

# Tabla letra DNI
import re

def verificarLetra(numerosDNI):
    LETRAS_DNI: str = 'TRWAGMYFPDXBNJZSQVHLCKE'
    resto: float = int(numerosDNI) % 23 
    letra: str = LETRAS_DNI[resto]

    return letra

dni:str = input('Escribe tu DNI con letra: ').upper()

numerosDNI: int = int(dni[:-1])
letraDNI: str = dni[-1]

letraCorrecta: str = verificarLetra(numerosDNI)

if letraCorrecta == letraDNI:
    print(f'La letra de tu DNI es correcta')
else:
    print(f'La letra de tu DNI no es correcta. La letra correcta es {letraCorrecta}')