# Demana a l'usuari/ària un número entre 0 i 99 i mostra'l escrit en lletres (pots fer-ho en català o castellà).

# Exemple: 56 (cinquanta-sis) o 56 (cincuenta y seis)



def pedirNum() -> int:
  num: int = int(input('Escribe un número entre 0 y 99: '))
  while num < 0 or num > 99:
    num: int = int(input('Error. El número tiene que estar entre 0 y 99. Prueba otra vez: '))

  return num


numUnicos: list[str] = ['cero','uno', 'dos', 'tres', 'cuatro',' cinco', 'seis', 'siete', 'ocho', 'nueve', 'diez', 'once', 'doce', 'trece','catorce',
                         'quince', 'dieciseis', 'diecisiete', 'dieciocho', 'diecinueve', 'veinte', 'veintiuno', 'veintidos', 'veintitres', 'veinticuatro', 
                         'veinticinco', 'veintiseis', 'veintisiete', 'veintiocho', 'veintinueve']

numDecenas: list[str] =['', '', 'veinte','treinta', 'cuarenta', 'cincuenta', 'sesenta', 'setenta', 'ochenta', 'noventa']


def numeroAPalabras(num: int):

  if num < 30:
    print(numUnicos[num])
  
  else:
    decena = num // 10 
    unidad = num % 10

    if unidad == 0:
      print(numDecenas[decena])
    else:
      print(f'{numDecenas[decena]} y {numUnicos[unidad]}')


def main():
  numero =  pedirNum()
  numeroAPalabras(numero)

main()