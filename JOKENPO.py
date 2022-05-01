from random import randint
from time import sleep
from os import system

jogar = 'S'
jogador_vence = comp_vence = empate = 0

while jogar == 'S':
    pedra = ('Pedra')
    papel = ('Papel')
    tesoura = ('Tesoura')
    opcoes = (pedra, papel, tesoura)
    computador = randint(0, 2)
    print(('''------JOKENPÔ------
Escolha sua jogada:
[ 0 ] PEDRA 
[ 1 ] PAPEL 
[ 2 ] TESOURA '''))
    jogador = ''
    lista = [0, 1, 2]
    jogador = int(input('Sua jogada? '))
    while jogador not in lista:
        jogador = int(input('Digite um valor válido [0, 1 ou 2]. Qual é a sua jogada? '))
   
    system('clear')
    print(f'\nComputador jogou {opcoes[computador]}.')
    print(f'Jogador jogou {opcoes[jogador]}.\n')
    
    if computador == 0:
        if jogador == 0:
            empate += 1
        elif jogador == 1:
            jogador_vence += 1
        elif jogador == 2:
            comp_vence += 1

    elif computador == 1:
        if jogador == 0:
            comp_vence += 1
        elif jogador == 1:
            empate += 1
        elif jogador == 2:
            jogador_vence += 1

    elif computador == 2:
        if jogador == 0:
            jogador_vence += 1
        elif jogador == 1:
            comp_vence += 1
        elif jogador == 2:
            empate += 1

    print(f'''PONTUAÇÃO
Você: {jogador_vence}
Computador: {comp_vence}''')
    jogar = str(input('\nDeseja continuar a jogar? '
                      '[S/N] ')).upper().strip()[0]
    while jogar not in 'SN':
        jogar = str(input('Digite um dado válido. Deseja continuar a jogar? [S/N] ')).upper().strip()[0]

else:
    if jogador_vence > comp_vence:
        print(f'\nVocê venceu o computador por {jogador_vence} a {comp_vence}.')
    elif jogador_vence < comp_vence:
        print(f'\nO computador venceu você por {comp_vence} a {jogador_vence}.')
    elif jogador_vence == comp_vence:
        print(f'\nEmpate.')