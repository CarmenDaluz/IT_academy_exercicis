
#EXERCICI 5

# Has de modificar el programa de les beques (ara el programa només ha de poder donar 5 beques).

# El programa anirà demanant les dades dels/les alumnes fins que es donin aquestes 5 beques. Un cop el programa hagi assignat les 5 beques s’ha de mostrar per pantalla els noms dels/les 5 alumnes que tenen beca.

becas: list = []
maxBecas: int  = 5

while len(becas) < maxBecas:
    age: int = int(input(f'Alumno nº{len(becas) + 1} ¿Cuál es tu edad?: '))
    title: str = (input('¿Tienes título universitario? si /no: ')).lower()
    paro: str = (input('¿Estás en paro? si/no: ')).lower()

    if  age < 18:
        print('Error. Menor de edad')

    elif title == 'si' or paro == 'si':
        print(f'¡¡Enhorabuena!! Alumno nº{len(becas) +1} Se te ha concedido la beca')
        name: str = (input('¿Cuál es tu nombre: '))
        becas.append(name)

    else:
        print('Lo siento, no se te ha concedido la beca')
              
 
print(f'Los {maxBecas} alumnos con beca son: {', '.join(becas)}') #ESTO SE USA??       
