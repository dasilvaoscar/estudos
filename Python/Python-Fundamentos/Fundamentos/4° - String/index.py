# O conteúdo da uma variável do tipo String, ou seja, a própria String é IMUTÁVEL

nome = 'Oscar da Silva'
numero = '1234567890'

print('Acesso ao terceiro item da string:' + nome[2]) # Acesso ao terceiro item da string ou seja 'c'.
print('Acessa um range de caracteres estabelecendo o seu FIM no 5° caractere: ' + nome[:4])
print('Acessa um range de caracteres estabelecendo o seu INÍCIO no 5° caractere: ' + nome[4:])
print('Acessa um range de caraceteres estabelecendo o seu INÍCIO e FIM: ' + nome[0:14])
print('Seleciona os caracteres pulando índices de 2 em 2: ' + numero[::2])
print('Seleciona os caracteres pulando índices de 2 em 2 apartir do 1: ' + numero[1::2])

# Utilizado o operador in para verificar se existe alguma letra na frase

print('Os' in nome)

print(len(nome)) # Verifica o tamanho da frase retornando um inteiro
print(nome.lower()) # Transforma todos os caracteres em minúsculos
print(nome.upper()) # Transforma todos os caracteres em maiúsculos
print(nome[0:5].upper() + nome[5:14].lower()) # Teste de concatenação com transformação de String 

frase = nome.upper()

print(frase.split()) # Quebra a frase por espaços, porém pode ser alterado o parâmetro através da função
print(frase.split('DA')) # Separa a Frase apartir de um parâmetro


