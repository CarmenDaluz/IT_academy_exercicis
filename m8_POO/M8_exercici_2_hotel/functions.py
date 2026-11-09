from Hotel import Hotel

def crearHotelesIniciales() -> list[Hotel]:
    return [
        Hotel('ritz', 300, 3, 3000),
        Hotel('hilton', 400, 4, 4000),
        Hotel('pepita', 100, 1, 1000)
    ]

def mostrarMenu() -> None:
    menu: list[str] = ['\nBienvenido al buscador de Hoteles', 
                       'Elige un nº del menú:', 
                       '1. Añadir un hotel', 
                       '2. Dar de baja un hotel', 
                       '3. Buscar hotel', 
                       '4. Modificar hotel', 
                       '5.Exit']
    
    for seccion in menu:
        print(seccion)  

def mostrarHotel(hotel):
    print(hotel)

def crearHotel(hotelesList: list[Hotel]) -> None:
    
    nomHotel: str = input('Nombre hotel: ')
    
    if encontrarNomHotel(hotelesList, nomHotel) is not None:
        print(f'El nombre: {nomHotel}, ya existe')
        return
    
    numHabitacions: int = int(input('Número habitacions: '))
    numPlantes: int = int(input('Nombre plantes: '))
    superficieTotal: float = float(input('Superficie total: '))
    
    hotel: Hotel = Hotel(nomHotel, numHabitacions, numPlantes, superficieTotal)
    hotelesList.append(hotel)

    print('Hotel creado correctamente')
    mostrarHotel(hotel)
    

def encontrarNomHotel(listHoteles: list[Hotel], nomHotelBuscado: str) -> Hotel | None:

    for hotel in listHoteles:
        if hotel.getNomHotel().lower() == nomHotelBuscado.lower():
            return hotel
    return None

def darDeBaixaHotel(listHoteles: list[Hotel]) -> None: # CON REMOVE
    nomHotelBuscado: str = input('¿Qué hotel quieres eliminar?: ')
    hotel: Hotel | None = encontrarNomHotel(listHoteles, nomHotelBuscado)

    if hotel is None:
        print(f'No hay ningún hotel que coincida con {nomHotelBuscado}')
        return
    
    listHoteles.remove(hotel)  
    print(f'Eliminando {nomHotelBuscado}')

def enseñarHotel(listHoteles: list[Hotel]) -> None:
    nomHotelBuscadoEnseñar: str = input('¿Qué hotel buscas?: ')
    hotel: Hotel | None = encontrarNomHotel(listHoteles, nomHotelBuscadoEnseñar) 

    if hotel is None:
        print(f'No hay ningún hotel que coincida con {nomHotelBuscadoEnseñar}')
        return 

    mostrarHotel(hotel)
    hotel.calcularManteniment()

def modificarHotel(listHoteles: list[Hotel]) -> None:
    nomHotelaModificar: str = input('¿Qué hotel quieres modificar?: ')
    hotel: Hotel | None = encontrarNomHotel(listHoteles, nomHotelaModificar) 

    if hotel is None:
        print(f'No hay ningún hotel que coincida con {nomHotelaModificar}')
        return 
    
    # modificar nº habitaciones, nº plantas, superficie
    
    elementoModificar: int = int(input('Qué deseas modificar: 1. Nº habitaciones, 2. Nº plantas, 3.Superficie: '))
    match elementoModificar:
        case 1:
            nuevoNumHabitacions: int = int(input(f'Ahora tiene {hotel.getNumHabitacions()} habitaciones.¿Cuántas quieres que tenga?: '))
            hotel.setNumHabitacions(nuevoNumHabitacions)
        case 2: 
            nuevoNumPlantas: int = int(input(f'Ahora tiene {hotel.getNumPlantes()} plantas.¿Cuántas quieres que tenga?: '))
            hotel.setNumPlantes(nuevoNumPlantas)
        case 3: 
            nuevaSuperficie: int = int(input(f'Ahora tiene {hotel.getSuperficieTotal()}m² .¿Cuántos quieres que tenga?: '))
            hotel.setSuperficieTotal(nuevaSuperficie)

    mostrarHotel(hotel)
    print('La modificación se ha realizado correctamente')