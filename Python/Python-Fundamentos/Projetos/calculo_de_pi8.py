from calculo_de_pi7 import calc_circulo as circulo
    
if __name__ == '__main__':
    raio_valor = float(input('Escreva o valor do raio: '))
    result = circulo(raio_valor)
    print(result)
else:
    print('Esse bloco não faz parte do __main__')





