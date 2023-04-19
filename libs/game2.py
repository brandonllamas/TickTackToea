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
        self.ganador = ""
        self.compMove()

    def on_draw(self):
        arcade.start_render()
        self.draw_grid()
        self.draw_markers()

    def check_winBot(self,mark):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] == mark:
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i]  == mark:
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2]  == mark:
            return
        if self.board[0][0] == self.board[1][1] == self.board[2][2]  == mark:
         return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0]  == mark:
         return True
     
    def checkDraw(self,board):
        i = 0
        for wi in board:
            j=0
            for wj in wi:
                if(board[i][j] == 0):
                    return False
            j+=1
        i+=i
        return True


    def minimax(self,board,depth, isMaximing):
        # verifica que si el movimiento hay un ganador 2
        if self.check_winBot(1):
            return 1
        # verifica que si el movimiento hay un ganador 1
        elif  self.check_winBot(2):
            return -1
        
        # verifica que si el movimiento hay un ganador 
        elif self.checkDraw(board):
            print("no mani")
            return 0
        
        if isMaximing:
           bestScore = -800
           i = 0
           for key in board:
               j=0
               for item in key:
                   if  board[i][j] == 0:
                       print("position {}:{} = 0".format(i,j))
        # coloca paso
                       board[i][j] = 1
                       source = self.minimax(board,depth + 1,False)
                       board[i][j] = 0
                       if(source > bestScore):
                           bestScore = source
                   j+=1
               i+=i
           return bestScore
        else:
           bestScore =  800
           i = 0
           for key in board:
               j=0
               for item in key:
                   if  board[i][j] == 0:
                       print("position {}:{} = 0".format(i,j))
        # coloca paso
                       board[i][j] = 1
                       print("boardpcc")
                       print(board)
                       source = self.minimax(board,depth + 1,True)
                       board[i][j] = 0
                       if(source > bestScore):
                           bestScore = source
                   j+=1
               i+=i
           return bestScore
    
    def compMove(self):
        bestScore = -800
        bestMoveI = 0
        bestMoveJ = 0
        i = 0
        for key in self.board:
            j=0
            for item in key:
                if self.board[i][j] == 0:
                    self.board[i][j] = 1
                    source = self.minimax(self.board,0,False)
                    print("position {}:{} = 0 and source is = {}".format(i,j,source))
                    self.board[i][j] = 0
                    if(source > bestScore):
                        bestScore = source
                        bestMoveI = i
                        bestMoveJ = j
                j+=1
            i+=i
        print("el pc dice que 💻")
        print("El mejor movimiento es = [{}][{}]".format(bestMoveI,bestMoveJ))
        self.board[bestMoveI][bestMoveJ] = self.current_player
        


    
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
                print("===========")
                for item in self.board:
                    print(item)
                if self.check_win():
                    print("gano cv")
                    print(self.current_player)
                    self.ganador= self.current_player
                    self.game_over = True
                    # arcade.finish_render()
                else:
                    self.current_player = 3 - self.current_player
                    self.compMove()

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
     
