try:
    suma = lambda x,y : x + y
    assert suma(2,2) == 5
    print(8/0)
except:
    print('division por cero')
print('hola')