# 3.- Crear un mètode que rebi una llista de números per paràmetre 
# i retorni la suma més gran de dos nombres correlatius.

# Per exemple: [5, 3, 2, 8, 1, 6, 5], en aquest cas retornaria 11

def calculateBiggestSum(numList: list[int]) -> int:
   
    biggestSum: int = numList[0] + numList[1]

    for i in range(len(numList) - 1):
        sum: int = numList[i] + numList[i + 1]
        if sum > biggestSum:
            biggestSum = sum

    return biggestSum

#  PROGRAMA PRINCIPAL:
def main():
    llista: list[int] = [5, 3, 2, 8, 1, 6, 5]
    sumaMesGran: int = calculateBiggestSum(llista)

    print(f'La suma més gran de dos nombres correlatius és {sumaMesGran}, en la llista de nombres: {llista}')

main()