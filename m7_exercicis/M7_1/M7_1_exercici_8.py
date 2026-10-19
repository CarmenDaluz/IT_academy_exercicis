# Crea un programa donde el usuario introduzca una temperatura en °C y se muestre por pantalla la conversión en ° Fahrenheit.

# K = 32;

# Fórmula (0 °C  × 9 / 5) + K = 32 °F

temp:int = int(input('Introduce una temperatura: '))
fah: float = temp*9/5+32
print(f'La temperatura de {temp} ºC es {fah} en ºFahrenheit')

# def convertirFah():
#dos funciones una de convertir a fahrenheit y otra al reves, es hacer la conversion y retornar

