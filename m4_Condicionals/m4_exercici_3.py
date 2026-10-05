# EXERCICI 4
# Una escola d’idiomes concedeix beques a futurs estudiants si compleixen una sèrie de requisits.
# A l'alumne/a se li assigna una beca si és major d’edat i si té un títol universitari. 
# O també se li assigna una beca si l’alumne/a està a l’atur. 

# El programa demana les tres dades per pantalla i en finalitzar mostra si l’alumne/a té la beca o no.
age: int = int(input('¿Cuál es tu edad?: '))
title: str = (input('¿Tienes título universitario? si /no: ')).lower()
paro: str = (input('¿Estás en paro? si/no: ')).lower()


if age >= 18:
    if title == 'si' or paro == 'si':
        print('Se te ha concedido la beca')
    else:
        print('no se te ha concedido la beca')
else:
    print('Edad no válida')