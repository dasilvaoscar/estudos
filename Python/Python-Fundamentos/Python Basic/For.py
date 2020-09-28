# Loop for para imprimir listas simples
b = ('A', 'B', 'C')

for i in b:
    print(i)
    if i == 'B':
        print('TESTE')
    else:
        pass
else:
    print('FIM')

# Loop for para imprimir duas listas
lista1 = ['Oscar', 'Oscar1', 'Oscar2']
lista2 = ['Osca3', 'Oscar4', 'Oscar5']

for i,j in zip(lista1, lista2):

    print(i, j)

# Loop for para mostrar indice
for i,j in enumerate(lista1):

    print(i)