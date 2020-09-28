# Dado um número aleatório de 1 a 6 
# Se for impar continue 
# Se for igual ao valor sorteado e par

from random import randint

number = randint(1 ,6)

for valor in range(1, 6):
    if valor % 2 == 1:
        continue
    elif valor % 2 == 0 and valor == number:
        print('ACERTOU ', number) 
        break
else:
    print('ERRO')
        

