from board import *
from service_board import *
from repo_board import *
import random


class UserInterfaceException(Exception):

    def __init__(self, message):
        self.__message = message

    @property
    def message(self):
        return self.__message


class UserInterface():
    def __init__(self, service):
        self.service = service

    def print_board(self):
        b = self.service.return_board()
        print(self.service.display_board(b))

    def adversare(self):
        self.print_board()
        valid = False
        while valid != True:
            print("please make your move")
            column = input("column>>>")
            valid = self.service.Valid_input(column)
            if valid != True:
                print(valid)

        self.service.add_move_yellow(column)
        self.print_board()

    def ai(self):
        self.service.generate_move()

    def menu(self):
        move = 0
        while move < 42:
            self.adversare()
            move += 1
            self.ai()
            move += 1
            final = self.service.verify_win()
            if final != "False":
                self.print_board()
                print(final)
                break
        if move == 42:
            print("Game Over")
