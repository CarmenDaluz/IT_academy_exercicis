

class Cuenta:
    def __init__(self, numCuenta: int, saldo: float = 0.0) -> None:
            self.__numCuenta: int = numCuenta
            self.__saldo: float   = saldo
           
   

# Mètodes GETTERS
    def getnumCuenta(self) -> int:
        return self.__numCuenta
    
    def getSaldo(self) -> float:
        return self.__saldo
    

# Mètodes SETTERS

# Otres mètodes

    def ingresar(self, cantidad: float) -> bool:
        if cantidad <= 0:
             return False
        
        self.__saldo += cantidad
        return True
           

    def retirar(self, cantidad: float) -> bool:
        if cantidad <= 0 or cantidad > self.__saldo:
             return False
        
        self.__saldo -= cantidad
        return True

    def devolverSaldo(self) -> None:
         print(f'El saldo actual es {self.__saldo:.2f}€')
        
    def __str__(self) -> str: 
        return f"Num cuenta: {self.__numCuenta} | Total: {self.__saldo}€"
