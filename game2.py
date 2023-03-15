import arcade

# Tamaño de la ventana
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 300

# Tamaño de la cuadrícula
GRID_WIDTH = SCREEN_WIDTH // 3
GRID_HEIGHT = SCREEN_HEIGHT // 3

# Tamaño de los marcadores (círculos y cruces)
MARKER_RADIUS = GRID_WIDTH // 2 - 10

# Colores
BG_COLOR = arcade.color.WHITE
LINE_COLOR = arcade.color.BLACK
PLAYER1_COLOR = arcade.color.BLUE
PLAYER2_COLOR = arcade.color.RED

class TicTacToe(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(BG_COLOR)
        self.board = [[0 for _ in range(3)] for _ in range(3)]
        self.current_player = 1
        self.game_over = False

    def on_draw(self):
        arcade.start_render()
        self.draw_grid()
        self.draw_markers()

    def draw_grid(self):
        for i in range(1, 3):
            # Líneas verticales
            x = i * GRID_WIDTH
            arcade.draw_line(x, 0, x, SCREEN_HEIGHT, LINE_COLOR, 2)
            # Líneas horizontales
            y = i * GRID_HEIGHT
            arcade.draw_line(0, y, SCREEN_WIDTH, y, LINE_COLOR, 2)

    def draw_markers(self):
        for i in range(3):
            for j in range(3):
                x = j * GRID_WIDTH + GRID_WIDTH // 2
                y = i * GRID_HEIGHT + GRID_HEIGHT // 2
                if self.board[i][j] == 1:
                    arcade.draw_circle_filled(x, y, MARKER_RADIUS, PLAYER1_COLOR)
                elif self.board[i][j] == 2:
                    arcade.draw_line(x - MARKER_RADIUS, y - MARKER_RADIUS,
                                     x + MARKER_RADIUS, y + MARKER_RADIUS,
                                     PLAYER2_COLOR, 2)
                    arcade.draw_line(x + MARKER_RADIUS, y - MARKER_RADIUS,
                                     x - MARKER_RADIUS, y + MARKER_RADIUS,
                                     PLAYER2_COLOR, 2)

    def on_mouse_press(self, x, y, button, modifiers):
        if not self.game_over:
            i = y // GRID_HEIGHT
            j = x // GRID_WIDTH
            if self.board[i][j] == 0:
                self.board[i][j] = self.current_player
                if self.check_win():
                    self.game_over = True
                else:
                    self.current_player = 3 - self.current_player

import arcade

# Tamaño de la ventana
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 300

# Tamaño de la cuadrícula
GRID_WIDTH = SCREEN_WIDTH // 3
GRID_HEIGHT = SCREEN_HEIGHT // 3

# Tamaño de los marcadores (círculos y cruces)
MARKER_RADIUS = GRID_WIDTH // 2 - 10

# Colores
BG_COLOR = arcade.color.WHITE
LINE_COLOR = arcade.color.BLACK
PLAYER1_COLOR = arcade.color.BLUE
PLAYER2_COLOR = arcade.color.RED

class TicTacToe(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(BG_COLOR)
        self.board = [[0 for _ in range(3)] for _ in range(3)]
        self.current_player = 1
        self.game_over = False

    def on_draw(self):
        arcade.start_render()
        self.draw_grid()
        self.draw_markers()

    def draw_grid(self):
        for i in range(1, 3):
            # Líneas verticales
            x = i * GRID_WIDTH
            arcade.draw_line(x, 0, x, SCREEN_HEIGHT, LINE_COLOR, 2)
            # Líneas horizontales
            y = i * GRID_HEIGHT
            arcade.draw_line(0, y, SCREEN_WIDTH, y, LINE_COLOR, 2)

    def draw_markers(self):
        for i in range(3):
            for j in range(3):
                x = j * GRID_WIDTH + GRID_WIDTH // 2
                y = i * GRID_HEIGHT + GRID_HEIGHT // 2
                if self.board[i][j] == 1:
                    arcade.draw_circle_filled(x, y, MARKER_RADIUS, PLAYER1_COLOR)
                elif self.board[i][j] == 2:
                    arcade.draw_line(x - MARKER_RADIUS, y - MARKER_RADIUS,
                                     x + MARKER_RADIUS, y + MARKER_RADIUS,
                                     PLAYER2_COLOR, 2)
                    arcade.draw_line(x + MARKER_RADIUS, y - MARKER_RADIUS,
                                     x - MARKER_RADIUS, y + MARKER_RADIUS,
                                     PLAYER2_COLOR, 2)

    def on_mouse_press(self, x, y, button, modifiers):
        if not self.game_over:
            i = y // GRID_HEIGHT
            j = x // GRID_WIDTH
            if self.board[i][j] == 0:
                self.board[i][j] = self.current_player
                if self.check_win():
                    print("gano cv")
                    self.game_over = True
                else:
                    self.current_player = 3 - self.current_player

    def check_win(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != 0:
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != 0:
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != 0:
            return
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != 0:
         return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != 0:
         return True
     
