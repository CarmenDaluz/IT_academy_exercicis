# # EXERCICI 2:

# El programa demana dos nombres enters i llavors calcula la suma dels valors compresos entre els dos números, inclosos. 
# # Exemple: 4 i 6  --> resultat = 4 + 5 + 6 = 15

number1: int = int(input('Escribe un número: '))


number2: int = int(input('Escribe otro número: '))
result: int = 0 #inicializar a 0

if number2 < number1:
    auxiliar: int = number1
    number1 = number2
    number2 = auxiliar

for i in range(number1, number2 + 1):
    result = result + i
print(f'La suma de los números comprendidos es: {result}')