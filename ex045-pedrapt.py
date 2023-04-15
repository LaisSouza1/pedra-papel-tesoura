#Pedra, papel e tesoura
from random import choice
from time import sleep
print('\033[1;36m--*--' * 10)
print('\033[0;36mVamos jogar Pedra, Papel e Tesoura? ')
print('\033[1;36m--*--' * 10)
print('''Suas opções: 
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA''')
op1 = ('PEDRA')
op2 = ('PAPEL')
op3 = ('TESOURA')
pc = choice(['PEDRA', 'PAPEL', 'TESOURA'])
player = int(input('Qual sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(0.5)
print('PO!')
sleep(0.5)
print('--*--' * 10)
print('O Computador jogou {}'.format(pc))
if player == 1:
    print('Jogador jogou PEDRA')
elif player == 2:
    print('Jogador jogou PAPEL')
elif player == 3:
    print('Jogador jogou TESOURA')
print('--*--' * 10)

if (pc == 'PEDRA' and player == 3) or (pc == 'PAPEL' and player == 1) or (pc == 'TESOURA' and player == 2):
    print('COMPUTADOR VENCEU!')
elif (pc == 'PEDRA' and player == 2) or (pc == 'PAPEL' and player == 3) or (pc == 'TESOURA' and player == 1):
    print('JOGADOR VENCEU!')
else:
    print('EMPATE! Vamos jogar novamente?')
