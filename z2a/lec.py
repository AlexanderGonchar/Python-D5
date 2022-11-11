# Программа для игры с конфетами человек против бота

import random

rules = ('На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. '
    'Первый ход определяется жеребьёвкой.'
    'За один ход можно забрать не более чем 28 конфет. '
    'Все конфеты оппонента достаются сделавшему последний ход. '
    'Сколько конфет нужно взять первому игроку, '
    'чтобы забрать все конфеты у своего конкурента?') 
            
print(rules)

player1 = input('\nИмя первого игрока: ')
bot_name = 'Bot_player '
print(f'\nВторой игрок: {bot_name}\n')
players = [player1, bot_name]

amount = 150
max_move = 28
print(f'Первому игроку нужно взять {amount%(max_move + 1)} конфет, чтобы выиграть \n')

def play_game(n, m, players):
    count = random.randint(0, 1)
    print(f'{count+1}!: первым берет конфеты {players[count]} \n')
    while n > 0:
        print(f'{players[count%2]}, возьмите конфеты')
        if players[count%2] != bot_name:
            move = int(input())
        else: 
            move = random.randint(1, m)
            print(f'Bot_player move = {move}')
        while move > n or move > m or move == 0:
            print(f'Нужно взять от одной до {m} конфет, сейчас у нас всего {n}')
            if players[count%2] != bot_name:
                move = int(input())
            else: 
                move = random.randint(1, n)
                print(f'Bot_player move = {move}')
        n = n - move
        if n > 0: print(f'Осталось конфет: {n}')
        else: print('Все конфеты разобраны.')
        count +=1
    return players[not count%2]

winer = play_game(amount, max_move, players)
if not winer:
    print('У нас нет победителя.')
else: print(f'Победитель {winer}!')
