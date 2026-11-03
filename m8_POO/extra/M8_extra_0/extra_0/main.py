from m8_POO.extra.M8_extra_0.extra_0.Coche import Coche

def crearCoche(lista: list) -> None:
    coche1: Coche = Coche('Fiat', 'Topolino', 100, 1200, 'Rojo')
    coche2: Coche = Coche('Renault', 'Laguna', 100, 1200, 'Verde')

    mostrarCoches(lista)

    print(f'Coche 1: {coche1}')
    print(coche1.arrancar())
    print(coche1.acelerar())

    print(f'Coche 2: {coche2}')
    print(coche2.girar())
    print(coche2.frenar())


def mostrarCoches(coches: list[Coche]) -> None:

    if len(coches) == 0:
        print('No hay coches disponibles')
        return
    
    for coche in coches:
        print(coche)

def main() -> None:
    coches: list[Coche] = [
        Coche("Audi", "A3", 110, 1200, "Blanco"),
        Coche("Seat", "Ibiza", 80, 1000, "Blanco"),
        Coche("Toyota", "Rav4", 110, 1300, "Gris"),
        Coche("BMW", "M3", 150, 1600, "Rojo"),
        Coche("Audi", "A1", 100, 1200, "Blanco")
    ]

    # crearCoche(coches) #Ejercicio para instanciar objetos en la class

# Si los atributos son públicos, podemos cambiar el valor así, sin necesidad de llamar al método
    coches[1].color = 'amarillo'

# Para cambiar el atributo llamando al método es asi:
    coches[0].setPotencia(1500)
    print(coches[3].getModelo()) 
    mostrarCoches(coches)

main()