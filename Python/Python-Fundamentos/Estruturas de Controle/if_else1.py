def convert(nota):

    if nota == 10 or nota >= 9.1:
        return 'Nota A'

    elif nota >= 8.1:
        return 'Nota A-'

    elif nota >= 7.1:
        return 'Nota B'

    elif nota >= 6.1:
        return 'Nota B-'

    elif nota >= 5.1:
        return 'Nota C'

    elif nota >= 4.1:
        return 'Nota C-'

    elif nota >= 3.1:
        return 'Nota D'

    elif nota >= 2.1:
        return 'Nota D-'

    elif nota >= 1.1:
        return 'Nota E'

    elif nota >= 0:
        return 'Nota E-'

    else:
        return 'Essa função não permite números menores que 0 ou maiores que 10'


print(convert(9))
