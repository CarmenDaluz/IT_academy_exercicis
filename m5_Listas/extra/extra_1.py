

nota: float = float(input("Introdueix la nota: "))
 
if nota < 0 or nota > 10:
    print("Nota no válida")
elif nota < 5:
    print("Suspès")
elif nota <= 6:
    print("Suficient")
elif nota <= 7:
    print("Bé")
elif nota <= 9:
    print("Notable")
else:
    print("Excel·lent")
 