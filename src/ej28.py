#!encoding: UTF-8
#!/usr/bin/python

from math import sqrt
a = float(raw_input('Valor de a: '))
b = float(raw_input('Valor de b: '))
c = float(raw_input('Valor de c: '))

if a == 0 and b == 0 and c == 0:
  print 'La ecuacion tiene infinitas soluciones'
else:
  if a == 0 and b == 0:
    print 'La ecuacion no tiene solucion'
  else:
    if a == 0:
      x = -c / b
      print 'La solucion de la ecuacion es: x=%4.3f' % x
    elif (4*a*c > b**2):
print 'El discriminate es negativo'
    else:
      x1 = (-b + sqrt(b**2 - 4*a*c)) / (2 * a)
      x2 = (-b - sqrt(b**2 - 4*a*c)) / (2 * a)
      print 'Las soluciones de la ecuacion son: x1=%4.3f y x2=%4.3f' % (x1, x2)
#Para que funcione es que aparte de todas las condiciones de antes, debe cumplirse que b**2 > 4*a*c

