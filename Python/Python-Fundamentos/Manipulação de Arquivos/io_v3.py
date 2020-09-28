arquivo = open('Python\\Manipulação de Arquivos\\arquivos\\pessoas.csv', encoding='utf-8')
dados = arquivo.read()

try:
    for registro in dados.splitlines():
        frase = 'Nome: {}, Idade: {}'.format(*registro.split(',',))
        print(frase.replace(',', ' | '))
finally:
    print('Finaly')
    arquivo.close()
