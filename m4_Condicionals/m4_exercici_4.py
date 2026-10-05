#EXERCICI 4:

# L’usuari/ària introdueix un número de mes per pantalla i mitjançant un match amb els 12 mesos de l’any, el programa calcula els dies del mes i mostra el següent:  

# Exemple: Si el número introduït és 1, llavors ha d'aparèixer per pantalla: “El mes de gener té 31 dies”

month: int = int(input('Elige un número de mes: '))


if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    message = ("tiene 31 días")
elif month == 2:
    message = ("tiene 28 días")
else:
    message = ("tiene 30 días")


match month:
    case 1:
        print(f"El mes de Enero tiene {message}")
    case 2:
        print(f"El mes de Febrero tiene {message}")
    case 3:
        print(f"El mes de Marzo tiene {message}")
    case 4:
        print(f"El mes de Abril tiene {message}")
    case 5:
        print(f"El mes de Mayo tiene {message}")
    case 6:
        print(f"El mes de Junio tiene {message}")
    case 7:
        print(f"El mes de Julio tiene {message}")
    case 8:
        print(f"El mes de Agosto tiene {message}")
    case 9:
        print(f"El mes de Septiembre tiene {message}")
    case 10:
        print(f"El mes de Octubre tiene {message}")
    case 11:
        print(f"El mes de Noviembre tiene {message}")
    case 12:
        print(f"El mes de Diciembre tiene {message}")
