#!/usr/bin/env python3

class LineDict():

    def __init__(self):
        self. d = {}
        self.d['empty'] = 0
        self.d['empty_list'] = []
        self.d['mine'] = 0
        self.d['mine_list'] = []
        self.d['opponent'] = 0
        self.d['opponent_list'] = []

    def __call__(self):
        return self.d

    def importance(self):
        return self.d['empty'] != 0 and self.d['mine'] == 0 or self.d['opponent'] == 0

    def fill(self, board, pos_x, pos_y):
        if board[pos_x][pos_y] == ' ':
            self.d['empty'] = self.d.get('empty', 0) + 1
            self.d['empty_list'].append((pos_x, pos_y))
        elif board[pos_x][pos_y] == mark:
            self.d['mine'] = self.d.get('mine', 0) + 1
            self.d['mine_list'].append((pos_x, pos_y))
        else:
            self.d['opponent'] = self.d.get('opponent', 0) + 1
            self.d['opponent_list'].append((pos_x, pos_y))

