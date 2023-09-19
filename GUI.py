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

    def ai(self):
        self.service.generate_move()

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
                        self.ai()
                        move_ai = self.service.get_move()
                        print("move ai: ", move_ai)
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
