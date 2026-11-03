
class Persona:
    def __init__(self, nombre : str, apellido : str, edad : int) -> None:
        self.nombre: str = nombre
        self.apellido: str = apellido
        self.edad: int = edad
 
    def getNombre(self) -> str:
        return self.nombre
 
    def getApellido(self) -> str:
        return self.apellido
 
    def getEdad(self) -> int:
        return self.edad
 
    def setNombre(self, nombre : str) -> None:
        self.nombre = nombre
 
    def setApellido(self, apellido : str) -> None:
        self.apellido = apellido

 
    # def cumpleaños(self) -> None:
    #     edad.propia = edad.propia + 1
 
    def saludar(self) -> str:
        return f"Me llamo {self.nombre} {self.apellido} y tengo {self.edad} años"
 
    def __str__(self) -> str:
        return f"Nombre: {self.nombre}, apellido: {self.apellido}, edad: {self.edad}"



#     def buscarCochePotencia(coches: list[Coche]) -> None:
#     potencia: int = pedirEnteroPositivo("Potencia mínima (CV): ")
#     encontrado: bool = False
   
#     for coche in coches:
#         if coche.getPotencia() > potencia:
#             encontrado = True
#             print(f"{coche}")
#             #print(coche)
 
#     if not encontrado:
#     #if encontrado == False:
#         print("No tenemos coches con esa potencia.")
 
# def pedirEnteroPositivo(mensaje: str) -> int:
#     numero: int = int(input(mensaje))
#     while numero <= 0:
#         print("Error: introduce un número entero positivo.")
#         numero = int(input(mensaje))
#     return numero
 