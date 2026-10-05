# EXERCICI 6

# Fer un programa que demani a l’usuari/ària quin dia i quin mes va néixer, amb aquesta informació el programa mostra per pantalla, de quin signe del zodíac és.

# Àries-Aries (21.03 — 19.04)
# Taure-Tauro (20.04 — 20.05)
# Bessons-Géminis (21.05 — 20.06)
# Cranc-Cáncer (21.06 — 22.07)
# Lleó-Leo (23.07 — 22.08)
# Verge-Virgo (23.08 — 22.09)
# Balança-Libra (23.09 — 22.10)
# Escorpí-Escorpión (23.10 — 21.11)
# Sagitari-Sagitario (22.11 — 21.12)
# Capricorn-Capricornio (22.12 — 19.01)
# Aquari-Acuario (20.01 — 18.02)
# Peixos-Piscis (19.02 — 20.03)

day: int = int(input('¿Cual es el día de tu cumpleaños?: '))
month: int = int(input('¿Cual es el nº de mes de tu cumpleaños?: '))

message: str = 'Tu signo de zodiaco es'
match month:
  case 1:
    if day >=  1 and day <= 19:
        print(f'{message} Capricornio')
    elif day >= 20 and day <= 31:
        print(f'{message} Acuario')
  case 2:
    if day >=  1 and day <= 18:
        print(f'{message} Acuario')
    elif day >= 19 and day <= 29:
        print(f'{message} Piscis')
  case 3:
    if day >=  1 and day <= 20:
        print(f'{message} Piscis')
    elif day >= 21 and day <= 31:
        print(f'{message} Aries')
  case 4:
    if day >=  1 and day <= 19:
        print(f'{message} Aries')
    elif day >= 20 and day <= 31:
        print(f'{message} Tauro')
  case 5:
    if day >=  1 and day <= 20:
        print(f'{message} Tauro')
    elif day >= 21 and day <= 31:
        print(f'{message} Géminis')
  case 6:
    if day >=  1 and day <= 20:
        print(f'{message} Géminis')
    elif day >= 21 and day <= 31:
        print(f'{message} Cáncer')
  case 7:
    if day >=  1 and day <= 22:
        print(f'{message} Cáncer')
    elif day >= 23 and day <= 31:
        print(f'{message} Leo')
  case 8:
    if day >=  1 and day <= 22:
        print(f'{message} Leo')
    elif day >= 23 and day <= 31:
        print(f'{message} Virgo')
  case 9:
    if day >=  1 and day <= 22:
        print(f'{message} Virgo')
    elif day >= 23 and day <= 31:
        print(f'{message} Libra')
  case 10:
    if day >=  1 and day <= 22:
        print(f'{message} Libra')
    elif day >= 23 and day <= 31:
        print(f'{message} Escorpio')
  case 11:
    if day >=  1 and day <= 21:
        print(f'{message} Escorpio')
    elif day >= 22 and day <= 31:
        print(f'{message} Sagitario')
  case 12:
    if day >=  1 and day <= 21:
        print(f'{message} Sagitario')
    elif day >= 22 and day <= 31:
        print(f'{message} Capricornio')
  case _:
    print("Error. Has introducido mal el mes.")