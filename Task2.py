lst = [i for i in range(1, 10)]
victory =   [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]

def print_lst(lst):
    print('-' * 13)
    for i in range(3):
        print('>', lst[0 + i * 3],'|', lst[1 + i * 3], '|', lst[2 + i * 3], '<')
        print('-' * 13)

def moving(step, symbol):
    ind = lst.index(step)
    lst[ind] = symbol

def get_result(name_player1, name_player2):
    win = ""
    for i in victory:
        if lst[i[0]] == "X" and lst[i[1]] == "X" and lst[i[2]] == "X":
            win = name_player1
        if lst[i[0]] == "O" and lst[i[1]] == "O" and lst[i[2]] == "O":
            win = name_player2       
    return win

name_player1 = input("Игрок №1. Назови свое имя: ")
name_player2 = input("Игрок №2. Назови свое имя: ")
game_over = False
player1 = True
while game_over == False:
    print_lst(lst)
    if player1 == True:
        symbol = "X"
        step = int(input(f"{name_player1} твой ход: "))
    else:
        symbol = "O"
        step = int(input(f"{name_player2} твой ход: "))
    moving(step,symbol)
    win = get_result(name_player1, name_player2)
    if win != "":
        game_over = True
    else:
        game_over = False
    player1 = not(player1)             
print_lst(lst)
print("Победил", win)