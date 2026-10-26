# Crea un programa donde el usuario introduzca una temperatura en °C y se muestre por pantalla la conversión en ° Fahrenheit.

# K = 32;

# Fórmula (0 °C  × 9 / 5) + K = 32 °F



def deCelsiusaFahrenheit(tempCelsius: float) -> float:
    
    fah: float = (tempCelsius * 9 / 5) + K

    return fah

def deFahrenheitaCelsius(tempFah: float) -> float:
    
    celsius: float = (tempFah - K) * 5/9

    return celsius

K: int = 32
tempCelsius: float = float(input('Introduce una temperatura en grados centígrados: '))
fah = deCelsiusaFahrenheit(tempCelsius)
print(f'La temperatura de {tempCelsius}°C es {fah:.2f}°F en Fahrenheit')

tempFah: float = float(input('Introduce una temperatura en fahrenheit: '))
celsius =  deFahrenheitaCelsius(tempFah)
print(f'La temperatura de {tempFah}°F es {celsius:.2f}°C en Celsius')



