from unittest import TestCase
import unittest
from repo_board import *
from service_board import *
from board import *


class Test_service(TestCase):
    def setUp(self):
        self.service = ServiceBoard(RepoBoard())
        self.board = []
        for row in range(0, 6):
            a = []
            for column in range(0, 7):
                a.append(" ")
            self.board.append(a)

    def test_add_move_yellow(self):
        self.service.add_move_yellow(0)
        self.board = self.service.return_board()
        self.assertEqual(self.board[0][0], 'Y')

    def test_add_move_red(self):
        self.service.add_move_red(0, 0)
        self.board = self.service.return_board()
        self.assertEqual(self.board[0][0], 'R')

    def test_verify_in_raw_right(self):
        self.service.add_move_yellow(0)
        self.service.add_move_yellow(1)
        self.service.add_move_yellow(2)
        self.assertEqual(self.service.verify_in_row_right(3, 'Y'), True)

    def test_verify_in_raw_left(self):
        self.service.add_move_yellow(0)
        self.service.add_move_yellow(2)
        self.service.add_move_yellow(3)
        self.assertEqual(self.service.verify_in_row_left(3, 'Y'), True)

    def test_verify_in_column(self):
        # Test the function with a valid case where there are 4 consecutive 'Y' in the first column
        self.service.add_move_yellow(1)
        self.service.add_move_yellow(1)
        self.service.add_move_yellow(1)
        self.service.add_move_yellow(1)
        self.assertEqual(self.service.verify_in_column(4, 'Y'), True)

    def test_verify_in_diagonal_right_down(self):
        for i in range(0, 4):
            for j in range(0, 4):
                self.service.add_move_red(i, j)
        assert self.service.verify_in_diagonal_right_down(4, 'R') == True

    def test_verify_diagonal_right_up(self):
        for i in range(0, 6):
            for j in range(0, 4):
                self.service.add_move_red(i, j)
        self.assertEqual(self.service.verify_in_diagonal_right_up(4, 'R'), True)

    def test_verify_diagonal_left_down(self):
        for j in range(3, 7):
            for i in range(0, 4):
                self.service.add_move_red(i, j)
        self.assertEqual(self.service.verify_in_diagonal_left_down(4, 'R'), True)

    def test_verify_diagonal_left_up(self):
        for j in range(3, 7):
            for i in range(0, 6):
                self.service.add_move_red(i, j)
        self.assertEqual(self.service.verify_in_diagonal_left_up(4, 'R'), True)

    def test_verify_win(self):
        self.service.add_move_yellow(0)
        self.service.add_move_yellow(1)
        self.service.add_move_yellow(2)
        self.service.add_move_yellow(3)
        self.assertEqual(self.service.verify_win(), "Yellow wins")

    def test_valid_input(self):
        self.assertEqual(self.service.Valid_input(4), True)
        self.assertEqual(self.service.Valid_input(7), "the column doesn't exist")
        self.assertEqual(self.service.Valid_input("Sd"), "column not int")


class Test_repo(TestCase):
    def setUp(self):
        self.repo = RepoBoard()
        self.board = []

    def test_ADD_move_yellow(self):
        self.repo.ADD_move_yellow(0)
        self.board = self.repo.copy_board
        self.assertEqual(self.board[0][0], 'Y')

    def test_ADD_move_red(self):
        self.repo.ADD_move_red(0, 0)
        self.board = self.repo.copy_board
        self.assertEqual(self.board[0][0], 'R')


if __name__ == '__main__':
    unittest.main()
