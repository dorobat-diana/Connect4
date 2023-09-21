from board import *


class RepoException(Exception):
    def __init__(self, message):
        """
        initialize an error
        :param message: the massage that the error provides
        """
        self.__message = message

    @property
    def message(self):
        return self.__message


class RepoBoard():
    def __init__(self):
        """
        this is where we create a second empty board
        """
        self.copy_board = []
        for row in range(0, 6):
            a = []
            for column in range(0, 7):
                a.append(" ")
            self.copy_board.append(a)

    def ADD_move_yellow(self, column):
        """
        this is where the yellows move is added
        :param column: the column introduced by the human player
        :return:
        """
        obs = 0
        while obs == 0:
            for row in range(0, 6):
                if self.copy_board[int(row)][int(column)] == " ":
                    self.copy_board[int(row)][int(column)] = "Y"
                    obs = 1
                    break
    def ADD_move_red_column(self, column):
        """
        this is where the reds move is added
        :param column:
        :return:
        """
        obs= 0
        while obs == 0:
            for row in range(0, 6):
                if self.copy_board[int(row)][int(column)] == " ":
                    self.copy_board[int(row)][int(column)] = "R"
                    obs = 1
                    break
    def ADD_move_red(self, row, column):
        """
        this is were the computers move is added
        :param row: the row chosen by the computer
        :param column: the column chosen by the computer
        :return:
        """
        self.copy_board[row][column] = "R"

    def get_board(self):
        """
        this is were the board is transmitted for further verifications
        :return: returns the board
        """
        return self.copy_board
