age: int = int(input("introduzca su edad:"))
title: str = input("¿tiene titulo? (si/no):").lower()[0]
paro: str = input("¿esta en el paro? (si/no):").lower()[0]



if (age >= 18 and title == "s") or paro == "s":
    print("BECA  ADJUDICADA")
else:
    print("NO ADJUDICADA")       

