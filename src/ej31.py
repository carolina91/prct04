#!/usr/bin/python
#!encoding: UTF-8

numero = int( raw_input('Introduzca un numero: '))

for potencia in [2,3,4,5]:
  print '%d elevado a %d es %d' % (numero, potencia, numero**potencia)
  
#Primero nos pide un número. Lo siguiente que hace con el comando "for potencia in [2,3,4,5] " es hacerle al numero introducido su potencia  al cuadrado, al cubo, a la cuarta y a la quinta. 