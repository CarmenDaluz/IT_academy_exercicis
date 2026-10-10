# 4- Demana a l'usuari/ària quants productes ha comprat.
# A continuació, demana el preu de cadascun dels productes.
# En acabar, mostra:
# El preu total de la compra.
# Quants productes costaven més de 10 €.
# El preu mitjà dels productes.
# El nombre de productes ha de ser superior a 0.
 
numProducts: int = int(input('¿Cuántos productos has comprado?: '))
prizeProductsList = []
sumaPrizeProducts = 0
productos_caros = 0

for i in range(1, numProducts + 1):
    prizeProducts: float = float(input(f'¿Qué precio tiene el producto {i}?: ')) 
    prizeProductsList.append(prizeProducts)
    sumaPrizeProducts += prizeProducts
    if i > 10:
        productos_caros += 1




print(f'El precio total de la compra es: {sumaPrizeProducts} ')
print(f'Cuántos productos cuestan más de 10€: {productos_caros} ')
print(f'La lista de producto es: {prizeProductsList} ')