def faixa_etaria(idade):
    if 0 <= idade < 18:
        return 'Menor de Idade'

    elif idade in range(18, 65):
        return 'Adulto'

    elif idade in range(66, 88):
        return 'Melhor Idade'

    elif idade in range(89, 100):
        return 'Já ta na fiapa'

    else:
        return 'Idade invalida'

if __name__ == '__main__':
    for idade in (1, 19, 71, 97):
        result = faixa_etaria(idade)
        print(f'Idade: {idade} Anos| {result}')