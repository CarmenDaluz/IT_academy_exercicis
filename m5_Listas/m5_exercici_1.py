# EXERCICI 1

# Fer un programa que pregunti a l'usuari/ària pel nombre (número) de paraules que es volen introduir en una llista.

# Un cop l'usuari/ària respongui, el programa haurà de preguntar per tantes paraules com el nombre (número) de paraules que ha dit l’usuari/ària que volia introduir.

# Les paraules s'aniran guardant a la llista i un cop han sigut totes introduïdes, es mostren per pantalla.

number: int = int(input('¿Qué número de palabras quieres introducir en la lista?: '))
wordsList: list[str] = []

for i in range(number):
    wordsResponse: str = (input(f'¿Qué palabras {i + 1}?: '))
    wordsList.append(wordsResponse)
print(wordsList)
    
for i in range(len(x)):
    wordList_mostrar = wordList_mostrar + wordsList[i] + " "

