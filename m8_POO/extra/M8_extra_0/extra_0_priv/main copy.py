from Coche_private import Coche

def crearCoche(lista: list) -> None:
    coche1: Coche = Coche('Fiat', 'Topolino', 100, 1200, 'Rojo')
    coche2: Coche = Coche('Renault', 'Laguna', 100, 1200, 'Verde')

    print(coche1)
    print(coche2)
    print(f'La marca del coche nº2 es: {coche2.getMarca()}, y el color: {coche2.getColor()}')

    coche1.setPotencia(200)
    print(coche1)

    coche2.setColor('Amarillo')
    print(coche2)
    

def mostrarCoches(coches: list[Coche]) -> None:

    if len(coches) == 0:
        print('No hay coches disponibles')
        return
    
    for coche in coches:
        print(coche)


def añadirCoche(coches: list[Coche]) -> None:
    demanaMarca: str      = input('Marca: ') 
    demanaModelo: str     = input('Model: ') 
    demanaPotencia: int   = int(input('Potencia: ')) 
    demanaCilindrada: int = int(input('Cilindrada: '))
    demanaColor: str      = input('Color: ')

    cocheDemanado: Coche = Coche(demanaMarca, demanaModelo, demanaPotencia, demanaCilindrada, demanaColor)
    coches.append(cocheDemanado)
    # Lo de antes se resume en esta línea:
    # coches.append(Coche(demanaMarca, demanaModelo, demanaPotencia, demanaCilindrada, demanaColor))


def mostrarMenu() -> None:
    print("\n--- CONCESIONARIO ---")
    print("1. Mostrar coches")
    print("2. Añadir coche")
    print("3. Buscar coche por potencia")
    print("4. Comprar coche por potencia")
    print("5. Buscar coche por marca y modelo")
    print("0. Salir")


def buscarCochePorPotencia(coches: list[Coche]) -> None:
    potencia: int = int(input('Qué potencia quieres: '))
    encontrado: bool = False

    for coche in coches:
        if coche.getPotencia() > potencia:
            encontrado = True
            print(coche.getMarca(), coche.getModelo())
        
    if not encontrado:
        print('No tenemos coches con esa potencia')


def pedirEnteroPositivo(mensaje: str) -> int:
    numero: int = int(input(mensaje))
    while numero <= 0:
        print('Error introduce un número entero positivo')
        numero = int(input(mensaje))

    return int(numero)


def buscarCocheObjeto(coches: list[Coche], potencia: int) -> Coche | None:
    for coche in coches:
        if coche.getPotencia() > potencia:
            return coche
        
    return None


def comprarCoche(coches: list[Coche]) -> None:
    potencia: int = pedirEnteroPositivo('Potencia mínima(CV): ')
    coche: Coche | None = buscarCocheObjeto(coches, potencia)

    if coche == None:
        print('No tenemos coches con esa potencia')
        return
    
    print(f'Coche comprado: {coche}')
    coches.remove(coche)

# OTRA OPCION DE COMPRAR COCHE PERO BUSCANDO POSICIÓN:
# def comprarCoche(coches: list[Coche]) -> None:
#     potencia: int = pedirEnteroPositivo("Potencia mínima (CV): ")
#     posicion: int = buscarCochePosicion(coches, potencia)
   
#     if posicion == -1:
#         print("No tenemos coches con esa potencia para vender.")
#         return
 
#     coche: Coche = coches.pop(posicion)
#     print(f"Coche comprado: {coche}")

# def buscarCochePosicion(coches: list[Coche], potencia: int) -> int:
#     for i in range(len(coches)):
#         if coches[i].getPotencia() > potencia:
#             return i
#     return -1 (cuando en el tamaño no hay nadie es -1, el último elemento es -1)
 

def buscarCocheMarcayModelo(coches: list[Coche],buscarMarca: str, buscarModelo: str) -> Coche | None:
    
    for coche in coches:
        if coche.getMarca().lower() == buscarMarca.lower() and coche.getModelo().lower() == buscarModelo.lower():
            return coche
    return None

def buscarPorMarcaModelo(coches: list[Coche]) -> None:
    buscarMarca: str = input('¿Qué marca estás buscando?: ').casefold()
    buscarModelo: str = input('¿Y qué modelo?: ').casefold()
    coche: Coche | None = buscarCocheMarcayModelo(coches, buscarMarca, buscarModelo)
    if coche is None:
        print("No se ha encontrado ese coche.")
        return
    print(f"Coche encontrado: {coche}")


def main() -> None:
    listaCoches: list[Coche] = []
    coches: list[Coche] = [
            Coche("Audi", "A3", 110, 1200, "Blanco"),
            Coche("Seat", "Ibiza", 80, 1000, "Blanco"),
            Coche("Toyota", "Rav4", 110, 1300, "Gris"),
            Coche("BMW", "M3", 150, 1600, "Rojo"),
            Coche("Audi", "A1", 100, 1200, "Blanco")
        ]
    
    mostrarMenu()
    texto: str = input('Elige una opción: ')

    while not texto.isdigit():
        texto: str = (input('Error. Elige una opción entre 0 y 5: '))
        
    match texto:
        case '1':
            mostrarCoches(coches)
        case '2':
            añadirCoche(coches)
        case '3':
            buscarCochePorPotencia(coches)
        case '4':
            comprarCoche(coches)
            print('Los coches disponibles ahora son: ', )
            for coche in coches: print(coche.getMarca(), coche.getModelo())
        case '5':
            buscarPorMarcaModelo(coches)
        case '0':
            print('Exit')
            return
        case _:
            print('Error. El nº debe estar entre 0 y 5')


    # EJERCICIO CON LISTA DE COCHES:
    # crearCoche(coches)
    # print(coches[1].getPotencia())
    # coches[0].setColor('Negro')
    # print(coches[1].getMarca())
    # mostrarCoches(coches)


    # EJERCICIO INSTANCIANDO DOS OBJETOS:
    # coche1: Coche = Coche('Fiat', 'Topolino', 100, 1200, 'Rojo')
    # coche2: Coche = Coche('Renault', 'Laguna', 100, 1200, 'Verde')
    
    # print(coche1)
    # print(coche2)
    # print(f'La marca del coche nº2 es: {coche2.getMarca()}, y el color: {coche2.getColor()}')

    # coche1.setPotencia(200)
    # print(coche1)

    # coche2.setColor('Amarillo')
    # print(coche2)

    # if coche1.getPotencia() <= 100:
    #     coche1.setPotencia(180)
    # print(coche1)

   

main()