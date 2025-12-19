# Librerias usadas
import os
import random

WALL = "wall"
FLOOR = "floor"
PLAYER = "player"
EXIT = "exit"
KEY = "key"
DOOR = "door"

TILE_RENDER = {
    WALL : "█",   # pared
    FLOOR : " ",   # camino
    PLAYER : "H",   # jugador
    EXIT : "X",   # salida
    KEY : "K", # llave
    DOOR : "D", # puerta
}

def create_empty_maze(rows, cols):  # Función para crear un laberinto vacío
    maze = []
    for _ in range(rows):
        row = []
        for _ in range (cols):
            row.append({"type": WALL})
        maze.append(row)
    return maze

def generate_maze_dfs(maze, row, col):
    maze[row][col]["type"] = FLOOR
    directions = [(2, 0), (-2, 0), (0, 2), (0, -2)] # Movimientos posibles (abajo, arriba, derecha, izquierda)
    random.shuffle(directions) # Mezclar las direcciones para hacer el laberinto aleatorio

    for dr, dc in directions: ##########
        new_row = row + dr 
        new_col = col + dc

        if(
            1 <= new_row < len(maze) - 1 and # Asegurarse de que la nueva posición esté dentro de los límites del laberinto
            1 <= new_col < len(maze[0]) - 1 and 
            maze[new_row][new_col]["type"] == WALL
        ):
            maze[row + dr // 2][col + dc // 2]["type"] = FLOOR # Eliminar la pared entre las celdas
            maze[new_row][new_col]["type"] = FLOOR # Marcar la nueva celda como camino
            generate_maze_dfs(maze, new_row, new_col) # Llamada recursiva para continuar generando el laberinto

def draw_maze(maze): # Función para dibujar el laberinto
    for row in maze:
        rendered_row = ""
        for cell in row:
            cell_type = cell["type"]
            if cell_type not in TILE_RENDER:
                print("TIPO DESCONOCIDO:",repr(cell_type))
            rendered_row += TILE_RENDER.get(cell_type, "?")# Renderizar cada celda del laberinto
        print(rendered_row)

def move_player(maze, player_pos, new_row, new_col, inventory): # Función para mover al jugador
    row,col = player_pos
    target_type = maze[new_row][new_col]["type"]
    if target_type == KEY:                          ##### Que pasa si hay una llave en frente
        inventory["keys"] += 1
        maze[new_row][new_col]["type"] = FLOOR
    if target_type == DOOR:                         ##### QUe pasa si hay una puerta en frente
        if inventory["keys"] > 0:
            inventory["keys"] -= 1
            maze[new_row][new_col]["type"] = FLOOR
        else:
            return player_pos 
    if maze [new_row][new_col]["type"] in (FLOOR, EXIT):
        maze[row][col]["type"] = FLOOR # Limpiar la posición anterior del jugador
        maze[new_row][new_col]["type"] = PLAYER # Mover al jugador a la nueva posición
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

def place_key(maze):
    rows = len(maze)
    cols = len(maze[0])

    while True:
        r = random.randrange(1,rows -1)
        c = random.randrange(1,cols -1)

        if maze[r][c]["type"] == FLOOR:
            maze[r][c]["type"] = KEY
            return (r,c)
        
def place_door(maze, exit_pos):
    r, c = exit_pos
    door_pos = (r -1, c) # Hacer aleatoreo la distancia entre la puerta y la salida

    if maze[door_pos[0]][door_pos[1]]["type"] == FLOOR:
        maze[door_pos[0]][door_pos[1]]["type"] = DOOR
        return door_pos
    
    return None

def play_round(rows, cols):
    maze = create_empty_maze(rows,cols)
    inventory = {
        "keys": 0
    }

    # Marca la celda inicial como camino
    maze[1][1]["type"] = FLOOR
    generate_maze_dfs(maze, 1,1)

    exit_pos = (len(maze)-2, len(maze[0])-2)
   
    # Aquí se asegura que la salida esté en un camino
    while maze[exit_pos[0]][exit_pos[1]] == WALL:
        maze = create_empty_maze(rows,cols)
        maze[1][1]["type"] = FLOOR
        generate_maze_dfs(maze, 1,1)

    player_pos = (1,1) # Posición inicial del jugador
    maze[player_pos[0]][player_pos[1]]["type"] = PLAYER

    exit_pos = (len(maze)-2, len(maze[0])-2) # Posición de la salida
    maze[exit_pos[0]][exit_pos[1]]["type"] = EXIT

    key_pos = place_key(maze)
    door_pos = place_door(maze, exit_pos)

    while True:
        clear_console()
        draw_maze(maze)

        move = get_move()
        if move == "q":
            return False # Salir del juego

        new_row, new_col = calculate_new_position(player_pos, move) # Calcular la nueva posición del jugador
        player_pos = move_player(maze, player_pos, new_row, new_col, inventory) # Mover al jugador

        if player_pos == exit_pos:
            draw_maze(maze)
            print("¡Ronda Completada!")
            input("Presiona ENTER para continuar a la siguiente ronda...")
            return True # Ronda completada

#MAIN LOOP DEL JUEGO

round_number = 1  #Luego debo de anotar incrementos por ronda

rows = 11
cols = 25

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