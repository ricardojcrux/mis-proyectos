#Entorno de variables para guardad calc.py
#Uso de módulo creado por mi llamado calc.py

import sys

sys.path.append('/home/estudiante/Ricardo/Modulo')

import calc
suma= calc.sumar(8,9)
print('la suma de los dos numeros usando el modulo: ',suma)

import calc as clc
resta= clc.restar(8,9)
print('la resta de los dos numeros usando el modulo con un alias: ',resta)

print('suerte: ',clc.suerte)

