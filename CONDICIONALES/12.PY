palabra=str(input("Por favor escriba un caracter: "))
vocales=["a","e","i","o","u"]

if palabra.lower()in vocales[:]:
    print("Esto es una vocal")

else:
    print("esto no es una vocal")
