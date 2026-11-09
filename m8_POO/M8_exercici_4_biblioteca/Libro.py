class Libro:
    def __init__(self, isbn: str, titulo: str) -> None:
        self.__isbn: str        = isbn
        self.__titulo: str      = titulo
        self.__disponible: bool = True

    # Getters
    def getIsbn(self) -> str:
        return self.__isbn
    
    def getTitulo(self) -> str:
        return self.__titulo

    def getDisponible(self) -> bool:
        return self.__disponible

    # Otros métodos
    def prestar(self) -> None:
        if self.__disponible == False:
            print('Ya se ha prestado')

        self.__disponible = False
    
    def devolver(self) -> None:
        if self.__disponible == True:
            print('El libro no se puede devolver. Ya estaba devuelto')
            return
        self.__disponible = True
        

    def mostrarDisponible(self) -> None:
        if self.__disponible:
            print('Disponible')
        print('No disponible')

        
    def __str__(self) -> str:
        estado: str = 'Disponible'
        if not self.__disponible:
            estado = 'Prestado'
            
        return f"ISBN: {self.__isbn} | Título: {self.__titulo} | {estado}"
