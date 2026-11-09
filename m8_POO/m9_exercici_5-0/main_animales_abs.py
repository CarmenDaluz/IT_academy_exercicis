from abc import ABC, abstractmethod
 
# De una clase abstracta no se pueden instanciar objetos
class Animal(ABC):
    def __init__(self, nombre: str) -> None:
        self.__nombre: str = nombre
 
    def getNombre(self) -> str:
        return self.__nombre
 
    @abstractmethod
    def hacerSonido(self) -> None:
        pass
 
    # método polimórfico
    def mostrarInformacion(self) -> None:
        print(f"Me llamo {self.__nombre}")
 
    def dormir(self) -> None:
        print(f"{self.__nombre} está durmiendo.")
 
 
class Perro(Animal):
    def __init__(self, nombre: str, raza: str) -> None:
        super().__init__(nombre)
        self.__raza: str = raza
 
    def getRaza(self) -> str:
        return self.__raza
 
    def hacerSonido(self) -> None:
        print("Guau, guau!")
 
    def mostrarInformacion(self) -> None:
        print(f"Perro: {self.getNombre()}, raza: {self.__raza}")
 
 
class Gato(Animal):
    def __init__(self, nombre: str, vidas: int) -> None:
        super().__init__(nombre)
        self.__vidas: int = vidas
 
    def getVidas(self) -> int:
        return self.__vidas
 
    def hacerSonido(self) -> None:
        print("Miau, miau!")
 
    def mostrarInformacion(self) -> None:
        print(f"Gato: {self.getNombre()}, vidas: {self.__vidas}")
 
 
def main() -> None:
    #animal: Animal = Animal("Rocky")#No se puede instanciar un objeto de una clase Abstracta
    perro: Perro = Perro("Rex", "Pastor alemán")
    gato: Gato = Gato("Misu", 7)
 
    animales: list[Animal] = [perro, gato]
 
    for animal in animales:
        animal.mostrarInformacion()
        animal.hacerSonido()
        animal.dormir()
        print()
 
 
main()