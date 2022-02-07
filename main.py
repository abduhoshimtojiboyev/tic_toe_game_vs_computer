import random

column = " | "
row = "---------"
positions = {1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " ", 9: " "}
example = f" 1 | 2 | 3 \n{row}\n 4 | 5 | 6 \n{row}\n 7 | 8 | 9"
winning_positions = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 5, 9], [3, 5, 7], [1, 4, 7], [2, 5, 8], [3, 6, 9]]


def draw_field():
    field = ""
    for i in range(1, 10):
        piece = f"{positions[i]}"
        if i == 3 or i == 6:
            piece += f"\n{row}\n"
        elif i < 9:
            piece += column
        field += piece
    return print(field+'\n\n')


def check(index):
    if positions[index] != "0" and positions[index] != "x":
        return True


def check_winning(test):
    for winning in winning_positions:
        if set(winning).issubset(set(test)):
            return True


def move_player(sign):
    player_choice = int(input('Please choose the position in range 1-9 :  '))
    if check(player_choice):
        positions[player_choice] = sign
        draw_field()
        keys_player.append(player_choice)
        if check_winning(keys_player):
            print(f'Player win')
            score_player.append(1)
            keys_player.clear()

            keys_computer.clear()

    else:
        print('This place is marked')


def move_computer(sign):
    computer_winning_positions = winning_positions
    for winning_position in computer_winning_positions:
        delete = False
        for chunk in keys_player:
            if chunk in winning_position:
                delete = True
        if delete:
            computer_winning_positions.remove(winning_position)
    computer_choice_array = None
    if number_of_steps == 1 or computer_choice_array not in computer_winning_positions:
        computer_choice_array = random.choice(computer_winning_positions)
    # if computer_choice_array not in computer_winning_positions:
    #     computer_choice_array = random.choice(computer_winning_positions)
    computer_choice = random.choice(computer_choice_array)
    if sign == "x":
        computer_sign = "0"
    else:
        computer_sign = "x"
    positions[computer_choice] = computer_sign
    draw_field()
    keys_computer.append(computer_choice)
    if check_winning(keys_player):
        print(f'computer win')
        score_computer.append(1)
        keys_player.clear()
        keys_computer.clear()


keys_player = []
keys_computer = []
score_player = []
score_computer = []
keys = ['x', "0"]
random_choice = None
number_of_steps = 0

choice = input("Do you want begin randomly(you don't know what will you get) or choose x or 0 (x always begin "
               "first)  options(random/x/0): ").lower()

while True:
    number_of_steps += 1
    if choice == "x":
        move_player(choice)
        move_computer(choice)
    elif choice == "0":
        move_player(choice)
        move_computer(choice)
    else:
        if number_of_steps == 1:
            random_choice = random.choice(keys)

        if random_choice == "x":
            move_player(random_choice)
            move_computer(random_choice)
        else:
            move_player(random_choice)
            move_computer(random_choice)
