try:
    # Condicao que gera a excecao
    a = 1/0
    # Condicao que NAO gera a excecao
    b = 2/1
except(Exception, ZeroDivisionError) as e:
    print(e)
else:
    print('No exception')
finally:
    print('Finaly')