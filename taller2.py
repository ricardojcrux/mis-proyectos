a=int(input('Escriba un número '))
liste=list(range(2,a))
for x in liste:
  if a%x == 0:
    print('El número no es primo')
    break
  elif a==x+1:
    print('El número es primo')
    break





































