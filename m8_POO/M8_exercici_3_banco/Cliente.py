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
       
    def getCuentas(self) -> list[Cuenta]:
         return self.__cuentas
    
# Otres mètodes

    def addCuenta(self, cuenta: Cuenta) -> None:
        self.__cuentas.append(cuenta)

        
    def mostrarCuenta(self) -> None:
        print(self)
        if len(self.__cuentas) == 0:
            print('Este cliente no tiene cuentas asociadas')
            return

        for cuenta in self.__cuentas:
            print(cuenta)


    def buscarCuenta(self, numCuentaBuscada: int) -> Cuenta | None:
        for cuenta in self.__cuentas:
            if cuenta.getNumCuenta() == numCuentaBuscada:
                return cuenta
        return None


    def __str__(self) -> str: 
        return f"Nombre: {self.__nombre} | Apellido: {self.__apellido} | DNI: {self.__dni}"
