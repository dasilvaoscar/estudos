local = 'Python\\Manipulação de Arquivos\\arquivos\\'

with open(f'{local}pessoas.csv', encoding='utf-8') as csv:
    arquivo = csv.read()

    with open(f'{local}pessoas.txt', mode='w', encoding='utf-8') as saida:

        for registro in arquivo.splitlines():
            frase = 'Nome: {}, Idade: {}'.format(*registro.split(',',))
            print(frase.replace(',', ' | '), file=saida)

if csv.closed:
    print('Arquivo Fechado !')


