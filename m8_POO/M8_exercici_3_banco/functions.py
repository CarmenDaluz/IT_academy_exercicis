from Cliente import Cliente
from Cuenta import Cuenta

def mostrarMenu():
    menu: list[str] = ['\nBienvenido/a a tu banco:',
        '1.- Crear cliente/a.',
        '2.- Eliminar cliente/a.',
        '3.- Crear cuenta de un cliente/a.',
        '4.- Ingresar euros en una cuenta de un cliente/a.',
        '5.- Retirar euros en una cuenta de un cliente/a.'
    ]
    
    for element in menu:
        print(element)

def mostrarCliente(cliente):
    print(cliente)


def buscarCliente(clientesList: list[Cliente], dniClienteBuscado: str) -> Cliente | None:
    
    for cliente in clientesList:
        if cliente.getDni().lower() == dniClienteBuscado.lower():
            return cliente
    return None


def crearCliente(clientesList: list[Cliente]):
    dniClienteBuscado: str = input('Escribe tu dni: ')

    if buscarCliente(clientesList, dniClienteBuscado) is not None:
        print(f'El nombre: {dniClienteBuscado}, ya existe')
        return

    nomCliente: str = input('Nombre: ')
    appellidoCliente: str = input('Apellido: ')
   
    cliente: Cliente = Cliente(nomCliente, appellidoCliente, dniClienteBuscado)
    clientesList.append(cliente)

    print('Cliente creado correctamente')
    mostrarCliente(cliente)


def eliminarCliente(clientesList: list[Cliente]):

    dniClienteEliminar: str = input('Escribe el dni del cliente que quieras eliminar:')
    clienteBuscarCliente: Cliente | None = buscarCliente(clientesList, dniClienteEliminar)
    
    if clienteBuscarCliente is None:
        print('El cliente no está dado de alta')
        return

    print('Cliente eliminado')
    clientesList.remove(clienteBuscarCliente)


def crearCuenta(clientesList: list[Cliente]) -> None:
    dniClienteBuscado: str = input('Escribe tu dni: ')
    cliente: Cliente | None = buscarCliente(clientesList, dniClienteBuscado)
    
    if cliente is None:
        print('No hay clientes registrados con este dni. Debe registrarse antes')
        return
    
    numCuenta: int = int(input('Escribe el número de cuenta: '))
    
    if cliente.buscarCuenta(numCuenta) is not None:
        print('Ya esxiste una cuenta con ese nº')
        return
    
    cliente.addCuenta(Cuenta(numCuenta))
    print(f'Cuenta {numCuenta} creada para {cliente.getNombre()}')


def ingresarEurosCuenta(clientesList: list[Cliente]) -> None:
    dniCliente: str = input('Accede a tu cuenta con tu dni: ')
    cliente: Cliente | None = buscarCliente(clientesList, dniCliente)

    if cliente is None: 
        print('No existe este cliente')
        return
    
    numCuenta: int = int(input('Escribe el número de cuenta: '))
    cuenta: Cuenta | None = cliente.buscarCuenta(numCuenta)
    if cuenta is None:
        print('No existe esta cuenta')
        return
  
    cantidadIngresar: int = int(input('Qué cantidad quieres ingresar: '))
    cuenta.ingresar(cantidadIngresar)
    print(f'Se ha ingresado {cantidadIngresar}€ en la cuenta {numCuenta}')
    cuenta.devolverSaldo()

def retirarEurosCuenta(clientesList: list[Cliente]):
    dniCliente: str = input('Accede a tu cuenta con tu dni: ')
    cliente: Cliente | None = buscarCliente(clientesList, dniCliente)

    if cliente is None: 
        print('No existe este cliente')
        return
    
    numCuenta: int = int(input('Escribe el número de cuenta: '))
    cuenta: Cuenta | None = cliente.buscarCuenta(numCuenta)
    if cuenta is None:
        print('No existe esta cuenta')
        return
  
    cantidadRetirar: int = int(input(f'Hay un saldo de {cuenta.getSaldo()}€. ¿Qué cantidad quieres retirar: '))
    if not cuenta.retirar(cantidadRetirar):
        print('Saldo insufuiciente')
        return
    
    print(f'Se ha retirado {cantidadRetirar}€ de la cuenta {numCuenta}. Queda {cuenta.getSaldo()}€')
    cuenta.devolverSaldo()