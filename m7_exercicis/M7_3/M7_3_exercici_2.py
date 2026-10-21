# En aquest programa l’usuari/ària ha d’introduir un string i, utilitzant un bucle for, el programa ha de mostrar l’string al revés.


text: str = (input('Escribe una palabra: '))

text_invertir: str = ""

for caracter in text:
    text_invertir = caracter + text_invertir

print(f'El text invertir es {text_invertir}')

# print(text[::-1]) -> Para poner la palabra al revés