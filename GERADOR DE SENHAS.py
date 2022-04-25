import random

print('Bem-vindo ao gerador de senhas!')

chars ='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#@&'

number = input('Quantitade de senhas para gerar: ')
number = int(number)


length = input('Insira o comprimento da sua senha: ')
length = int(length)

print('\nAqui está sua(s) senha(s):')


for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)
