# Fes un programa que pregunti a l'usuari/ària dos nombres enters al qual anomenaràs dividend i divisor respectivament.

# El divisor haurà d'estar comprès entre 2 i 7.

# En cas contrari, el programa haurà de mostrar un missatge d'error.

# Si el divisor és correcte (2-7) mostra en pantalla si el dividend és múltiple del divisor, o no.

dividendo: int = int(input('Escribe un número entero: '))
divisor: int = int(input('Escribe otro número entero entre 2-7: '))

if divisor >= 2 and divisor <= 7: 
    resto: int = dividendo % divisor
    if resto == 0:
        print(f'El {dividendo} es múltiplo del {divisor}')
    else:
        print(f'El {dividendo} no es múltiplo del {divisor}')

else:
    print(f'Error. El {divisor} no está entre 2 y 7')
