# Función para inicializar el tablero
def inicializar_tablero():
    return [[" " for _ in range(3)] for _ in range(3)]

# Función para imprimir el tablero
def imprimir_tablero(tablero):
    for fila in tablero:
        print(" | ".join(fila))
        print("-" * 9)

# Función para verificar si alguien ha ganado
def verificar_ganador(tablero, jugador):
    # Verificar filas, columnas y diagonales
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] == jugador:
            return True
        if tablero[0][i] == tablero[1][i] == tablero[2][i] == jugador:
            return True
    if tablero[0][0] == tablero[1][1] == tablero[2][2] == jugador:
        return True
    if tablero[0][2] == tablero[1][1] == tablero[2][0] == jugador:
        return True
    return False

# Función para jugar el juego
def jugar_tateti():
    tablero = inicializar_tablero()

    # Pedir a los jugadores que elijan su símbolo
    jugador_x = input("Jugador X, elige 'X' o 'O': ").upper()
    if jugador_x not in ["X", "O"]:
        print("Elección no válida. Jugador X jugará con 'X' por defecto.")
        jugador_x = "X"
    jugador_o = "O" if jugador_x == "X" else "X"

    jugador_actual = jugador_x
    juego_terminado = False

    while not juego_terminado:
        print("\nTurno del jugador", jugador_actual)
        imprimir_tablero(tablero)

        fila = int(input("Ingresa el número de fila (0, 1, 2): "))
        columna = int(input("Ingresa el número de columna (0, 1, 2): "))

        # Verificar si la casilla está disponible
        if tablero[fila][columna] == " ":
            tablero[fila][columna] = jugador_actual

            # Verificar si el jugador actual ha ganado
            if verificar_ganador(tablero, jugador_actual):
                imprimir_tablero(tablero)
                print("¡El jugador", jugador_actual, "ha ganado!")
                juego_terminado = True
            else:
                # Cambiar al siguiente jugador
                jugador_actual = jugador_x if jugador_actual == jugador_o else jugador_o
        else:
            print("Esa casilla ya está ocupada. Intenta de nuevo.")

    print("Fin del juego.")

# Iniciar el juego
if __name__ == "__main__":
    jugar_tateti()
