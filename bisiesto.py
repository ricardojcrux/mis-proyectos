def bisiesto(bis):
    if bis%4 == 0:
        if bis%100 == 0:
            if bis%400 == 0:
                print('El año',bis,'es bisiesto')
            else:
                print('El año',bis,'no es bisiesto')
        else:
            print('El año',bis,'es bisiesto')
    else:
        print('El año',bis,'no es bisiesto')

bis = int(input('Ingrese un año bisiesto: '))
bisiesto(bis)