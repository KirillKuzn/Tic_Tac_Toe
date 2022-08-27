import random


class Board:
    def __init__(self, board, valid, winner=None):
        self.board = board
        self.winner = winner
        self.valid = valid

    def print_board(self):
        print(self.board[0], self.board[1], self.board[2])
        print(self.board[3], self.board[4], self.board[5])
        print(self.board[6], self.board[7], self.board[8])

    def check_win(self):
        for i in range(3):
            if self.board[0 + i * 3] == self.board[1 + i * 3] == self.board[2 + i * 3] != '-':
                self.winner = self.board[0 + i * 3]
            if self.board[0 + i] == self.board[3 + i] == self.board[6 + i] != '-':
                self.winner = self.board[0 + i]
        if self.board[0] == self.board[4] == self.board[8] != '-':
            self.winner = self.board[0]
        if self.board[2] == self.board[4] == self.board[6] != '-':
            self.winner = self.board[6]

    def AI_defence(self):


        for i in range(9):
            if self.board[i] == '-':
                self.board[i] = '0'
                self.check_win()
                if self.winner == '0':
                    self.valid.remove(i)
                    return None
                else:
                    self.board[i] = '-'


        for i in range(9):
            if self.board[i] == '-':
                self.board[i] = 'X'
                self.check_win()
                if self.winner == 'X':
                    self.valid.remove(i)
                    self.board[i] = '0'
                    self.winner = None
                    return None
                else:
                    self.board[i] = '-'
        self.board[random.choice(self.valid)] = '0'
        self.valid.remove(random.choice(self.valid))

bd = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
n = [0, 1, 2, 3, 4, 5, 6, 7, 8]
a = 0
board = Board(bd, n)
board.print_board()
while len(n) > 1:
    me = int(input())
    if me >= 0 and me <= 8 and me in n:
        board.board[me] = 'X'
        n.remove(me)
        board.print_board()
        board.check_win()
        if board.winner != None:
            break
    elif me not in n:
        print('Again')
        continue
    board.AI_defence()
    board.print_board()
    board.check_win()
    if board.winner != None:
        break
