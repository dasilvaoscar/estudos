# Estrutira que não aceita índice, repetição e a ordem não faz diferença

a = {1, 2, 3}

print(a)

# Funções
b = {4,5,6,1}
c = {10, 11, 12}

print(a.union(b)) # Faz a união de dois conjuntos
print(a.intersection(b)) # Mostra os elementos IGUAIS

a.update(c) # Insiro o conjunto c em a através de uma atualização
print(a)

a.add('z') # Adicionao um valor ao conjunto a
print(a)

# ------------------------------------------------------------------
teste1 = {1, 2, 3}
teste2 = {2, 3}

teste1.difference_update(teste2) # No grupo TESTE1 eu removo os elementos que também existem no grupo TESTE2
print(teste1)

a.discard(12) # Remove um elemento caso ele exista | cumpre a mesmo papel a.remove(11)



