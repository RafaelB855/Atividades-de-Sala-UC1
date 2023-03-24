'''''''''
Equipe 1:

Elabore o jogo pedra, papel e tesoura.


requisitos:
1 - criar menu inicial
2 - que seja um jogador contra a máquina
3 - os movimentos do oponente devem ser escolhidos aleatoriamnete(Dica: biblioteca random)
'''''''''

from random import randint
itens = ('Pedra', 'Papel','Tesoura')
computador = randint (0, 2)
print('''Suas opções:
[0] PEDRA
[1] PAPEL 
[2] TESOURA''')

jogador = int(input('Qual é sua jogada?'))
print('-='* 11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)

if computador == 0: # computador jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')

elif computador ==1:# computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
         print('JOGADOR VENCE')
    else:
         print('JOGADA INVÁLIDA!')
elif computador ==2:# computador jogou TESOURA
    if jogador == 0:
            print('JOGADOR VENCE')
    elif jogador == 1:
            print('COMPUTADOR VENCE')
    elif jogador == 2:
            print('EMPATE')
    else:
       print('JOGADA INVÁLIDA!')