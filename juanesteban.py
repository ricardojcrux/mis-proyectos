n1= input("Selecione la operación que desea realizar: \na) Costos de producción \nb) Liquidación de salario \nc) Ingreso disponible en una economía abierta \n")

if n1=="a":
  k=int(input("Ingrese el valor de materia prima: "))
  l=int(input("Ingrese el valor de la mano de obra: "))
  c=int(input("Ingrese el valor de los costos variables: "))
  suma=k+c+l
  print("Los costos de producción son " + repr(suma))

elif n1=="c":
  C=int(input("Ingrese el valor de consumo: "))
  I=int(input("Ingrese el valor de inversión: "))
  G=int(input("Ingrese el valor del gasto fiscal: "))
  X=int(input("Ingrese el valor de las exportaciones: "))
  Z=int(input("Ingrese el valor de las importanciones: "))
  t=suma=C+I+G+X 
  resta=t-Z
  print("El ingreso disponible en esta economía abierta sería "+ repr(resta))

elif n1=="b":
  salarie=int(input("Ingrese el valor de su salario base: "))
  a= salarie-salarie*0.08

  if salarie<=2000000:
    salario = a+117172
  else:
    salario= a
  print("Su salario devengado: ", salario)

else:
  print('Elija una opción válida')