from math import sin, cos, tan , radians
ang = float(input('Digite um ângulo: '))
sen = sin(radians(ang))
cos = cos(radians(ang))
tang = tan(radians(ang))
print('O ângulo {}, tem valor {:.2f} no seno, {:.2f} no cosseno e {:.2f} na tangente'.format(ang, sen, cos, tang))
