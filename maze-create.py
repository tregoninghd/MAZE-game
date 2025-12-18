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

clear_console()
draw_maze(maze)
