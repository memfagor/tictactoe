#!/usr/bin/env python3

class TicTacToe():

    def __init__(self, board_size):
        self.bs = board_size
        self.board = [[' ' for y in range(self.bs)] for x in range(self.bs)]

    def getBoardSize(self):
        return self.bs

    def checkHorizLines(self):
        for line in self.board:
            for x in line[1:]:
                if x != line[0]: break
            else: break
        else: return False
        return line[0]

    def checkVertLines(self):
        for y in range(self.bs):
            for x in range(self.bs):
                if self.board[x][y] != self.board[0][y]: break
            else: break
        else return False
        return self.board[0][y]

    def checkDiagFall(self):
        for x in range(1, self.bs):
            if self.board[x][x] != self.board[0][0]: break
        else: return self.board[0][0]
        return False

    def checkDiagRise(self):
        for x in range(1, self.bs):
            if self.board[self.bs - 1 -x][x] != self.board[self.bs - 1][0]:
                break
            else: return self.board[self.bs - 1][0]
            return False


