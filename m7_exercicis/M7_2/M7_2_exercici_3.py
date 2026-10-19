linies:int  = int(input("Escoge un número: "))
ASTERISCO: str = '*'


for fila in range(linies, 0, -1):
    linia: str = ""
    for columna in range(fila): #este bucle se repite tantas veces fila 
        linia += ASTERISCO + " "

    print(linia)

# VERSION 2:

# for fila in range(linies, 0, -1):
#     for columna in range(fila):
#         print(ASTERISCO, end=" ")
#     print()

# Fes una funció que donades dues llistes d'elements qualsevol. Retorni una tercera llista amb els elements de les dues llistes, sense duplicats.

# Per finalitzar mostra la llista resultant per pantalla.

# Exemple:

# llista1 = [1, 1, 2, 4, 3]

# llista2 = [3, 4, 5]

# resultat = [1, 2, 3, 4, 5]