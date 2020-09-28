#! python

from math import pi

try:
    raio = int(input('Escreva o valor do Raio: '))
    result = pi * raio ** 2

    print(result)
except Exception as e:
    print('Erro ', e)


