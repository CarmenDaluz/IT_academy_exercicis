from functions import (
    mostrarMenu, crearHotelesIniciales, crearHotel, darDeBaixaHotel, enseñarHotel, modificarHotel
    )
from Hotel import Hotel

# PROGRAMA PRINCIPAL
def main() -> None:
    
# MENÚ
    hoteles: list[Hotel] = crearHotelesIniciales()
    opcion: int = -1

    while opcion != 0:
        mostrarMenu()
        numMenu: int = int(input('Elige un nº: '))

    # Opción match menú
        match numMenu:
            case 1:
                crearHotel(hoteles)
            case 2:
                darDeBaixaHotel(hoteles)
            case 3:
                enseñarHotel(hoteles)
            case 4:
                modificarHotel(hoteles)
            case 5:
                print('Exit')
                return
            case _:
                print('Error debe ser una opción entre 0 y 4.')

    #Otra opción con if de menú:
        # if opcion == 1:
        #     crearHotel(hoteles)
        # elif opcion == 2:
        #     darDeBaixaHotel(hoteles)
        # elif opcion == 3:
        #     enseñarHotel(hoteles)
        # elif opcion == 4:
        #     modificarHotel()
        # else:
        #     print('Hasta pronto') 
        
main()