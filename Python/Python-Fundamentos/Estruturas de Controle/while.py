# Função para tentar descobrir qual número o sistema gerou

from random import randint # Função que gera número inteiro aleatório
import os

def aleatorio():

    numero_informado = -1
    numero_secreto = randint(0 ,9)
    tentativas = 0

    while numero_informado != numero_secreto:
        numero_informado = int(input('Escreva um número: '))
        if numero_informado != numero_secreto:
            print('ERROOOOO!!!')
            tentativas += 1

        elif tentativas == 0:
            os.system('clear') # Limpa o console
            print('POOOHAAA, tu é o bichão hein acertou na 1° tentativa')

        else:
            os.system('clear')
            print(f'Finalmente, o número era o {numero_secreto}, foi acertar só na {tentativas}° tentativa')

aleatorio()