from math import ceil 

class Hotel:
    def __init__(self, nomHotel: str, numHabitacions: int, numPlantes: int, superficieTotal: float) -> None:
            self.__nomHotel: str        = nomHotel
            self.__numHabitacions: int  = numHabitacions
            self.__numPlantes: int      = numPlantes
            self.__superficieTotal: float = superficieTotal

# Mètodes GETTERS
    def getNomHotel(self) -> str:
        return self.__nomHotel
    
    def getNumHabitacions(self) -> int:
        return self.__numHabitacions
    
    def getNumPlantes(self) -> int:
        return self.__numPlantes
    
    def getSuperficieTotal(self) -> float:
        return self.__superficieTotal


# Mètodes SETTERS
    
    def setNumHabitacions(self, numHabitacions: int) -> None:
        self.__numHabitacions = numHabitacions

    def setNumPlantes(self, numPlantes: int) -> None:
        self.__numPlantes = numPlantes

    def setSuperficieTotal(self, superficieTotal: float) -> None:
        self.__superficieTotal = superficieTotal

# Otres mètodes

    def calcularManteniment(self) -> None:

        HABITACIONES_PERSONA: int = 20
        SUELDO_PERSONA: int = 1500
        personas: int = ceil(self.__numHabitacions / HABITACIONES_PERSONA)
        costeMensual: int = SUELDO_PERSONA * personas

        print(f'Personas necesarias para limpiar: {personas}')
        print(f'Coste mensual del servicio: {costeMensual}€')

    def __str__(self) -> str: 
        return f"Hotel {self.__nomHotel} | {self.__numHabitacions} habitacions | " f"{self.__numPlantes} plantes | {self.__superficieTotal} m²"
