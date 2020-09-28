# Percorrendo um dicionário

produto = {
    'nome': 'Caneta Azul',
    'preço': 19.44,
    'importada': True,
    'estoque': 144
}

for chave in produto:
    print(chave)

for valor in produto.values():
    print(valor)

for chave, valor in produto.items():
    print(f'{chave} = {valor}')