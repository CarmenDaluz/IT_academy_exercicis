num1: int = int(input("introduzca un número:"))
num2: int = int(input("introduzca otro número:"))
operador: str = str(input("introduzca +,-,*,/"))

if operador == "+":
    print(num1 + num2)
elif operador == "-":
    print(num1 - num2)
elif operador == "*":
    print(num1 * num2)
elif operador == "/":
    print(num1 / num2)

match operador:
    case "+":
        print(f'El resultat es: {num1 + num2:.2f}') #.2f es 2 decimales
    case "-":
        print(f'El resultat es: {num1 - num2:.2f}') #.2f es 2 decimales
    case "*":
        print(f'El resultat es: {num1 * num2:.2f}') #.2f es 2 decimales
    case "/":
        if num2 != 0:
            print(f"El resultat es: {num1 / num2:.2f}") #.2f es 2 decimales
        else:
            print('No es pot dividir entre zero')
    

