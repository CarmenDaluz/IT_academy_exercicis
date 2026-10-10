userCar: str = str(input("¿Qué coche quiere comprar? Saab, Volvo, BMW, Mercedes, Fiat: "))

cars: list[str] = ["Saab", "Volvo", "BMW", "Mercedes", "Fiat"]


if userCar in cars:
    cars.remove(userCar)
    print('Coche comprado correctamente')
    print(f'Los coches que quedan son: {cars}')
else:
    print('Coche no disponible')
