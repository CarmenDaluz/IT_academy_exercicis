from Ordenador import Ordinador


def crearOrdinador(marca: str, model: str, processador: str, ram: int, discodur: int) -> Ordinador:

    ordinador: Ordinador = Ordinador(marca, model, processador, ram, discodur)
    return ordinador

def demanarInfoPerOrdinador(quantitatOrdinadores: int) -> list[Ordinador]:
    ordinadoresList: list[Ordinador] = []

    for i in range(1, quantitatOrdinadores + 1):
        demanaMarca: str       = input(f'Marca ordinador {i}: ') 
        demanaModel: str       = input(f'Model ordinador {i}: ') 
        demanaProcessador: str = input(f'Processador ordinador {i}: ') 
        demanaRam: int         = int(input(f'Memoria RAM ordinador {i}: '))
        demanaDiscodur: int    = int(input(f'Capacitat disco dur ordinador {i}: '))

        ordinador: Ordinador = crearOrdinador(demanaMarca, demanaModel, demanaProcessador, demanaRam, demanaDiscodur)
        ordinadoresList.append(ordinador)

    return ordinadoresList

def imprimirLlista(llistaObjectes: list[Ordinador]) -> None:

    for i in range(len(llistaObjectes)):
        print(f'Ordinador {i + 1}: {llistaObjectes[i]}')

# PROGRAMA PRINCIPAL   
def main() -> None:

    QUANTITAT_ORDINADORES: int = 2 #Constante porque el ejercicio pide 2 exactamente

    ordinadoresList: list[Ordinador] = demanarInfoPerOrdinador(QUANTITAT_ORDINADORES) 
    imprimirLlista(ordinadoresList)
    
    print(ordinadoresList[0].executar('VSC'))
    
    ordinadoresList[0].setProcessador('I8')
    print(ordinadoresList[0])

    ordinadoresList[1].setRam(32)
    print(ordinadoresList[1])

main()