# L’usuari/ària introdueix un any “a” per teclat
# i el programa crida a una funció que indiqui si l’any és de traspàs o no.


def esTraspas(a: int)-> bool:
    
    if a % 400 == 0:
        return True
    elif (a % 4 == 0) and (a % 100 != 0):
        return True
    
    return False

def main():
    a: int  = int(input("Introdueix un any: "))
    esTraspas(a)
    while not esTraspas(a):
        a:int  = int(input("No es traspas, Introdueix otre any: "))
    print(f"L'any {a} és traspàs")
    
main()

