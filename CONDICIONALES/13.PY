
print("ATLETISMO 100MTS HOMBRES")

posicion=int(input("introduzca su posicion en la competencia: "))

def competencia(posicion):
	resultado="clasificado"
	if posicion>10:
		resultado="descalificado"
	return resultado

print(competencia(posicion))