import random

from Cell import Cell


class Board:
    def __init__(self):
        self.board = [[Cell(), Cell(), Cell()],[Cell(), Cell(), Cell()],[Cell(), Cell(), Cell()]]

    def mark_cell(self, x, y, marker):
        self.board[x][y] = marker

    def check_winner(self):

        #checking  rows
        if self.get_marker(0, 0) == self.get_marker(0, 1) == self.get_marker(0, 2):
            return self.get_marker(0,0)
        elif self.get_marker(1, 0) == self.get_marker(1, 1) == self.get_marker(1, 2):
            return self.get_marker(1, 0)
        elif self.get_marker(2, 0) == self.get_marker(2, 1) == self.get_marker(2, 2):
            return self.get_marker(2, 0)

        # checking columns
        elif self.get_marker(0, 0) == self.get_marker(1, 0) == self.get_marker(2, 0):
            return self.get_marker(0, 0)
        elif self.get_marker(0, 1) == self.get_marker(1, 1) == self.get_marker(2, 1):
            return self.get_marker(0, 1)
        elif self.get_marker(0, 2) == self.get_marker(1, 2) == self.get_marker(2, 2):
            return self.get_marker(0, 2)

        #checking diags
        elif self.get_marker(0, 0) == self.get_marker(1, 1) == self.get_marker(2, 2):
            return self.get_marker(0, 0)
        elif self.get_marker(0, 2) == self.get_marker(1, 1) == self.get_marker(2, 0):
            return self.get_marker(0, 2)
        else:
            return None


    def get_marker(self, x, y):
        the_cell = self.board[x][y]
        if the_cell.marker == None:
            return random.random()
        else:
            return the_cell.marker

