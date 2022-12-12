import os 

nota_de_practica_1 = float (input("Ingresa el valor de la practica 1:  "))
nota_de_practica_2 = float (input("Ingresa el valor de la practica 2:  "))
nota_de_practica_3 = float (input("Ingresa el valor de la practica 3:  "))
promedio_final=nota_de_practica_1+nota_de_practica_2+nota_de_practica_3
if nota_de_practica_1>=10 and nota_de_practica_1<18:
    promedio_final=promedio_final+2
if nota_de_practica_2>=10 and nota_de_practica_2<18:
    promedio_final=promedio_final+2
if nota_de_practica_3>=10 and nota_de_practica_3<18:
    promedio_final+promedio_final+2
if nota_de_practica_1>=18 and nota_de_practica_1<20:
    promedio_final=promedio_final-nota_de_practica_1+20
if nota_de_practica_2>=18 and nota_de_practica_2<20:
    promedio_final=promedio_final-nota_de_practica_2+20
if nota_de_practica_3>=18 and nota_de_practica_3<20:
    promedio_final=promedio_final-nota_de_practica_3+20
promedio_fina=promedio_final/3
print ("valor de promedio final:" + repr(promedio_final))
print()
os.system ("pause")