
# Fes una funció que donades dues llistes d'elements qualsevol. Retorni una tercera llista amb els elements de les dues llistes, sense duplicats.

# Per finalitzar mostra la llista resultant per pantalla.

# Exemple:

# llista1 = [1, 1, 2, 4, 3]

# llista2 = [3, 4, 5]

# resultat = [1, 2, 3, 4, 5]

# lista1:int  = int(input("Escribe una lista de números: "))

# lista2:int  = int(input("Escribe otra lista de números: "))

def comprobarNumIguales(lista1: list[int], lista2: list[int]) -> bool:
    duplicado: bool = False
    resultado = []
    
    for i in lista1:
        for j in lista2:
            if i == j:
                duplicado = True
                
    if duplicado:
        resultado.append(i)
    return duplicado

# def añadirIguales(duplicado: bool, resultado: list[int]):
  

def main():
    lista1 = [1, 1, 2, 4, 3]
    lista2 = [3, 4, 5]

    comprobarNumIguales(lista1, lista2)
main()

