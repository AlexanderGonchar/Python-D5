# Программа для игры с конфетами человек против бота с ''интеллектом''

from random import randint

print('Правила игры:' 
      'На столе лежит 2021 конфета.'
      'Играют два игрока делая ход друг после друга.' 
      'Первый ход определяется жеребьёвкой.' 
      'За один ход можно забрать не более чем 28 конфет.'
      'Все конфеты оппонента достаются сделавшему последний ход. ')

def player_vs_bot():
    candies_total = 2021
    max_take = 28
    player_1 = input('\nВведите своё имя: ')
    player_2 = 'Бот'
    players = [player_1, player_2]
    print('\nДля начала опеределим кто первый начнет игру.\n')

    lucky = randint(-1, 0)

    print(f'Поздравляю {players[lucky+1]} Вы ходите первым !')

    while candies_total > 0:
        lucky += 1

        if players[lucky % 2] == 'Бот':
            print(
                f'\nХодит {players[lucky%2]} \nНа кону {candies_total}.')

            if candies_total < 29:
                step = candies_total
            else:
                delenie = candies_total//28
                step = candies_total - ((delenie*max_take)+1)
                if step == -1:
                    step = max_take -1
                if step == 0:
                    step = max_take
            while step > 28 or step < 1:
                step = randint(1,28)
            print(step)
        else:
            step = int(input(f'\nВаш ход,  {players[lucky%2]} \nНа кону {candies_total} : '))
            while step > max_take or step > candies_total:
             step = int(input(f'\nЗа один ход можно взять {max_take} конфет, попробуй еще раз: '))
        candies_total = candies_total - step

    print(f'На кону осталось {candies_total} \nПобедил {players[lucky%2]}')

player_vs_bot()