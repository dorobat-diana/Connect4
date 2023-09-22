# in this file I added a gui to the original console based game and I also added a better alternative for the computer player based on the minimax algorithm with alpha beta pruning
import copy
import math
from ui import *
import pygame as pygame
from service_board import *
import sys

BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
RADIUS = int(100 / 2 - 5)


class GUI():
    def __init__(self, service):
        self.service = service
        self.ui = UserInterface(self.service)
        self.AI = GUI_AI(self.service)
        pygame.init()
        SQUARESIZE = 100
        width = 7 * SQUARESIZE
        height = (6 + 1) * SQUARESIZE
        size = (width, height)
        self.screen = pygame.display.set_mode(size)
        self.draw_board()
        pygame.display.update()

    def draw_board(self):
        board = self.service.return_board()
        for c in range(7):
            for r in range(6):
                pygame.draw.rect(self.screen, BLUE, (c * 100, (r + 1) * 100, 100, 100))
                if board[5 - r][c] == ' ':
                    pygame.draw.circle(self.screen, BLACK, (int(c * 100 + 50), int((1 + r) * 100 + 50)), RADIUS)
                elif board[5 - r][c] == 'R':
                    pygame.draw.circle(self.screen, RED, (int(c * 100 + 50), int((1 + r) * 100 + 50)), RADIUS)
                elif board[5 - r][c] == 'Y':
                    pygame.draw.circle(self.screen, YELLOW, (int(c * 100 + 50), int((1 + r) * 100 + 50)), RADIUS)
    def menu(self):
        move = 0
        move_ai = (0, 0)
        while move < 42:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    posx = event.pos[0]
                    pygame.draw.rect(self.screen, BLACK, (0, 0, 700, 100))
                    col = int(math.floor(posx / 100))
                    if self.service.Valid_input(col) == True:
                        self.service.add_move_yellow(col)
                        self.draw_board()
                        pygame.display.update()
                        self.ui.print_board()
                        move += 1
                        # pygame.time.wait(500)
                        self.AI.ai()
                        # move_ai = self.service.get_move()
                        # print("move ai: ", move_ai)
                        move += 1
                        self.draw_board()
                        pygame.display.update()
                        self.ui.print_board()
                        final = self.service.verify_win()
                        if final != "False":
                            print(final)
                            myfont = pygame.font.SysFont("monospace", 75)
                            label = myfont.render(final, 1, RED)
                            self.screen.blit(label, (40, 10))
                            pygame.display.update()
                            pygame.time.wait(3000)
                            sys.exit()
                    posx = event.pos[0]
                    pygame.draw.rect(self.screen, BLACK, (0, 0, 700, 100))
                    pygame.draw.circle(self.screen, YELLOW, (posx, 50), RADIUS)
                    pygame.display.update()
                elif event.type == pygame.MOUSEMOTION:
                    posx = event.pos[0]
                    pygame.draw.rect(self.screen, BLACK, (0, 0, 700, 100))
                    pygame.draw.circle(self.screen, YELLOW, (posx, 50), RADIUS)
                    pygame.display.update()
        if move == 42:
            print("Game Over")
            myfont = pygame.font.SysFont("monospace", 75)
            label = myfont.render("Game Over", 1, RED)
            self.screen.blit(label, (40, 10))
            pygame.display.update()
            pygame.time.wait(3000)
            sys.exit()


