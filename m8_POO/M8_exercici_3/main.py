from functions import (
    mostrarMenu, crearCliente, eliminarCliente, crearCuenta, ingresarEurosCuenta, retirarEurosCuenta 
    )
from Cuenta import Cuenta
from Cliente import Cliente

# PROGRAMA PRINCIPAL
def main() -> None:
    
# MENÚ
    clientes: list[Cliente] = []
    opcion: int = -1

    while opcion != 0:
        mostrarMenu()
        opcion: int = int(input('Elige un nº: '))
  
        if opcion == 1:
            crearCliente(clientes)
        elif opcion == 2:
            eliminarCliente()
        elif opcion == 3:
            crearCuenta()
        elif opcion == 4:
            ingresarEurosCuenta()
        elif opcion == 5:
            retirarEurosCuenta()
        else:
            print('Hasta pronto') 
        
main()