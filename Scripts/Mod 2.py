from math import hypot
co = float(input('Qual o valor do cateto oposto? '))
ca = float(input('Qual o valor do cateto adjacente? '))
hy = hypot(co, ca)
print('O triângulo com cateto oposto {} e adjacente {}, tem hipotenusa {:.2f}.'.format(co, ca, hy))
