import os

maze = [
    ["#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#"]
]

player_pos = (1,1)
maze[player_pos[0]][player_pos[1]] = "P"

def draw_maze(maze):
    for row in maze:
        print("".join(row))


def move_player(maze, player_pos, new_row, new_col):
    row,col = player_pos

    if maze [new_row][new_col] != "#":
        maze[row][col] = " "
        maze[new_row][new_col] = "P"
        return (new_row, new_col)
    
    return player_pos

def clear_console():
    os.system("cls")

def get_move():
    move = input("Mover (W/A/S/D, Q para salir): ").lower()
    return move 

def calculate_new_position(player_pos, move):
    row, col = player_pos
    if move == "w":
        return row - 1, col
    elif move == "s":
        return row + 1, col
    elif move == "a":
        return row, col - 1
    elif move == "d":
        return row, col + 1
    return row,col

while True:
    clear_console()
    draw_maze(maze)

    move = get_move()

    if move == "q":
        break

    new_row, new_col = calculate_new_position(player_pos, move)
    player_pos = move_player(maze, player_pos, new_row, new_col)