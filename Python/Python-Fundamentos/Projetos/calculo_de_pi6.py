pi = 3.14150
#__name__ = '__notmain__'

if __name__ == '__main__':
    raio = int(input('Escreva o valor do Raio: '))
    result = pi * raio ** 2

    print(result)
else:
    print('Esse bloco não faz parte do __main__')

