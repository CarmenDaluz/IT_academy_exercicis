from Cliente import Cliente

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
    
    if buscarCliente(clientesList, dniClienteEliminar) is not None:
        print('Cliente eliminado')
        clientesList.remove(clienteBuscarCliente)


def crearCuenta():
    pass

def ingresarEurosCuenta():
    pass

def retirarEurosCuenta():
    pass