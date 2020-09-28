with open('Python\\Manipulação de Arquivos\\arquivos\\pessoas.csv', encoding='utf-8') as csv:
    arquivo = csv.read()
    
    
    for registro in arquivo.splitlines():
        frase = 'Nome: {}, Idade: {}'.format(*registro.split(',',))
        print(frase.replace(',', ' | '))

    print('\n')
    print(arquivo)

if csv.closed:
    print('Arquivo Fechado !')