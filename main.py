from random import randint
import sys

player_1_choice = 'x'
player_2_choice = 'o'
game_draw = "DRAW"

grid = [cell for cell in range(1,10)]
def display_board():
    print(f"{grid[0]}  {grid[1]}  {grid[2]}")
    print(f"{grid[3]}  {grid[4]}  {grid[5]}")
    print(f"{grid[6]}  {grid[7]}  {grid[8]}")

def check_for_win_draw():
    if grid[0] == grid[1] ==grid[2]:
        return grid[0]
    elif grid[3] == grid[4]==grid[5]:
        return grid[3]
    elif grid[6] == grid[7]==grid[8]:
        return grid[6]
    elif grid[0] == grid[3]==grid[6]:
        return grid[0]
    elif grid[1] == grid[4] == grid[7]:
        return grid[1]
    elif grid[2] == grid[5]==grid[8]:
        return grid[2]
    elif grid[0] == grid[4]==grid[8]:
        return grid[0]
    elif grid[2] == grid[4]==grid[6]:
        return grid[2]
    else:
        for row in grid:
            if isinstance(row,int):
                return
        return game_draw

def game():
    winner = check_for_win_draw()
    if winner == 'x':
        display_board()
        sys.exit()
        print("Player[x] have won.")
    elif winner == 'o':
        print("Player [o] have won.")
        display_board()
        sys.exit()
    elif winner == game_draw:
        print("Is TIE")
        display_board()
        sys.exit()

def update_grid(choice,location):
    if location < 0 or location > 9:
        raise ValueError("The location is not valid")
    if grid[location] == 'x' or grid[location] == 'o':
        raise ValueError(grid[location],"is not a valid location.")
    else:
        grid[location] = choice

def main():
    player_1_location = int(input("Player[x], please enter your choice (0-8) "))
    update_grid(player_1_choice, player_1_location)
    game()
    display_board()

    player_2_location = int(input("Player[o] please enter your choice (0-8)"))
    update_grid(player_2_choice, player_2_location)
    game()
    display_board()

while True:
    main()