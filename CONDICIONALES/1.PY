#Calculadora.
print ("  \n       Calculadora.")
n1= float (input("Digite N1: "))
n2= float (input("Digite N2: "))

print ("\n  ¿Que operacion que desea realizar?.")
op = input("A) Suma. \nB) Resta. \nC) Multiplicacion. \nD) Division.\n>Opcion: ").lower()
print ("\n")
if op=='a':
    print(f"Usted eligió sumar.\nEl resultado de {n1} mas {n2} es: {n1+n2}")
elif op=='b':
    print (f"Usted eligió restar.\nEl resultado de {n1} menos {n2} es: {n1-n2}")
elif op=='c':
    print (f"Usted eligió multiplicar.\nEl resultado de {n1} por {n2} es: {n1*n2}")
elif op=='d':
    print (f"Usted eligió dividir.\nEl resultado de {n1} dividido {n2} es: {n1/n2:.2f}")
else:
    print (f"Usted introdujo una opcion incorrecta, vuelva a intentarlo.")