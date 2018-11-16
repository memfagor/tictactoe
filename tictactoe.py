#!/usr/bin/env python3

class TicTacToe():

    def __init__(self, board_size=3):
        self.bs = board_size
        self.ba = []
        self.board = [[' ' for y in range(self.bs)] for x in range(self.bs)]

    def getBoardSize(self):
        return self.bs

    def printBoard(self):
        for line in self.board:
            print(line)

    def getBoardAnalyze(self):
        return self.ba

    def printBoardAnalyze(self):
        for index, line in enumerate(self.ba):
            print('Line {}:'.format(index))
            for key in line:
                print('{0} : {1}'.format(key, line[key]))

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
        else: return False
        return self.board[0][y]

    def checkDiagFall(self):
        for i in range(1, self.bs):
            if self.board[i][i] != self.board[0][0]: break
        else: return self.board[0][0]
        return False

    def checkDiagRise(self):
        for y in range(1, self.bs):
            x = self.bs -1 - y
            if self.board[x][y] != self.board[x][0]:
                break
            else: return self.board[x][0]
            return False

    def boardAnalyzeHoriz(self, mark='x'):
        analyze = []
        for x in range(self.bs):
            l = {}
            l['empty'] = 0
            l['empty_list'] = []
            l['mine'] = 0
            l['mine_list'] = []
            l['opponent'] = 0
            l['opponent_list'] = []
            for y in range(self.bs):
                if self.board[x][y] == ' ':
                    l['empty'] = l.get('empty', 0) + 1
                    l['empty_list'].append((x, y))
                elif self.board[x][y] == mark:
                    l['mine'] = l.get('mine', 0) + 1
                    l['mine_list'].append((x, y))
                else:
                    l['opponent'] = l.get('opponent', 0) + 1
                    l['opponent_list'].append((x, y))
            if l['empty'] != 0 and l['mine'] == 0 or l['opponent'] == 0:
                analyze.append(l)
        return analyze

    def boardAnalyzeVert(self, mark='x'):
        analyze = []
        for y in range(self.bs):
            l = {}
            l['empty'] = 0
            l['empty_list'] = []
            l['mine'] = 0
            l['mine_list'] = []
            l['opponent'] = 0
            l['opponent_list'] = []
            for x in range(self.bs):
                if self.board[x][y] == ' ':
                    l['empty'] = l.get('empty', 0) + 1
                    l['empty_list'].append((x, y))
                elif self.board[x][y] == mark:
                    l['mine'] = l.get('mine', 0) + 1
                    l['mine_list'].append((x, y))
                else:
                    l['opponent'] = l.get('opponent', 0) + 1
                    l['opponent_list'].append((x, y))
            if l['empty'] != 0 and l['mine'] == 0 or l['opponent'] == 0:
                analyze.append(l)
        return analyze

    def boardAnalyzeDiagFall(self, mark='x'):
        analyze = []
        l = {}
        l['empty'] = 0
        l['empty_list'] = []
        l['mine'] = 0
        l['mine_list'] = []
        l['opponent'] = 0
        l['opponent_list'] = []
        for i in range(self.bs):
            if self.board[i][i] == ' ':
                l['empty'] = l.get('empty', 0) + 1
                l['empty_list'].append((i, i))
            elif self.board[i][i] == mark:
                l['mine'] = l.get('mine', 0) + 1
                l['mine_list'].append((i, i))
            else:
                l['opponent'] = l.get('opponent', 0) + 1
                l['opponent_list'].append((i, i))
        if l['empty'] != 0 and l['mine'] == 0 or l['opponent'] == 0:
           analyze.append(l)
        return analyze

    def boardAnalyzeDiagRise(self, mark='x'):
        analyze = []
        l = {}
        l['empty'] = 0
        l['empty_list'] = []
        l['mine'] = 0
        l['mine_list'] = []
        l['opponent'] = 0
        l['opponent_list'] = []
        for y in range(self.bs):
            x = self.bs - 1 - y
            if self.board[x][y] == ' ':
                l['empty'] = l.get('empty', 0) + 1
                l['empty_list'].append((x, y))
            elif self.board[x][y] == mark:
                l['mine'] = l.get('mine', 0) + 1
                l['mine_list'].append((x, y))
            else:
                l['opponent'] = l.get('opponent', 0) + 1
                l['opponent_list'].append((x, y))
        if l['empty'] != 0 and l['mine'] == 0 or l['opponent'] == 0:
            analyze.append(l)
        return analyze


    def boardAnalyze(self, mark='x'):
        self.ba = []
        self.ba.extend(self.boardAnalyzeHoriz(mark))
        self.ba.extend(self.boardAnalyzeVert(mark))
        self.ba.extend(self.boardAnalyzeDiagRise(mark))
        self.ba.extend(self.boardAnalyzeDiagFall(mark))


