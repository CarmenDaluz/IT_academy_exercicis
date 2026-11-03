
class Coche:
    # CONSTRUCTOR
    def __init__(self, marca : str, modelo : str, potencia : int, cilindrada: int, color: str) -> None:
        self.__marca: str = marca
        self.__modelo: str = modelo
        self.__potencia: int = potencia
        self.__cilindrada: int = cilindrada
        self.__color: str = color
    
    def getMarca(self) -> str:
        return self.__marca
 
    def getModelo(self) -> str:
        return  self.__modelo
 
    def getPotencia(self) -> int:
        return self.__potencia

    def getCilindrada(self) -> int:
        return  self.__cilindrada
 
    def getColor(self) -> str:
        return self.__color

    # MARCA Y MODELO SIN SETTERS, NO SE PUEDEN MODIFICAR
    
    def setPotencia(self, potencia : int) -> None:
        self.__potencia = potencia
    
    def setCilindrada(self, cilindrada : int) -> None:
        self.__cilindrada = cilindrada

    def setColor(self, color : str) -> None:
        self.__color = color


 #  MÉTODOS
    def __str__(self) -> str: # Define como se representa un objeto en texto
        return f"{self.__marca} {self.__modelo} | " f"{self.__potencia} {self.__cilindrada} | " f"{self.__color}"

    def arrancar(self) -> str:
        return f'arrancando...'

    def acelerar(self) -> str:
        return 'acelerando...'

    def girar(self) -> str:
        return 'girando...'

    def frenar(self) -> str:
        return 'frenando...'
    
   

 