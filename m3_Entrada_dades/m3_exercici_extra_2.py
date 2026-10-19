# Escriu un programa que calculi els litres de pintura necessaris per a pintar una paret rectangular.

# Un litre de pintura cobreix aproximadament, 12 m² en una sola mà.

# Crear una constant, Cobertura a Litros (recordar les convencions de noms) per a guardar la dada de cobertura de la pintura (12 m²).

# Hauràs de demanar a l'usuari/ària:

# L'alt i ample de la paret (multiplicant sabràs l'àrea de la mateixa).
# El nombre de mans a aplicar.
# Mostra en pantalla els litres de pintura a utilitzar.

COBERTURA_METROS_X_LITRO: float = 12

numAlto: float = float(input('¿Cuál es el alto de la pared?: '))
numAncho: float = float(input('¿Cuál es el ancho de la pared?: '))
numManos: int = int(input('¿Cuántas manos quieres dar?: '))

areaParedMetros: float = numAlto * numAncho
coberturaParedLitrosPorMano: float = areaParedMetros / COBERTURA_METROS_X_LITRO
litrosTotales: float = numManos * coberturaParedLitrosPorMano

print(f'El área de la pared es de {areaParedMetros} m² y dando {numManos} manos, necesitamos {litrosTotales:.2f} litros para cubrirla')


