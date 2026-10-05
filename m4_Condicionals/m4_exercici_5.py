# EXERICI 5
# Fer un programa que demani dos números i un operador(+,-,x,/).

# Al final, el programa ha d'imprimir per pantalla el resultat de fer l’operació que contingui la variable operador.

num1: int = int(input('Elige un número: '))
num2: int = int(input('Elige otro número: '))
operator: str = (input('Elige un operador +,-,x,/: '))

match operator:
  case '+':
    print(f"{num1} + {num2}= {num1 + num2:.2f}")
  case '-':
    print(f"{num1} - {num2}= {num1 - num2:.2f}")
  case 'x':
    print(f"{num1} x {num2}= {num1 * num2:.2f}")
  case '/':
    if num2 != 0:
      print(f"{num1} / {num2}= {num1 / num2:.2f}")
    else:
      print('No es pot dividir entre zero')
  case _:
    print("error")
