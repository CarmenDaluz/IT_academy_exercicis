# 2.- Ens donen dues llistes. En un hi ha productes disponibles i en l'altre productes que volem comprar.
#    Productes disponibles: "xampú", "sabó", "patates", "bledes", "lletuga", "llimones", "kiwis", "alvocats", "fideus", "arròs", "cafè", "xocolata"
#    Productes que volem comprar: "xampú", "xocolata", "alvocats", "bledes", "llimones", "llimonada"
#    Crea una tercera llista amb els productes que estan en les dues anteriors. Aquests seran els productes que es poden comprar.


def compareProducts(list1: list[str], element: str) -> bool:

    for i in list1:
        if element == i:
            return True

    return False

def findEquals(list1: list[str], list2: list[str]) -> list[str]:
    result: list[str] = []

    for element in list1:
        if compareProducts(list2, element) and not compareProducts(result, element):
            result.append(element)

    return result

#  PROGRAMA PRINCIPAL:
def main():
    productesDisponibles: list[str] = ["xampú", "sabó", "patates", "bledes", "lletuga", "llimones", "kiwis", 
                                   "alvocats", "fideus", "arròs", "cafè", "xocolata"]

    productesVolemComprar: list[str] = ["xampú", "xocolata", "alvocats", "bledes", "llimones", "llimonada"]

    productesPodemComprar: list[str] = findEquals(productesDisponibles, productesVolemComprar)

    print(f'Els productes que es poden comprar són: {", ".join(productesPodemComprar)}.')

main()

