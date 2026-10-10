# Calculadora arcaica. El programa demana a l’usuari/ària que introdueixi dos números i l’operació que desitja realitzar. 

# Cada operació (suma, resta, multiplicació, divisió i mòdul) estarà programada en una funció diferent.


def sumar(num1: int, num2: int) -> int:
    return num1 + num2

def restar(num1: int, num2: int) -> int:
    return num1 - num2

def multiplicar(num1: int, num2: int) -> int:
    return num1 * num2

def dividir(num1: int, num2: int) -> float | None:
    if num2 == 0:
          print('No es pot dividir entre zero')
          return None 
    return num1 / num2
# def divExacta(num1:int, num2:int) -> str:
#    if num2 == 0:
#       return "El divisor no pot ser 0"
#    


num1: int = int(input('Elige un número: '))
num2: int = int(input('Elige otro número: '))
operator: str = (input('Elige un operador +,-,x,/: '))

match operator:
  case '+':
    print(sumar(num1,num2))
  case '-':
    print(restar(num1,num2)), 
  case 'x':
    print(multiplicar(num1,num2)), 
  case '/':
    print(dividir(num1,num2)), 

  case _:
    print("error")
