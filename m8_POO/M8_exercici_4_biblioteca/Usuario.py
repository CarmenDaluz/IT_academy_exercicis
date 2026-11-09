from Libro import Libro

class Usuario:
    def __init__(self, nombre: str, apellido: str, dni: str) -> None:
        self.__nombre: str = nombre
        self.__apellido: str = apellido
        self.__dni: str = dni
        self.__librosPrestados: list[Libro] = []

# Getters
    def getNombre(self) -> str:
        return self.__nombre

    def getApellido(self) -> str:
        return self.__apellido

    def getDni(self) -> str:
        return self.__dni

    def getLibrosPrestados(self) -> list[Libro]:
        return self.__librosPrestados

# Otros métodos
    def tieneLibrosPrestados(self) -> bool:
        return len(self.__librosPrestados) > 0

    def prestar(self, libro) -> None:
        self.__librosPrestados.append(libro)
        

    def devolver(self, libro) -> None:
        self.__librosPrestados.remove(libro)
        
    def mostrarListaLibros(self) -> None:
        for libro in self.__librosPrestados:
            print(libro)

    def __str__(self) -> str:
        return f"Nombre: {self.__nombre} | Apellido: {self.__apellido} | Dni: {self.__dni} | Libros prestados: {len(self.__librosPrestados)}"
