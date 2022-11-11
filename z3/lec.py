# Создайте программу для игры в ""Крестики-нолики"".

import random

def printList(newList: list):
    for i in newList: print(i)

def returnPoz(number: int, newList: list, count: str) -> list:
    if number == 1: newList[0][0] = count
    elif number == 2: newList[0][1] = count
    elif number == 3: newList[0][2] = count
    elif number == 4: newList[1][0] = count
    elif number == 5: newList[1][1] = count
    elif number == 6: newList[1][2] = count
    elif number == 7: newList[2][0] = count
    elif number == 8: newList[2][1] = count
    elif number == 9: newList[2][2] = count
    return newList

def trueFalse(newList: list, count: str):
    checkInput = False
    for i in range(len(newList)):
        for j in range(len(newList)):
            if newList[i][j] == count:
                checkInput = True
                break
    return checkInput

def winGame(newList: list):
    if newList[0][0] == newList[1][1] == newList[2][2] != ' ': return True
    elif newList[0][2] == newList[1][1] == newList[2][0] != ' ': return True
    elif newList[0][0] == newList[0][1] == newList[0][2] != ' ': return True
    elif newList[1][0] == newList[1][1] == newList[1][2] != ' ': return True
    elif newList[2][0] == newList[2][1] == newList[2][2] != ' ': return True
    elif newList[0][0] == newList[1][0] == newList[2][0] != ' ': return True
    elif newList[0][1] == newList[1][1] == newList[2][1] != ' ': return True
    elif newList[0][2] == newList[1][2] == newList[2][2] != ' ': return True
    else: return False

newList = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
newList2 = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
print('Номера ячеек:')
printList(newList2)
print()
gamers = random.randint(1, 2)

if gamers == 1: print('Первый ход достаётся первому игроку!')
else: print('Первый ход достаётся второму игроку!')
print()
for i in range(len(newList)*2):
    if trueFalse(newList, ' '):
        if gamers == 1:
            printList(newList)
            number = int(input('Ходит первый игрок. Введите номер свободной ячейки: '))
            print()
            newList = returnPoz(number, newList, 'X')
            if winGame(newList) == True:
                printList(newList)
                print(f'Победил игрок №{gamers}!')
                break
            elif trueFalse(newList, ' '): gamers = 2
        if gamers == 2:
            printList(newList)
            number = int(input('Ходит второй игрок. Введите номер свободной ячейки: '))
            print()
            newList = returnPoz(number, newList, '0')
            if winGame(newList) == True:
                printList(newList)
                print(f'Победил игрок №{gamers}!')
                break
            elif trueFalse(newList, ' '): gamers = 1
    else: 
        printList(newList)
        print('Ничья!')
        