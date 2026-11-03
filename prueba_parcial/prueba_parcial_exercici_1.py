# 1.- Donat el següent array de nombres: [15, 16, 8, 2, 4, 6, 2]
# Mostra per pantalla els múltiples de 3, el nombre més gran i el més petit de l'array


def checkMultiplesOfThree(numList: list[int]) -> list[int]:
    multiplesThree: list[int] = []

    for num in numList:
        if num % 3 == 0:
            multiplesThree.append(num)

    return multiplesThree

def smallestBiggestNum(numList: list[int]) -> None:
    biggestNum: int = numList[0]
    smallestNum: int = numList[0]

    for num in numList:
        if num > biggestNum:
            biggestNum = num
        elif num < smallestNum:
            smallestNum = num

    print(f'The biggest number is {biggestNum}')
    print(f'The smallest number is {smallestNum}')


def main():
    numbers: list[int] = [15, 16, 8, 2, 4, 6, 2]
    multiplesOfThree = checkMultiplesOfThree(numbers)


    print(f'In list: {numbers}, the multiples of three are: {multiplesOfThree}')
    smallestBiggestNum(numbers)

main()