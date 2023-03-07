import numpy as np


class Board():
    def __init__(self):
        """
        this is where we generate an empty board
        """
        self.__board = []
        for row in range(0, 6):
            a = []
            for column in range(0, 7):
                a.append(" ")
            self.__board.append(a)

    @property
    def board(self):
        """
        :return: returns the board
        """
        return self.__board

    @board.setter
    def board(self, new_board):
        """
        sets the parameter board with a new board
        :param new_board: the new board we want to save
        :return:
        """
        self.__board = new_board
