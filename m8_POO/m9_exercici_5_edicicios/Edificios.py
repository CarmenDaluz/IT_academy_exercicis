# from abc import ABC, abstractmethod

# CLASE MADRE
class Edificio:

    def __init__(self, nombre: str, numPlantas: int, superficie: int) -> None:
        self.__nombre: str     = nombre
        self.__numPlantas: int = numPlantas
        self.__superficie: int = superficie

    # Getters
    def getNombre(self) -> str:
        return self.__nombre
    
    def getNumPlantas(self) -> int:
        return self.__numPlantas

    def getSuperficie(self) -> int:
        return self.__superficie

    # Otros métodos
    # @abstractmethod
    def limpiar(self, superficie: int, numPlantas: int) -> None:
        METROS_POR_MIN: int = 5
        tiempoSubirPlanta: float = 0.5

        EUROS_MIN: int = 1
        HORAS_DIA: int = 24
        DIAS_MES: int = 30

        minutosLimpiar: float = superficie / METROS_POR_MIN
        totalMinLimpiarConPlantas: float = minutosLimpiar + (tiempoSubirPlanta * numPlantas)

        totalEurosPorMinuto = totalMinLimpiarConPlantas * EUROS_MIN
        totalEurosDia = totalEurosPorMinuto * HORAS_DIA
        totalEurosMes = totalEurosDia * DIAS_MES

        print(f'El tiempo que se aha tardado en limpiar es de {totalMinLimpiarConPlantas} minutos')
        print(f'El coste mensual es de {totalEurosMes}€')

    def __str__(self) -> str:
        return f"Nombre: {self.__nombre} | Plantas: {self.__numPlantas} | {self.__superficie} m²"


# CLASES HIJAS

class Hotel(Edificio):
    def __init__(self, nombre: str, numPlantas: int, superficie: int) -> None:
        super().__init__(nombre, numPlantas, superficie)

    def calcularCostVigilancia(self, superficie: int) -> None:

        METROS_POR_VIGILANTE: int = 1000
        EUROS_VIGILANTE: int = 1300
        PLUS_PELIGROSIDAD: int = 500

        cantidadVigilantes: float = superficie / METROS_POR_VIGILANTE
        sueldoVigilantes: float = cantidadVigilantes * EUROS_VIGILANTE
        totalDineroPorVigilantes: float = sueldoVigilantes + (PLUS_PELIGROSIDAD * cantidadVigilantes)

        print(f'Cuesta {totalDineroPorVigilantes}€ al mes contratar vigilantes en {self.getNombre()}')

class Hospital(Edificio):
    def __init__(self, nombre: str, numPlantas: int, superficie: int) -> None:
        super().__init__(nombre, numPlantas, superficie)

    def calcularCostVigilancia(self, superficie: int) -> None:

        METROS_POR_VIGILANTE: int = 1000
        EUROS_VIGILANTE: int = 1300

        cantidadVigilantes: float = superficie / METROS_POR_VIGILANTE
        sueldoVigilantes: float = cantidadVigilantes * EUROS_VIGILANTE
    
        print(f'Cuesta {sueldoVigilantes}€ al mes contratar vigilantes en {self.getNombre()}')

class Cine(Edificio):
    def __init__(self, nombre: str, numPlantas: int, superficie: int) -> None:
        super().__init__(nombre, numPlantas, superficie)

    def calcularCostVigilancia(self) -> None:
        pass