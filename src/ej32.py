#!/usr/bin/python
#!encoding: UTF-8


a = ['pan','huevos', 100, 1234]
print a
 #Imprime ['pan','huevos',100, 1234]

print a[0]
 #Imprime el lugar 0 de la cadena, osea pan

print a[3]
 #Imprime el lugar 3 de la cadea, osea 1234

print a[-2]
 #Imprime el lugar -2 que es el 3, osea 100

print a[1:-1]
 #Imprime ['huevos', 100]

print a[:2] + ['carne',2*2]
 #Imprime ['pan', 'huevos', 'carne', 4]

print 3*a[:3] + ['Boo!']
 #Imprime ['pan', 'huevos', 100, 'pan', 'huevos', 100, 'pan', 'huevos', 100, 'Boo!']

print a
 #Imprime ['pan','huevos', 100, 1234]

a[2] = a[2] + 23

print a[2]
 #Imprime 123

 a[0:2] = [1,12]
print a[0:2]
 #Imprime [1, 12]

 print len(a)
 #Imprime 4

q = [2,3]
p = [1,q,4]

print len(p)
 #Imprime la longuitud de la cadena p, osea 3

print p[1]
 #Imprime [2, 3]

print p[1][0]
 #Imprime 2

p[1] .append('extra')

print p
 #Imprime [1, [2, 3, 'extra'], 4]

 print q
 #Imprime [2, 3]