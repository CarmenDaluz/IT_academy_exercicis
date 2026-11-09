from functions import (
    mostrarMenu, crearCliente, eliminarCliente, 
    crearCuenta, ingresarEurosCuenta, 
    retirarEurosCuenta 
    )
from Cuenta import Cuenta
from Cliente import Cliente

# PROGRAMA PRINCIPAL
def main() -> None:
    
# MENÚ
    clientes: list[Cliente] = []
    
    cliente1: Cliente = Cliente("Pedro", "Pérez", "1")
    cliente2: Cliente = Cliente("María", "Pérez", "2")
    cliente3: Cliente = Cliente("Andrés", "Pérez", "3")
    cliente4: Cliente = Cliente("Sonia", "Pérez", "4")
    cliente5: Cliente = Cliente("Miguel", "Pérez", "5")
 
    clientes.append(cliente1)
    clientes.append(cliente2)
    clientes.append(cliente3)
    clientes.append(cliente4)
    clientes.append(cliente5)
 
    clientes[0].addCuenta(Cuenta(1))
    clientes[0].addCuenta(Cuenta(2))
    clientes[1].addCuenta(Cuenta(1))
    clientes[1].addCuenta(Cuenta(2))
    clientes[1].addCuenta(Cuenta(3))
    clientes[2].addCuenta(Cuenta(1))
    
    opcion: int = -1
    while opcion != 0:
        mostrarMenu()
        opcion: int = int(input('Elige un nº: '))
  
        if opcion == 1:
            crearCliente(clientes)
        elif opcion == 2:
            eliminarCliente(clientes)
        elif opcion == 3:
            crearCuenta(clientes)
        elif opcion == 4:
            ingresarEurosCuenta(clientes)
        elif opcion == 5:
            retirarEurosCuenta(clientes)
        else:
            print('Hasta pronto') 
        
main()