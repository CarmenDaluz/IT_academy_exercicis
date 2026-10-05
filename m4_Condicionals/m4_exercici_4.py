numero_mes: int = int(input("introduzca (1-12):"))


match mes:
    case 1:
        print ("El mes de enero tiene 31 días") 
    case 2:
        print ("El mes de febrero tiene 31 días") 
    case 3:
        print ("El mes de marzo tiene 31 días")
    case 4:
        print ("El mes de abril tiene 31 días")
    case 5:
        print ("El mes de mayo tiene 31 días")
    case 6:
        print ("El mes de junio tiene 31 días")
    case 7:
        print ("El mes de julio tiene 31 días") 
    case 8:
        print ("El mes de agosto tiene 31 días")
    case 9:
        print ("El mes de septiembre tiene 31 días")
    case 10:
        print ("El mes de octubre tiene 31 días")
    case 11:
        print ("El mes de noviembre tiene 31 días")
    case 12:
        print ("El mes de diciembre tiene 31 días")
    case _:
        print ("Error")

