# valores dentro de un array y sumar las 2 ultimas posiciones y añadir
# empieza en 0 y 1

def fibonacci(num: int) -> list[int]:
    fibonacci: list[int] = []
    
    for i in range(num):
        if i < 2:
            fibonacci.append(i)
        else:
            fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])

    return fibonacci


#PROGRAMA PRINCIPAL

num:int  = int(input("Introdueix otre num: "))

while num <= 0:
    num:int  = int(input("Cantidad incorrecta, Introdueix otre num: "))

resultat: list[int] = fibonacci(num)
print(resultat)
