
day: int = int(input("introduzca el número del día que nació 1-31:"))
month: int = int(input("introduzca el número del mes que nació 1-12"))

missatge: str = ('No es correcte')
match month:
        case 1:
                if day >1 and day <= 19:
                    missatge('Capricornio')
                elif day > 19 and day <= 31:
                    missatge('Acuario')  
                
                else:
                    missatge('No valid')   
        case 2:
                    if day <=18:
                        missatge('Acuario')  
                        
                    else:
                        missatge('Piscis')  
        case 3:
                    if day <=20:
                        missatge('Piscis')  
                    else:
                        missatge('Aries')

        case 4:
                    if day <=19:
                        missatge('Aries')  
                    else:
                        missatge('Tauro')
        case 5:
                    if day <=20:
                        missatge('Tauro')  
                    else:
                        missatge('Géminis')
        case 6:
                    if day <=20:
                        missatge('Géminis')  
                    else:
                        missatge('Cáncer')
        case 7:
                    if day <=22:
                        missatge('Cáncer')  
                    else:
                        missatge('Leo')
        case 8:
                    if day <=22:
                        missatge('Leo')  
                    else:
                        missatge('Virgo')
        case 9:
                    if day <=22:
                        missatge('Virgo')  
                    else:
                        missatge('Libra')

        case 10:
                    if day <=22:
                        missatge('Libra')  
                    else:
                        missatge('Escorpio')
        case 11:
                    if day <=21:
                        missatge('Escorpio')  
                    else:
                        missatge('Sagitario')
        case 12:
                    if day <=21:
                        missatge('Sagitario')  
                    else:
                        missatge('Capricornio')
        case _:
              missatge('no valid')

print('missatge')