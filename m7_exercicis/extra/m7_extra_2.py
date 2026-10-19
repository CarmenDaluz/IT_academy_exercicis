# 2- Un cinema disposa de les tarifes següents:
# Edat                            Preu
# Menors de 12 anys                6 €
# De 12 a 64 anys                10 €
# A partir de 65 anys            7 €
 
# El programa ha de preguntar quantes entrades es volen comprar (entre 1 i 20) i demanar l'edat de cada espectador (entre 0 i 120 anys). Les edats s'han de guardar en una llista.
# Després, l'usuari ha de seleccionar entre un dia normal o el dia de l'espectador, que té un 20% de descompte. Finalment, cal mostrar l'import total amb dos decimals.
# Funcions: demanarEnterRang(), demanarEdats(), calcularPreuEntrada(), calcularTotal() i main().

edades = []
cantidadEntradas: int = int(input('¿Cuantas entradas quieres?: '))

for i in range(1, cantidadEntradas + 1):
    if cantidadEntradas >= 1 and cantidadEntradas <= 20:
        edad: int = int(input(f'¿Cuántos años tiene el espectador nº{i}'))


