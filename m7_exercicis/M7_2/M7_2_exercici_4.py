
# Fes una funció que donades dues llistes d'elements qualsevol. Retorni una tercera llista amb els elements de les dues llistes, sense duplicats.

# Per finalitzar mostra la llista resultant per pantalla.

# Exemple:

# llista1 = [1, 1, 2, 4, 3]

# llista2 = [3, 4, 5]

# resultat = [1, 2, 3, 4, 5]

# lista1:int  = int(input("Escribe una lista de números: "))

# lista2:int  = int(input("Escribe otra lista de números: "))

def añadirLista1():
    for i in lista1:
        if i not in resultado:
            resultado.append(i)
    return i

def igualarListas():
    for x in lista2:
        if x not in resultado:
            resultado.append(x)

def main():
    añadirLista1()
    igualarListas()
    resultadoOrdenado = sorted(resultado)
    print(resultadoOrdenado)
    
lista1 = [1, 1, 2, 4, 3]
lista2 = [3, 4, 5]

resultado = []

    

