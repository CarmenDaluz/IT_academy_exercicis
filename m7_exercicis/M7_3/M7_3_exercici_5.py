# Comprovar si una frase introduïda per l’usuari/ària està formada només per minúscules, només per majúscules o per minúscules i majúscules.

frase: str = input('Introduce una frase: ')

def comprobarFrase(frase):
    if frase.isupper():
        print('Todos los caracteres estan en MAYÚSCULA')
    elif frase.islower():
        print('Todos los caracteres estan en MINÚSCULA')
    else:
        print('Hay tanto caracteres en MAYÚSCULA como en MINÚSCULA')   

comprobarFrase(frase)



# if frase.isupper():
#     print('Todos los caracteres estan en MAYÚSCULA')
# elif frase.islower():
#     print('Todos los caracteres estan en MINÚSCULA')
# else:
#     print('Hay tanto caracteres en MAYÚSCULA como en MINÚSCULA')   
