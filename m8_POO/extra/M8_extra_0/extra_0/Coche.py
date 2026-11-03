
class Coche:
    # CONSTRUCTOR
    def __init__(self, marca : str, modelo : str, potencia : int, cilindrada: int, color: str) -> None:
        self.marca: str = marca
        self.modelo: str = modelo
        self.potencia: int = potencia
        self.cilindrada: int = cilindrada
        self.color: str = color
    
 
    def getMarca(self) -> str:
        return self.marca
 
    def getModelo(self) -> str:
        return  self.modelo
 
    def getPotencia(self) -> int:
        return self.potencia

    def getCilindrada(self) -> int:
        return  self.cilindrada
 
    def getColor(self) -> str:
        return self.color

    # MARCA Y MODELO SIN SETTERS, NO SE PUEDEN MODIFICAR

    def setPotencia(self, potencia : int) -> None:
        self.potencia = potencia
    
    def setCilindrada(self, cilindrada : int) -> None:
        self.cilindrada = cilindrada

    def setColor(self, color : str) -> None:
        self.color = color


 #  MÉTODOS
    def __str__(self) -> str: # Define como se representa un objeto en texto
        return f"Marca:{self.marca}, Modelo: {self.modelo}, Potencia: {self.potencia}, Cilindrada: {self.cilindrada}, Color: {self.color}"
 
    def arrancar(self) -> str:
        return f'arrancando...'

    def acelerar(self) -> str:
        return 'acelerando...'

    def girar(self) -> str:
        return 'girando...'

    def frenar(self) -> str:
        return 'frenando...'
    
  