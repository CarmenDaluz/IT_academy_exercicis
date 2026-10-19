# Demana a l'usuari/ària un número entre 0 i 99 i mostra'l escrit en lletres (pots fer-ho en català o castellà).

# Exemple: 56 (cinquanta-sis) o 56 (cincuenta y seis)

num: int = int(input('Escribe un número entre 0 y 99: '))



if num >= 0 and num <=99:
    print('')

day = 4
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")