# Un concessionari té inicialment els vehicles següents:
# ["Saab", "Volvo", "BMW", "Mercedes", "Fiat"]
# El programa ha de permetre mostrar els vehicles, buscar una marca, vendre un vehicle i afegir-ne un de nou. 
# El concessionari té una capacitat màxima de 8 vehicles i no pot haver-hi marques repetides.
# Les cerques no han de distingir entre majúscules i minúscules.
# Restricció: no es poden utilitzar in, index() ni remove() per buscar o eliminar vehicles.
# Funcions: demanarEnterRang(), mostrarCotxes(), cercarCotxe(), vendreCotxe(), afegirCotxe() i main().

#  def demanarEnterRang()

def menu(carsList: list[str]):
    print("Welcome to The concessionari. What do you want to do?: ")
    menuOptions = ['1. Search a car', 
                '2. Buy a car', 
                '3. Sell a car',
                '0. Exit']
    
    for i in menuOptions: print(i)
    chooseMenu: int = int(input('Choose a number to continue: '))

    while chooseMenu < 0 or chooseMenu > 3:
        chooseMenu = int(input('Error you have to choose 0-3: '))
        
    match chooseMenu:
        case 1:
            searchCar(carsList)
        case 2:
            deleteCar(carsList)
        case 3:
            addCar(carsList)
        case 0:
            print('Exit')
            return
        case _:
            print('Error you have to choose 1-3')

def askContinue(carsList: list[str]):
    askContinue: int = int(input('What do you want to do?: 1. Go to the MENU 2. Exit: '))

    if askContinue == 1:
        menu(carsList)
    elif askContinue == 2:
        print('Exit')
        return
    else: 
        print('Error. Choose 1 or 2: ')

def printCars(cars: list[str]):
    print(f'The available cars are: {", ".join(cars)}')

def searchCar(carsList: list[str]) -> str:
    print('Search a car: ')
    printCars(carsList)
    
    finded = False

    while not finded:
        element = input('Which car are you looking for?: ')

        for car in carsList:
            if car.casefold() == element.casefold():
                finded = True

        if not finded:
            print(f'{element} IS NOT available.')
 
    print(f'Yes, {element} IS available')
    askContinue(carsList)

    return element   

def deleteCar(carsList: list[str]):
    print('Buy a car: ')
    printCars(carsList)
    deleteElement = input(f'Do you want to buy a car yes-no?: ')
    
    if deleteElement == 'yes'.casefold():
        carFinded: bool = False

        while not carFinded:
            chooseElement = input('Which one?: ')
            for i in carsList:
                if chooseElement.casefold() == i.casefold():
                    carFinded = True

            if not carFinded:
                print(f'{chooseElement} IS NOT available')     

        newCarsList: list[str] = []
        for i in carsList:
            if chooseElement.casefold() != i.casefold():
                newCarsList.append(i)

        print(f'Congratulations, you have bought a {chooseElement}. \nThe available cars now are {newCarsList}')
        askContinue(carsList)

    elif deleteElement == 'no'.casefold():
        askContinue(carsList)
    
    else:
        print('Sorry, you have to write yes or no')
        askContinue(carsList)

def  addCar(carsList: list[str]):
    MAX_CAPACITY = 7 
    addElement = input(f'Do you want to add a car?: ')

    if addElement == 'yes'.casefold():
        element = input(f'Wich one?: ')
        if len(carsList) <= MAX_CAPACITY:
            noRepeatCar = False
            for car in carsList:
                if element.casefold() != car.casefold():
                    noRepeatCar = True

            if noRepeatCar:
                carsList.append(element)
            print(f'Congratulations, you have sold the {element}. \nThe available cars now are {carsList}')
            askContinue(carsList)

        else:
            print('We are at full capacity')
            askContinue(carsList)

    elif addElement == 'no'.casefold():
            askContinue(carsList)
    else:
        print('Sorry, you have to write yes or no')
        askContinue(carsList)


def main() -> None:

    carsList: list[str] = ["Saab", "Volvo", "BMW", "Mercedes", "Fiat"]
    
    menu(carsList)


    
main()