# EXERCICI 2:
# Fer un programa que li demani dos nombres enters a l’usuari/ària. Al final, el programa imprimeix per pantalla el següent missatge:  
# El resultat de la suma és: “valor”
# El resultat de la resta és: “valor”
# El resultat de la multiplicació és: “valor”
# El resultat de la divisió és: “valor”.

number1: int = int(input('Escribe un número: '))
number2: int = int(input('escribe otro número: '))

print(f'El resultat de la suma {number1} + {number2} és: {number1 + number2}')
print(f'El resultat de la resta {number1} - {number2} és: {number1 - number2}')
print(f'El resultat de la multiplicació {number1} x {number2} és: {number1 * number2}')
print(f'El resultat de la divisió {number1} / {number2} és: {number1 / number2}')