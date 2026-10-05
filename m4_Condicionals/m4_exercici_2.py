
age: int = int(input("introduzca su edad:"))

if age <= 5:
  print("preescolar")

elif age >= 6 and age <= 11:
    print("primària")

elif age >= 12 and age <= 15:
    print("ESO")

elif age >= 16 and age <= 17:
    print("Batxillerat")

elif age >= 18:
    print("FP o Universitat")


