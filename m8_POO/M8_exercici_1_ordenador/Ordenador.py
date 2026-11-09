# Crea una classe en Python anomenada "Ordinador", en un fitxer anomenat ordinador.py

# Aquesta classe tindrà com a atributs la marca, el model, el processador, la quantitat de memòria RAM 
# i la capacitat del disc dur.

# A més del constructor, ha de disposar dels següents mètodes:

# Mètodes que permetin consultar cadascun dels atributs (getters).
# Mètodes que permetin modificar el processador, la quantitat de memòria 
# ram i la capacitat del disc dur. (setters).
# Un mètode que rebrà un paràmetre i retornarà una frase que digui:
# "En aquests moments s'està executant: 'X'" (X és el paràmetre rebut 
# pel mètode i que normalment serà el nom d'un programa).
# Exemple: "En aquests moments s'està executant: Chrome" 
# Un mètode que retornarà una descripció completa de l'ordinador (toString()).
# En un altre fitxer anomenat main.py, crea la funció crearOrdinadors().

# Demana a l'usuari/ària les dades de dos ordinadors. 

# Un cop introduïdes les dades dels dos ordinadors, crida als mètodes de la 
# classe Ordinador per comprovar que funcionen correctament.

class Ordinador:
    def __init__(self, marca : str, model : str, 
                 processador : str, ram : int, discodur : int) -> None:
            self.__marca: str       = marca
            self.__model: str       = model
            self.__processador: str = processador
            self.__ram: int         = ram
            self.__discodur: int    = discodur

# Mètodes de consulta cadascun dels atributs / GETTERS:
    def getMarca(self) -> str:
        return self.__marca
    
    def getModel(self) -> str:
        return self.__model
    
    def getProcessador(self) -> str:
        return self.__processador
    
    def getRam(self) -> int:
        return self.__ram

    def getDiscodur(self) -> int:
        return self.__discodur

# Mètodes permetin modificar: processador, ram i disco dur / SETTERS:
    def setProcessador(self, processador: str) -> None:
        self.__processador = processador
    
    def setRam(self, ram: int) -> None:
        self.__ram = ram

    def setDiscodur(self, discodur: int) -> None:
        self.__discodur = discodur

# Mètode que rebrà un paràmetre i retornarà una frase 
    def executar(self, programa: str) -> str:
        return f"En aquests moments s'està executant: {programa}"

# Mètode que retornarà una descripció completa de l'ordinador (toString())
    def __str__(self) -> str: 
        return f"{self.__marca} | {self.__model} | " f"{self.__processador} | {self.__ram} GB | " f"{self.__discodur} GB"
