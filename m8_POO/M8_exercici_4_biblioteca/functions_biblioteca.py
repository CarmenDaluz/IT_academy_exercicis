from Usuario import Usuario
from Libro import Libro

def mostrarMenu():
    menu: list[str] = ['\nBienvenido a la Biblioteca',
                        '1. Crear un usuario',
                        '2. Eliminar un usuario',
                        '3. Registrar un libro en el sistema',
                        '4. Prestar un libro a un usuario',
                        '5. Devolver un libro']

    for seccion in menu:
        print(seccion)

def buscarUsuario(usuarioList: list[Usuario], dniUsuarioBuscar: str) -> Usuario | None:
    for usuario in usuarioList:
        if dniUsuarioBuscar == usuario.getDni():
            return usuario
    return None

    
def crearUsuario(usuarioList: list[Usuario]) -> None:

    dni: str = input('Dni: ')
    if buscarUsuario(usuarioList, dni) is not None:
        print('Ya hay usuarios con este dni')
        return
    
    nombre: str = input('Nombre: ')
    apellido: str = input('Apellido: ')

    usuario: Usuario = Usuario(nombre, apellido, dni)
    usuarioList.append(usuario)
    print(usuario)

def eliminarUsuario(usuarioList: list[Usuario]) -> None:
    dni: str = input('Dni: ')
    usuario: Usuario | None = buscarUsuario(usuarioList, dni)
    
    if usuario is None:
        print('No hay ningún usuario con este dni')
        return

    usuarioList.remove(usuario)
    print(f'Usuario: {usuario.getNombre()} {usuario.getApellido()} con dni: {dni}, borrado correctamente')

def buscarLibro(librosList: list[Libro], títuloLibroBuscador: str) -> Libro | None:

    for libro in librosList:
        if libro.getTitulo().lower() == títuloLibroBuscador.lower():
            return libro
        
        return None

def registrarLibro(librosList: list[Libro]) -> None:

    tituloLibro: str = input('Escribe el título del libro: ')
    if buscarLibro(librosList, tituloLibro) is not None:
        print('Ya hay usuarios con este dni')
        return
    
    isbn: str = input('Isbn: ')

    libro: Libro = Libro(isbn, tituloLibro)
    librosList.append(libro)
    print(libro)
    
def prestarLibroUsuario(usuarioList: list[Usuario], librosList: list[Libro]) -> None:
    dniUsuarioBuscar: str = input('Escribe tu dni: ')
    usuario: Usuario | None = buscarUsuario(usuarioList, dniUsuarioBuscar)
    if usuario is None:
        print('No hay usuario con ese dni')
        return

    títuloLibroBuscador: str = input('¿Qué libro quieres tomar prestado?: ')
    libro: Libro | None = buscarLibro(librosList, títuloLibroBuscador)
    if libro is None:
        print('No hay ningún libro con ese nombre')
        return

    if libro.getDisponible() == False:
        print('El libro no está disponible')
        return
    
    libro.prestar() 
    usuario.prestar(libro)
    print(usuario)

    print(f'El libro {libro.getTitulo()} se ha tomado prestado por {usuario.getNombre()} {usuario.getApellido()}')
    print(libro)

def devolverLibro(usuarioList: list[Usuario], librosList: list[Libro]):
    dniUsuarioBuscar: str = input('Escribe tu dni: ')
    usuario: Usuario | None = buscarUsuario(usuarioList, dniUsuarioBuscar)

    if usuario is None:
        print('No hay usuario con ese dni')
        return
    print(usuario)
    print(f'Hola, {usuario.getNombre()} {usuario.getApellido()}. Has tomado prestado {usuario.getLibrosPrestados()}')
    
    títuloLibroBuscador: str = input('¿Qué libro quieres devolver?: ')
    libro: Libro | None = buscarLibro(librosList, títuloLibroBuscador)
    if libro is None:
            print('No hay ningún libro con ese nombre')
            return
    libro.devolver()
    usuario.devolver(libro)
    print(f'El libro: {libro.getTitulo()} se ha devuelto correctamente por el usuario {usuario.getNombre()}')
    