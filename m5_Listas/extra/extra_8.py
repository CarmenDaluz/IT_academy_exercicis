

coches: list[str] = ["Volvo", "Seat", "Audi", "Volkswagen", "Renault", "Ford"]
cocheBuscado: str = input("Introduzca el coche a buscar: ")

encontrado: bool = False

for i in range(len(coches)):
    if cocheBuscado.lower() == coches[i].lower():
        encontrado = True

if encontrado:
    print('El coche está en stock')
else:
    print('El coche no está en stock')
