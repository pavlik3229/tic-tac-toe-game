import random


def print_fied():
    for i in range(3):
        print(*field[i])
    print()


def is_win():
    flag = True
    for i in range(3):        #горизонтально
        el = field[i][0]
        flag = True
        for j in range(3):
            if field[i][j] != el or field[i][j] == "[ ]":
                flag = False
    if flag:
        return True
    flag = True

    flag = True
    for i in range(3):
        el = field[0][0]      #главная диагональ
        if field[i][i] != el or field[i][i] == "[ ]":
            flag = False
    if flag:
        return True

    flag = True
    el = field[0][2]
    for i in range(3):     #побочная диагональ
        if field[i][2 - i] != el or field[i][2 - i] == "[ ]":
            flag = False

    return flag


def winner():
    if is_win():
        if move == 1:

            print("Игрок 2 выйграл!")
            print_fied()
            return True
        else:
            print("Игрок 1 выйграл!")
            print_fied()
            return True
    return False


print("Игра 'Крестики нолики'")
print("Игрок 1 - x")
print("Игрок 2 - 0")
move = 1
player = random.randrange(1, 3)
print(f"Первый ход делает игрок под номером {player} \n")

field = [['[ ]' for j in range(3)] for i in range(3)]

while True:

    print_fied()
    if move == 1:
        print(f"Игрок {player} выбирает куда походить (x y):", end=" ")
        xy = [int(i) for i in input().split(" ")]
        x, y = xy[0], xy[1]
        field[x - 1][y - 1] = '[x]'
        move = 2
        player = 2
        if winner():
            break
        continue
    if move == 2:
        print(f"Игрок {player} выбирает куда походить (x y):", end=" ")
        xy = [int(i) for i in input().split(" ")]
        x, y = xy[0], xy[1]
        field[x - 1][y - 1] = '[0]'
        move = 1
        player = 1
        if winner():
            break
        continue
