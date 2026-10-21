# 3- Una empresa vol conèixer els hàbits de mobilitat dels seus treballadors. Cada participant ha de seleccionar com es desplaça habitualment: a peu, en bicicleta o en transport públic.
# El programa ha de demanar el nombre de participants (entre 1 i 100), recollir els vots i guardar el nombre de respostes de cada categoria en una llista.
# Finalment, ha de mostrar quantes persones han seleccionat cada transport i quin percentatge representen sobre el total de participants.
 
# Funcions: demanarEnterRang(), recollirVots(), calcularPercentatges(), mostrarResultats() i main().

def demanarEnterRang() -> int: #Pide y valida
    numParticipants: int = int(input('Quin és el nombre de participants (entre 1-100): '))
    while numParticipants < 1 or numParticipants > 100:
        numParticipants: int = int(input('El nombre de participants no és valgut, vaig donar un altre numero: '))

    return numParticipants
    

def recollirVots(numParticipants: int) -> list: 
    aPeu: list = []
    bicicleta: list = []
    transportPublic: list = []
    
    for i in range(1, numParticipants + 1):
        desplacament: int = int(input(f'Com es desplaça el participant nº{i}: 1) Peu, 2) Bicicleta, 3)Transport public: '))
        while desplacament != 1 and desplacament != 2 and desplacament != 3:
            desplacament: int = int(input(f'Error, nombre no valgut. Com es desplaça el participant nº{i}: 1) Peu, 2) Bicicleta, 3)Transport public: '))

        match desplacament:
            case 1:
               aPeu.append(i) 
            case 2:
                bicicleta.append(i)
            case 3:
                transportPublic.append(i)
            
    return [aPeu, bicicleta, transportPublic]

def calcularPercentatges(numParticipants: int, aPeu: list, bicicleta: list, transportPublic: list) -> list:

    percentatgeAPeu = (len(aPeu) / numParticipants) * 100
    percentatgeBicicleta = (len(bicicleta) / numParticipants) * 100
    percentatgeTransportPublic = (len(transportPublic) / numParticipants) * 100

    return [percentatgeAPeu, percentatgeBicicleta, percentatgeTransportPublic]

def mostrarResultats(aPeu: list, bicicleta: list, transportPublic:list, percentatgeAPeu: float, percentatgeBicicleta: float, percentatgeTransportPublic: float):
  
    print(f'A peu van {len(aPeu)} persones, un {percentatgeAPeu:.2f}%; en bicicleta {len(bicicleta)} persones, un {percentatgeBicicleta:.2f}%; y en transport public van {len(transportPublic)} persones, un {percentatgeTransportPublic:.2f}%')
    


def main():
    numParticipants = demanarEnterRang()
    aPeu, bicicleta, transportPublic = recollirVots(numParticipants)
    percentatgeAPeu, percentatgeBicicleta, percentatgeTransportPublic = calcularPercentatges(numParticipants, aPeu, bicicleta, transportPublic)
    mostrarResultats(aPeu, bicicleta, transportPublic, percentatgeAPeu, percentatgeBicicleta, percentatgeTransportPublic)

main()