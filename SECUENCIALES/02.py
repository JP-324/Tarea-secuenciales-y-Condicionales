metros=int(input("DIGITE UNA CANTIDAD EN METROS"))

centimetros=metros*100
pulgadas=centimetros/2.54
pies=pulgadas/12
yardas=pies/3

print("centimetros:",format(centimetros,".2f"),"cm")
print("pulgadas :",format(pulgadas,".2f"),"in")
print("pies :",format(pies,".2f"),"ft")
print("yardas",format(yardas,".2f"),"yd")