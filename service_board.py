from board import *
from repo_board import *


class ServiceException(Exception):
    def __init__(self, message):
        """
        initialize an error
        :param message: the massage that the error provides
        """
        self.__message = message

    @property
    def message(self):
        return self.__message


class ServiceBoard():
    def __init__(self, repo):
        """
        initialization
        :param repo: transfers the repository used
        """
        self.__repo = repo

    def add_move_yellow(self, column):
        """
        adds the move the opponent has chosen
        :param column: the column chosen by the opponent
        :return:
        """
        self.__repo.ADD_move_yellow(column)

    def add_move_red(self, row, column):
        """
        adds the computers move
        :param row:the row chosen
        :param column: the column chosen
        :return:
        """
        self.__repo.ADD_move_red(row, column)

    def display_board(self, board: Board):
        """
        returns the model of the boards display
        :param board: a copy of the board
        :return:
        """
        return "        0  1  2  3  4  5  6" + "\n" + "row_5 ||" + self.display_single_row(
            board[5]) + "\n" + "row_4 ||" + self.display_single_row(
            board[4]) + "\n" + "row_3 ||" + self.display_single_row(
            board[3]) + "\n" + "row_2 ||" + self.display_single_row(
            board[2]) + "\n" + "row_1 ||" + self.display_single_row(
            board[1]) + "\n" + "row_0 ||" + self.display_single_row(board[0]) + "\n"

    def return_board(self):
        """

        :return: returns the matrix that represents the board
        """
        return self.__repo.get_board()

    def display_single_row(self, list):
        """
        the model how to display a row
        :param list: the row to be displayed
        :return:
        """
        return str(list[0]) + "||" + str(list[1]) + "||" + str(list[2]) + "||" + str(list[3]) + "||" + str(
            list[4]) + "||" + str(list[5]) + "||" + str(list[6]) + "||"

    def verify_in_row_right(self, goal, color):
        """
        verifies from left to right if the opponent or the computer can win, the color is transmited and the goal of how many of the same color to be in the row
        :param goal: the number of how many of the same color in a row we are looking for
        :param color: the color we are looking for
        :return: true if it has found what we were looking for or false in the contrary
        """
        board = self.return_board()
        for row in range(0, 6):
            obs = 0
            poz = 0
            while poz < 7:
                if board[row][poz] == color:
                    obs += 1
                    if goal == 4 and obs == goal:
                        return True
                    elif goal == 3 and obs == 2 and poz + 2 < 7 and board[row][poz + 1] == " " and board[row][
                        poz + 2] == color:
                        self.add_move_red(row, poz + 1)
                        return True
                    elif obs == goal and poz < 6 and board[row][poz + 1] == " ":
                        if row - 1 >= 0 and board[row - 1][poz + 1] != " ":
                            self.add_move_red(row, poz + 1)
                            return True
                        elif row == 0:
                            self.add_move_red(row, poz + 1)
                            return True
                else:
                    obs = 0
                poz += 1
        return False

    def verify_in_row_left(self, goal, color):
        """
                verifies from right to left if the opponent or the computer can win, the color is transmited and the goal of how many of the same color to be in the row
                :param goal: the number of how many of the same color in a row we are looking for
                :param color: the color we are looking for
                :return: true if it has found what we were looking for or false in the contrary
                """
        board = self.return_board()
        for row in range(0, 6):
            obs = 0
            poz = 6
            while poz > 0:
                if board[row][poz] == color:
                    obs += 1
                    if goal == 4 and obs == goal:
                        return True
                    elif goal == 3 and obs == 2 and poz - 2 >= 0 and board[row][poz - 1] == " " and board[row][
                        poz - 2] == color:
                        self.add_move_red(row, poz - 1)
                        return True
                    elif obs == goal and poz > 0 and board[row][poz - 1] == " ":
                        if row - 1 >= 0 and board[row - 1][poz - 1] != " ":
                            self.add_move_red(row, poz - 1)
                            return True
                        elif row == 0:
                            self.add_move_red(row, poz - 1)
                            return True
                else:
                    obs = 0
                poz -= 1
        return False

    def verify_in_column(self, goal, color):
        """
        verifies if we have a number of the same color in a column
        :param goal: the number of the same color we are trying to find
        :param color: the color we are looking for
        :return:true if the goal was found or false otherwise
        """
        board = self.return_board()
        for column in range(0, 7):
            obs = 0
            poz = 0
            while poz < 6:
                if board[poz][column] == color:
                    obs += 1
                    if goal == 4 and obs == goal:
                        return True
                    elif obs == goal and poz < 5 and board[poz + 1][column] == " ":
                        if goal == 2 and column >= 3 and board[poz + 1][column - 1] == "Y":
                            if poz - 1 >= 0 and board[poz][column - 2] == "Y" and board[poz - 1][column - 3] == "Y":
                                return False
                        if goal == 2 and column <= 3 and board[poz + 1][column + 1] == "Y":
                            if poz - 1 >= 0 and board[poz][column + 2] == "Y" and board[poz - 1][column + 3] == "Y":
                                return False
                        self.add_move_red(poz + 1, column)
                        return True
                else:
                    obs = 0
                poz += 1
        return False

    def verify_in_diagonal_right_down(self, goal, color):
        """
        verifies if we have a number of the same color in diagonal from left to right starting from the left down side corner
        :param goal: the number of the same color we are trying to find
        :param color: the color we are looking for
        :return:true if the goal was found or false otherwise
        """
        board = self.return_board()
        for row in range(0, 4):
            for column in range(0, 4):
                obs = 0
                c = column
                r = row
                while row <= 5 and column <= 6 and board[row][column] == color:
                    obs += 1
                    if obs == 4:
                        return True
                    elif obs == goal and row + 1 <= 5 and column + 1 <= 6 and board[row + 1][column + 1] == ' ' and \
                            board[row][column + 1] != " ":
                        self.add_move_red(row + 1, column + 1)
                        return True
                    else:
                        row += 1
                        column += 1
                row = r
                column = c
        return False

    def verify_in_diagonal_right_up(self, goal, color):
        """
        verifies if we have a number of the same color in diagonal from left to right starting from the left up side corner
        :param goal: the number of the same color we are trying to find
        :param color: the color we are looking for
        :return:true if the goal was found or false otherwise
        """
        board = self.return_board()
        for row in range(5, 2, -1):
            for column in range(0, 4):
                obs = 0
                c = column
                r = row
                while row >= 0 and column <= 6 and board[row][column] == color:
                    obs += 1
                    if obs == 4:
                        return True
                    elif obs == goal and row - 1 >= 0 and column + 1 <= 6 and board[row - 1][column + 1] == ' ':
                        if row - 2 >= 0 and board[row - 2][column + 1] != " ":
                            self.add_move_red(row - 1, column + 1)
                            return True
                        elif row - 2 < 0:
                            self.add_move_red(row - 1, column + 1)
                            return True
                    else:
                        row -= 1
                        column += 1
                row = r
                column = c
        return False

    def verify_in_diagonal_left_up(self, goal, color):
        """
        verifies if we have a number of the same color in diagonal from right to left starting from the right up side corner
        :param goal: the number of the same color we are trying to find
        :param color: the color we are looking for
        :return:true if the goal was found or false otherwise
        """
        board = self.return_board()
        for row in range(5, 2, -1):
            for column in range(6, 2, -1):
                obs = 0
                c = column
                r = row
                while row >= 0 and column >= 0 and board[row][column] == color:
                    obs += 1
                    if obs == 4:
                        return True
                    elif obs == goal and row - 1 >= 0 and column - 1 >= 0 and board[row - 1][column - 1] == ' ':
                        if row - 2 >= 0 and board[row - 2][column - 1] != " ":
                            self.add_move_red(row - 1, column - 1)
                            return True
                        elif row - 2 < 0:
                            self.add_move_red(row - 1, column - 1)
                            return True
                    else:
                        row -= 1
                        column -= 1
                row = r
                column = c
        return False

    def verify_in_diagonal_left_down(self, goal, color):
        """
              verifies if we have a number of the same color in diagonal from right to left starting from the right down side corner
              :param goal: the number of the same color we are trying to find
              :param color: the color we are looking for
              :return:true if the goal was found or false otherwise
              """
        board = self.return_board()
        for row in range(2, -1, -1):
            for column in range(6, 2, -1):
                obs = 0
                c = column
                r = row
                while row <= 5 and column >= 0 and board[row][column] == color:
                    obs += 1
                    if obs == 4:
                        return True
                    elif obs == goal and row + 1 <= 5 and column - 1 >= 0 and board[row + 1][column - 1] == ' ' and \
                            board[row][column - 1] != " ":
                        self.add_move_red(row + 1, column - 1)
                        return True
                    else:
                        row += 1
                        column -= 1
                row = r
                column = c
        return False

    def generate_move(self):
        """
        this is where the computer generates its moves.It starts by looking for winning combinations of 3 for itself after
         for the opponent, then it first starts to look for blockings afterwards for winning combinations of 2,1 and 0
        :return:
        """
        goal = 3
        if self.verify_in_row_right(goal, 'R') == True:
            return
        elif self.verify_in_row_left(goal, 'R') == True:
            return
        elif self.verify_in_diagonal_right_down(goal, 'R') == True:
            return
        elif self.verify_in_diagonal_right_up(goal, 'R') == True:
            return
        elif self.verify_in_diagonal_left_down(goal, 'R') == True:
            return
        elif self.verify_in_diagonal_left_up(goal, 'R') == True:
            return
        elif self.verify_in_column(goal, 'R') == True:
            return
        elif self.verify_in_row_right(goal, "Y") == True:
            return
        elif self.verify_in_row_left(goal, "Y") == True:
            return
        elif self.verify_in_column(goal, 'Y') == True:
            return
        elif self.verify_in_diagonal_right_down(goal, 'Y') == True:
            return
        elif self.verify_in_diagonal_right_up(goal, 'Y') == True:
            return
        elif self.verify_in_diagonal_left_down(goal, 'Y') == True:
            return
        elif self.verify_in_diagonal_left_up(goal, 'Y') == True:
            return
        goal -= 1
        while goal != 0:
            if self.verify_in_row_right(goal, 'Y') == True:
                return
            elif self.verify_in_row_left(goal, 'Y') == True:
                return
            elif self.verify_in_diagonal_right_down(goal, 'Y') == True:
                return
            elif self.verify_in_diagonal_right_up(goal, 'Y') == True:
                return
            elif self.verify_in_diagonal_left_down(goal, 'Y') == True:
                return
            elif self.verify_in_diagonal_left_up(goal, 'Y') == True:
                return
            elif self.verify_in_column(goal, 'Y') == True:
                return
            elif self.verify_in_row_right(goal, "R") == True:
                return
            elif self.verify_in_row_left(goal, "R") == True:
                return
            elif self.verify_in_column(goal, 'R') == True:
                return
            elif self.verify_in_diagonal_right_down(goal, 'R') == True:
                return
            elif self.verify_in_diagonal_right_up(goal, 'R') == True:
                return
            elif self.verify_in_diagonal_left_down(goal, 'R') == True:
                return
            elif self.verify_in_diagonal_left_up(goal, 'R') == True:
                return
            goal -= 1

    def verify_win(self):
        """
        here we verify if yellow or red has a winning combination
        :return:
        """
        goal = 4
        if self.verify_in_row_right(goal, 'R') == True:
            return "Red wins"
        if self.verify_in_row_left(goal, 'R') == True:
            return "Red wins"
        elif self.verify_in_diagonal_right_down(goal, 'R') == True:
            return "Red wins"
        elif self.verify_in_diagonal_right_up(goal, 'R') == True:
            return "Red wins"
        elif self.verify_in_diagonal_left_down(goal, 'R') == True:
            return "Red wins"
        elif self.verify_in_diagonal_left_up(goal, 'R') == True:
            return "Red wins"
        elif self.verify_in_column(goal, 'R') == True:
            return "Red wins"
        elif self.verify_in_row_right(goal, "Y") == True:
            return "Yellow wins"
        elif self.verify_in_row_left(goal, "Y") == True:
            return "Yellow wins"
        elif self.verify_in_column(goal, 'Y') == True:
            return "Yellow wins"
        elif self.verify_in_diagonal_right_down(goal, 'Y') == True:
            return "Yellow wins"
        elif self.verify_in_diagonal_right_up(goal, 'Y') == True:
            return "Yellow wins"
        elif self.verify_in_diagonal_left_down(goal, 'Y') == True:
            return "Yellow wins"
        elif self.verify_in_diagonal_left_up(goal, 'Y') == True:
            return "Yellow wins"
        return "False"

    def Valid_input(self, column):
        """
        this is were we are looking for invalid input from the human opponent
        :param column: the column introduced by the human opponent
        :return: returns a messege in case of wrong input or true if the input is ok
        """
        try:
            column = int(column)
        except:
            return "column not int"
        if column < 0 or column > 6:
            return "the column doesn't exist"
        board = self.return_board()
        if board[5][column] != ' ':
            return "the column if full"
        return True
