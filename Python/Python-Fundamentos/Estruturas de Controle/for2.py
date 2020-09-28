# For percorrendo String 
palavra = 'Vai Corinthians'

for letra in palavra:
    print(letra, end='|')
    if letra == 's':
        print('\n')

# For para percorrer uma lista
aprovados = ['Oscar', 'Reginaldo', 'Kaká']

for nome in aprovados:
    print(nome, end='|')
    if nome == 'Kaká':
        print('\n')

# Percorrentdo uma tupla
modos = ('Jônio', 'Dórico', 'Frígio', 'Lídio', 'Mixolídio', 'Eólio', 'Lócrio')

for escala in modos:
    print(escala)