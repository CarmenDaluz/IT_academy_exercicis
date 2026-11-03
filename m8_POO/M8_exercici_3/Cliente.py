from Cuenta import Cuenta

class Cliente:
    def __init__(self, nombre: str, apellido: str, dni: str) -> None:
            self.__nombre: str           = nombre
            self.__apellido: str         = apellido
            self.__dni: str              = dni
            self.__cuentas: list[Cuenta] = []

# Mètodes GETTERS
    def getNombre(self) -> str:
        return self.__nombre
    
    def getApellido(self) -> str:
        return self.__apellido
    
    def getDni(self) -> str:
        return self.__dni
       

# Mètodes SETTERS


# Otres mètodes


    def __str__(self) -> str: 
        return f"Nombre: {self.__nombre} | Apellido: {self.__apellido} | DNI: {self.__dni} "
