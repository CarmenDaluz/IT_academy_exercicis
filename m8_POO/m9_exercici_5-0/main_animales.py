# Herencia y polimorfismo
# __ private: Sólo se puede acceder desde la propia clase
# _  protected: Sólo se puede acceder desde la propia clase y desde las clases hijas

class Animal:
    def __init__(self, nombre: str) -> None:
        self.__nombre: str = nombre
 
    def getNombre(self) -> str:
        return self.__nombre
 
    #método polimórfico
    def hacerSonido(self) -> None:
        print("Este animal no tiene un sonido específico definido.")
 
    def dormir(self) -> None:
        print(f"{self.__nombre} está durmiendo.")
 
 
class Perro(Animal):
    def __init__(self, nombre: str, raza: str) -> None:
        super().__init__(nombre)
        self.__raza: str = raza
 
    def getRaza(self) -> str:
        return self.__raza
   
    #método polimórfico
    def hacerSonido(self) -> None:
        print("Guau, guau!")
 
 
class Gato(Animal):
    def __init__(self, nombre: str, vidas: int) -> None:
        super().__init__(nombre)
        self.__vidas: int = vidas
 
    def getVidas(self) -> int:
        return self.__vidas
 
    #método polimórfico
    def hacerSonido(self) -> None:
        print("Miau, miau!")
 
# Hormiga no sobrescribe hacerSonido().
# Por tanto, utiliza la implementación heredada de Animal.
class Hormiga(Animal):
    def __init__(self, nombre: str, energia: int) -> None:
        super().__init__(nombre)
        self.__energia: int = energia
 
    def getEnergia(self) -> int:
        return self.__energia
 
   
 
def main() -> None:
    animal: Animal = Animal("Animal genérico")
    perro: Perro = Perro("Rex", "Pastor alemán")
    gato: Gato = Gato("Misu", 7)
    hormiga: Hormiga = Hormiga("Flik", 100)
 
    animales: list[Animal] = [animal, perro, gato, hormiga]
 
    for animal in animales:
        print(f"Nombre: {animal.getNombre()}")
        animal.hacerSonido()
        animal.dormir()
        print()
 
main()
 