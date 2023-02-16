def primos(n): #n debe ser si o si mayor que 1 para que funcione la funcion
    primos = [2]
    i = 2
    while i < n:
        i += 1
        j = 0
        while j < len(primos):
            if i%primos[j]== 0:
                break
            j += 1
        else:
            primos.append(i)
    return 'Existen ' + str(len(primos)) + ' números primos hasta el ' + str(n)

def fibo(n): #n debe ser si o si mayor a 1 para que funcione la funcion
    fibo = [1,1]
    i = 1
    while fibo[i] < n:
        new = fibo[i]+fibo[i-1]
        fibo.append(new)
        i +=1
   
    try:
        a = str(n) + ' está en la posición ' + str(fibo.index(n)) + ' de la sucesion de Fibonacci'
        if n == 1:
            a='1 esta en la posicion 0 y 1 de la sucesión'  
    except:
        a = str(n) + ' no pertenece a la sucesion de Fibonacci'
    return a