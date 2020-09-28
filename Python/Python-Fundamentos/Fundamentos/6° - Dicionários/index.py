# Forma de criação de um dicionário

pessoa = {'nome':'Oscar',
          'idade':18,
          'cursos':['TI', 'Música'],
          'filho':{
              'nome':'Irineu',
              'sobrenome':'Não Sabe Nem Eu',
              'neto':{
                  'nome':'João',
                  'sebrenome':'Na Tua Mão'
              }
          }}


# Funções
print(pessoa['idade']) # Mostra o valor pedido atribuído aquela chave
print(pessoa.keys()) # Mostra as chaves do dicionário
print(pessoa.items())# Mostra chaves e valores
print(pessoa.values()) # Mostra os Valores
print(pessoa.get('idade')) # Mostra o valor pedido atribuído aquela chave 
print(dir(pessoa['cursos']))
# Alteração de valores 

pessoa['idade'] = 19
pessoa['cursos'].append('Teologia') # append é utilizado pois o valor dessa chave corresponde a uma LISTA



# Chamada de um dicionário dentro do dicionário

print(pessoa['filho']['neto'].keys()) # Entro no dicionário do dicionário do dicionário para verificas as chaves
