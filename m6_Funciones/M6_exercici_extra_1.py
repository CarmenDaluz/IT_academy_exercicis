# Fes un programa amb 3 funcions. El programa ha de cridar a les 3 funcions e interactuar amb elles de la següent manera:

# a. Crea una funció sense paràmetres i sense retorn que imprimeixi per consola “sóc una funció”.

# b. Crea una funció que rebi una llista de números com a paràmetre, imprimeixi el número més gran per pantalla i retorni l’índex 
# d'on es troba el número més petit. Crea una llista de 5 números i crida a la funció que acabes de crear per imprimir el número més petit de l’array. 

# c. Crea una funció que rebi dos números com a paràmetres i retorni una llista amb tots els números compresos entre ells.
# Crida a la funció que acabes de crear amb els dos números que vulguis i imprimeix la llista que et retorna.
# 

def printInfo() -> None:
    print("I'm a function :)")

def createList():
    print("Let's write a 5 number list:")
    lengthList: int = 5
    numList: list = []

    for i in range(1, lengthList + 1):
        numbersInList: int = int(input(f'Which number is the nº{i}: '))
        numList.append(numbersInList)

    return numList


def numBiggestSmallest(numList: list) -> int:
    
    isBiggest: int = numList[0]
    isSmallest: int = numList[0]
    
    for i in numList:
        if i > isBiggest:
            isBiggest = i
        elif i < isSmallest:
            isSmallest = i

    print(f'The biggest number of {numList} is {isBiggest}')
    indexIsSmallest: int = numList.index(isSmallest)

    return indexIsSmallest

def receiveNumbers(num1: int, num2: int) -> list:
    rangeList: list = []
    if num1 < num2:
        for i in range(num1, num2 + 1):
            rangeList.append(i)
    else:
        for i in range(num1, num2 - 1, -1):
            rangeList.append(i)

    return rangeList

def main():

    #  Parte a:
    print('EJERCICIO: PARTE A')
    printInfo()

    #  Parte b:
    print('EJERCICIO: PARTE B')
    numList = createList() 
    indexIsSmallest = numBiggestSmallest(numList)
    print(f'The smallest number of {numList} is {numList[indexIsSmallest]} and its index is {indexIsSmallest}')

    #  Parte c:
    print('EJERCICIO: PARTE C')
    num1: int = int(input('Write one number: '))
    num2: int = int(input('Write other number: '))
    rangeList = receiveNumbers(num1, num2)
    print(f'The number range between {num1} and {num2} is {rangeList}')

main()
