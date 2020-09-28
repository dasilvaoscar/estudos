lista = [3]

lista.append(1) # Append permite adicionar um valor em uma lista existente
lista.append(2)
print('Lista Original:', lista)

list_copy = lista.copy() # Cria uma cópia separada da Lista
print('Cópia da lista original: ', list_copy)

lista.remove(3) # Remove o valor pelo conteúdo e não pelo índice
print('Romevendo um dos valores: ', lista)

lista.clear() # Limpa a lista por completo
print('Lista Limpa ',lista)

# Para adicionar um valor já existente **************************
lista.extend(list_copy)



