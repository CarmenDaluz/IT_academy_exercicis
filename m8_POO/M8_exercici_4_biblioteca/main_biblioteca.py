from functions_biblioteca import (
    mostrarMenu, crearUsuario, eliminarUsuario, registrarLibro, prestarLibroUsuario, devolverLibro
    )
from Libro import Libro
from Usuario import Usuario


def main() -> None:
    option: int = -2
    usuarios: list[Usuario] = []
    libros: list[Libro] = []

    libros[0].getIsbn()
    while option != -1:
        mostrarMenu()
        option = int(input('Elige un nº: '))

        if option == 1:
            crearUsuario(usuarios)
        elif option == 2:
            eliminarUsuario(usuarios)
        elif option == 3:
            registrarLibro(libros)
        elif option == 4:
            prestarLibroUsuario(usuarios, libros)
        elif option == 5:
            devolverLibro(usuarios, libros)
        else:
            print('Hasta pronto')
          

main()