import random
import pygame
import numpy as np
from random import randint


class Sudoku(object):
    def __init__(self,):
        self.board = np.zeros((9,9), dtype=int)
        
    def get_row(self, i):
        b = self.board
        row = []
        row.append(b[i])
        return b[i]

    def get_col(self, j):
        b = self.board
        col = []
        col.append(b[:, j])
        return b[:, j]

    def get_square(self, y, x):
        y1 = int(y/3)
        x1 = int(x/3)
        square = []
        for i in range(y1*3, y1*3+3):
            for j in range(x1*3, x1*3+3):
                square.append(self.board[i, j])
        return square

    def check_number(self, num, i, j, num_list):
        
        b = self.board
        row = self.get_row(i)
        col = self.get_col(j)
        square = self.get_square(i, j)
    
        
        if num in row:
            return False
        elif num in col:
            return False
        elif num in square:
            return False
        else:
            num_list.append(num)
            return num_list
        
    def set_number(self, num, i, j):
        b = self.board
        b[i, j] = num
        return b[i, j]

def main():
    valid_numlist = []
    sudoku = Sudoku()
    for i in range(9):
        for j in range(9):
            for num in range(1, 10):
                sudoku.check_number(num, i, j, valid_numlist)
            cell_value = int(random.choice(valid_numlist))
            sudoku.board[i, j]  =  cell_value
            valid_numlist = []
    print(sudoku.board)

if __name__ == "__main__":
    main()