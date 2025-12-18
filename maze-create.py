import os
import random

""" maze = [
    ["#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#"]
] """

def create_empty_maze(rows, cols):
    maze = []
    for _ in range(rows):
        maze.append(["#"] * cols)
    return maze


maze = create_empty_maze(11,21)

player_pos = (1,1)
exit_pos = (3,5)
maze[player_pos[0]][player_pos[1]] = "P"
maze[exit_pos[0]][exit_pos[1]] = "E"

def draw_maze(maze):
    for row in maze:
        print("".join(row))

def move_player(maze, player_pos, new_row, new_col):
    row,col = player_pos

    if maze [new_row][new_col] in (" ","E"):
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

    if player_pos == exit_pos:
        clear_console()
        draw_maze(maze)
        print("¡Felicidades! Has salido del laberinto.")
        break