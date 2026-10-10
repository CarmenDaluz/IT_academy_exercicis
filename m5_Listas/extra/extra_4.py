# 3- Demana las temperaturas máximas dels 7 días de una semana.
# Al terminar, el programa ha de mostrar:
# La temperatura mitjana máxima.
# Quants dies han tingut una temperatura superior a 25 °C.
# Quants dies han tingut una temperatura inferior a 10 °C.

tempList = []
tempSup = []
sumaTemp = 0
dias_calor = 0
dias_frio = 0

for i in range(1, 8):
    temp: int = int(input(f'Temperatura máxima {i}: '))
    tempList.append(temp)
    sumaTemp = sumaTemp + temp

    if temp > 25:
        dias_calor += 1
    elif temp < 10:
        dias_frio += 1

mediaTemp = sumaTemp / 7

print(f'Las temperaturas son: {tempList}')
print(f'La media de temperatura es: {mediaTemp}')

#FALTA LO DEL FRIO Y CALOR