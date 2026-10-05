
name: str = str(input('¿Cuál es tu nombre: '))
lastName: str = str(input('¿Cuál es tu apellido: '))
age: int = int(input('¿Cuál es tu edad: '))

if age < 1 or age >= 100:
  print('edad no válida')
  
elif age >= 18:
  print(f'Mi nombre es {name} {lastName}, y soy MAYOR de edad')
 
else:
  print(f'Mi nombre es {name} {lastName}, y soy MENOR de edad')



