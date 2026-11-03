
# Fes una funció que donades dues llistes d'elements qualsevol. Retorni una tercera llista amb els elements de les dues llistes, sense duplicats.

# Per finalitzar mostra la llista resultant per pantalla.

# Exemple:

# llista1 = [1, 1, 2, 4, 3]

# llista2 = [3, 4, 5]

# resultat = [1, 2, 3, 4, 5]

# lista1:int  = int(input("Escribe una lista de números: "))

# lista2:int  = int(input("Escribe otra lista de números: "))

def comprobarDuplicado(lista: list[int], elemento: int) -> bool:

    for i in lista:
        if i == elemento:
            return False

    return True

def comprobacionFinal(lista1: list[int],lista2: list[int]) -> list[int]:
    resultado = []

    for elemento in lista1:
        if comprobarDuplicado(resultado, elemento):
            resultado.append(elemento)
    for e in lista2:
        if comprobarDuplicado(resultado, e):
                resultado.append(e)

    return resultado
     
def main():
    llista1 = [1, 1, 2, 4, 3]
    llista2 = [3, 4, 5]

    resultat = comprobacionFinal(llista1, llista2)
    resultat.sort()

    print(resultat)

main()
