# # #EXERCICI EXTRA 2:

# Realitza un programa que pinti la lletra L per pantalla feta amb asteriscs.

# El programa demanarà l'altura.

# El pal horitzontal de la L tindrà una longitud de la meitat (divisió entera entre 2) de l'altura més un.

# Exemple:

# Introduïu l'alçada de la L : 5

# La base serà  la divisió del nombre entre 2 : (5 / 2) + 1 = 3

print("Dibuixarem una L feta amb asteriscs")
asteriscs: int = int(input("Introduïu quants asteriscs té l'altura: "))
numBase:int = int(asteriscs/2) + 1 


for i in range(asteriscs):
    print('*')
    
print(numBase * '* ')
