import os

maze = [
    ["#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#"]
]

def draw_maze(maze):
    for row in maze:
        print("".join(row))

def clear_console():
    os.system("cls")

clear_console()
draw_maze(maze)