class GUI_AI():
    def __init__(self, service):
        self.service = service
    def ai(self):
        # self.service.generate_move()

        # col = self.pick_best_move()

        col, score = self.minimax(self.service.return_board(), 4, -math.inf, math.inf, True)
        print(score)
        if self.service.verify_win() == 'False':
            self.service.add_move_red_column(col)

    def get_column(self, board, col):
        array_column = []
        for r in range(6):
            array_column.append(board[r][col])
        return array_column

    def score_position(self, board):
        score = 0
        # score center
        center_array = self.get_column(board, 3)
        center_count = center_array.count('R')
        score += center_count * 3
        ## score horizontal
        for r in range(6):
            row_array = board[r]
            for c in range(4):
                window = row_array[c:c + 4]
                score += self.evaluet_window(window)
        ## score vertical
        for c in range(7):
            col_array = self.get_column(board, c)
            for r in range(3):
                window = col_array[r:r + 4]
                score += self.evaluet_window(window)
        ## score positive sloped diagonal
        for c in range(4):
            for r in range(3):
                window = [board[r + i][c + i] for i in range(4)]
                score += self.evaluet_window(window)
        ## score negative sloped diagonal
        for r in range(3):
            for c in range(3, 7):
                window = [board[r + i][c - i] for i in range(4)]
                score += self.evaluet_window(window)
        return score

    def evaluet_window(self, window):
        score = 0
        if window.count('R') == 4:
            score += 1000
        if window.count('Y') == 4:
            score -= 1000
        if window.count('R') == 3 and window.count(' ') == 1:
            score += 100
        if window.count('Y') == 3 and window.count(' ') == 1:
            score -= 50
        if window.count('R') == 2 and window.count(' ') == 2:
            score += 10
        return score

    def get_valid_locations(self):
        valid_locations = []
        board = self.service.return_board()
        for col in range(7):
            if self.service.Valid_input(col):
                valid_locations.append(col)
        return valid_locations

    def get_next_open_row(self, col, board):

        for r in range(6):
            if board[r][col] == ' ':
                return r

    def pick_best_move(self):
        valid_locations = self.get_valid_locations()
        best_score = -10000
        board = self.service.return_board()
        for col in range(7):
            if self.service.Valid_input(col) == True:
                row = self.get_next_open_row(col, board)
                temp_board = copy.deepcopy(board)
                temp_board[row][col] = 'R'
                score = self.score_position(temp_board)
                if score > best_score:
                    best_score = score
                    best_col = col
        return best_col

    def minimax(self, board, depth, alpha, beta, maximizingPlayer):
        valid_locations = self.get_valid_locations()
        if self.service.verify_win() != "False" or len(valid_locations) == 0 or depth == 0:
            if self.service.verify_win() == "Red wins":
                return None, 100000000000000
            elif self.service.verify_win() == "Yellow wins":
                return None, -10000000000000
            elif depth == 0:
                return None, self.score_position(board)
            else:  # game is over
                return None, 0
        elif maximizingPlayer:
            value = -math.inf
            column = random.choice(valid_locations)
            for col in range(7):
                if self.Valid_input_copy(board, col) == True:
                    row = self.get_next_open_row(col, board)
                    temp_board = copy.deepcopy(board)
                    temp_board[row][col] = 'R'
                    new_score = self.minimax(temp_board, depth - 1, alpha, beta, False)[1]
                    if new_score > value:
                        value = new_score
                        column = col
                    alpha= max(alpha, value)
                    if alpha >= beta:
                        break
            return column, value
        else:  # minimizing player
            value = math.inf
            column = random.choice(valid_locations)
            for col in range(7):
                if self.Valid_input_copy(board, col) == True:
                    row = self.get_next_open_row(col, board)
                    temp_board = copy.deepcopy(board)
                    temp_board[row][col] = 'Y'
                    new_score = self.minimax(temp_board, depth - 1, alpha, beta, True)[1]
                    if new_score < value:
                        value = new_score
                        column = col
                    beta = min(beta, value)
                    if alpha >= beta:
                        break
            return column, value


    def Valid_input_copy(self, board, column):
        """
        this is where we are looking for invalid input from the human opponent
        :param column: the column introduced by the human opponent
        :return: returns a messege in case of wrong input or true if the input is ok
        """
        try:
            column = int(column)
        except:
            return "column not int"
        if column < 0 or column > 6:
            return "the column doesn't exist"
        if board[5][column] != ' ':
            return "the column if full"
        return True
