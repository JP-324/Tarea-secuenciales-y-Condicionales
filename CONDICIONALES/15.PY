print("Se procedera a calcular las horas extras de un trabajor segun su salario y su categoria.\n")
nombre = ""
categoria = 0
horas_extras = 0
while nombre == "" or categoria == 0 or horas_extras == 0:
    nombre = input("\nIngrese el nombre del empleado: ")
    categoria = int(input("Ingrese la categoria del empleado: "))
    salario = float(input("Ingrese el salario del empleado: "))
    horas_extras = int(input("Ingrese la cantidad de horas extras trabajadas: "))
    if nombre == "":
        i = input("\nEl nombre esta en blanco, intentelo de nuevo.")
    elif categoria == 0:
        i = input("\nLa categoria esta en cero, intentelo de nuevo.")
    elif salario == 0:
        i = input("\nEl salario esta en cero, intentelo de nuevo.")    
    elif categoria > 3:
        i = input("\nLos empleados con categoria mayor a 3 no cobran horas extras.")
        break
    elif horas_extras == 0:
        i = input("\nLas horas extras estan en cero, intentelo de nuevo.")
if horas_extras > 30:
    horas_extras = 30    
if categoria <= 3 and categoria > 0:
    if categoria == 1:
        hora = 40
    elif categoria == 2:
        hora = 50
    else:
        hora = 85
    print(f"\nEl empleado {nombre} va a cobrar:\nSu salario Bs. {salario}\nHoras extras ({horas_extras}), Bs. {horas_extras * hora}\nTotal a Cobrar Bs. {salario + (horas_extras * hora)}")