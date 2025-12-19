import os
import random

TILE_RENDER = {
    "#": "█",   # pared
    " ": " ",   # camino
    "P": "H",   # jugador
    "E": "X"    # salida
    
}

quit

def draw_maze(maze): # Función para dibujar el laberinto
    for row in maze:
        rendered_row = ""
        for cell in row:
            rendered_row += TILE_RENDER.get(cell, "?")# Renderizar cada celda del laberinto
        print(rendered_row)


def create_empty_maze(rows, cols):  # Función para crear un laberinto vacío
    maze = []
    for _ in range(rows):
        maze.append(["#"] * cols)
    return maze

def generate_maze_dfs(maze, row, col):
    directions = [(2, 0), (-2, 0), (0, 2), (0, -2)] # Movimientos posibles (abajo, arriba, derecha, izquierda)
    random.shuffle(directions) # Mezclar las direcciones para hacer el laberinto aleatorio

    for dr, dc in directions: ##########
        new_row = row + dr 
        new_col = col + dc

        if(
            1 <= new_row < len(maze) - 1 and # Asegurarse de que la nueva posición esté dentro de los límites del laberinto
            1 <= new_col < len(maze[0]) - 1 and 
            maze[new_row][new_col] == "#"
        ):
            maze[row + dr // 2][col + dc // 2] = " " # Eliminar la pared entre las celdas
            maze[new_row][new_col] = " " # Marcar la nueva celda como camino
            generate_maze_dfs(maze, new_row, new_col) # Llamada recursiva para continuar generando el laberinto


def move_player(maze, player_pos, new_row, new_col): # Función para mover al jugador
    row,col = player_pos
    if maze [new_row][new_col] in (" ","E"):
        maze[row][col] = " " # Limpiar la posición anterior del jugador
        maze[new_row][new_col] = "P" # Mover al jugador a la nueva posición
        return (new_row, new_col)    
    return player_pos

def clear_console():
    os.system("cls")

def get_move(): # Función para obtener el movimiento del jugador
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

def play_round(rows, cols):
    maze = create_empty_maze(rows,cols)
    maze[1][1] = " "
    generate_maze_dfs(maze, 1,1)

    exit_pos = (len(maze)-2, len(maze[0])-2)
    while maze[exit_pos[0]][exit_pos[1]] == "#":
        maze = create_empty_maze(rows,cols)
        maze[1][1] = " "
        generate_maze_dfs(maze, 1,1)

    player_pos = (1,1) # Posición inicial del jugador
    maze[player_pos[0]][player_pos[1]] = "P"

    exit_pos = (len(maze)-2, len(maze[0])-2) # Posición de la salida
    maze[exit_pos[0]][exit_pos[1]] = "E"

    while True:
        clear_console()
        draw_maze(maze)

        move = get_move()
        if move == "q":
            return False # Salir del juego

        new_row, new_col = calculate_new_position(player_pos, move) # Calcular la nueva posición del jugador
        player_pos = move_player(maze, player_pos, new_row, new_col) # Mover al jugador

        if player_pos == exit_pos:
            draw_maze(maze)
            print("¡Ronda Completada!")
            input("Presiona ENTER para continuar a la siguiente ronda...")
            return True # Ronda completada

round_number = 1

rows = 11
cols = 21

while True:
    won = play_round(rows, cols)

    if not won:
        print("\nJuego terminado.")
        break

    round_number += 1
    rows += 2
    cols += 4
    print(f"\n¡Bienvenido a la ronda {round_number}!")
    input("Presiona ENTER para empezar la ronda...")