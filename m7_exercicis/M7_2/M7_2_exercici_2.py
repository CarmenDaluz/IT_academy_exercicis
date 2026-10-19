# Fes un programa que mostri el següent per pantalla:

# *

# * *

# * * *

# * * * *

# * * * * *

# * * * * * *

# El nombre de línies formades per “*” vindrà donat per un número que l’usuari/ària introduirà per consola.

linies:int  = int(input("Escoge un número: "))
ASTERISCO: str = '*'


for fila in range(1, linies +1):
    linia: str = ""

    for columna in range(fila):
        linia += ASTERISCO + " "

    print(linia)

