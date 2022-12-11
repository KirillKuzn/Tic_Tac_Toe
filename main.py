import copy
import random


class Board:
    def __init__(self, board, valid_move, winner=None):
        self.board = board
        self.winner = winner
        self.valid_move = valid_move
        self.side = 'x'

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
                    self.valid_move.remove(i)
                    return None
                else:
                    self.board[i] = '-'

        for i in range(9):
            if self.board[i] == '-':
                self.board[i] = 'X'
                self.check_win()
                if self.winner == 'X':
                    self.valid_move.remove(i)
                    self.board[i] = '0'
                    self.winner = None
                    return None
                else:
                    self.board[i] = '-'
        self.board[random.choice(self.valid_move)] = '0'
        self.valid_move.remove(random.choice(self.valid_move))


class Node:
    def __init__(self, board, win_x=0, draw=0, win_0=0, parents=None, move=None):
        self.board = board
        self.win_x = win_x
        self.draw = draw
        self.win_0 = win_0
        self.parents = parents
        self.move = move
        self.child = []


class Tree:
    def __init__(self, node):
        self.root = node

    def generate_tree(self, node):
        print('x-', self.root.win_x)
        print('0-', self.root.win_0)
        print('draw', self.root.draw)

        for move_ in node.board.valid_move:
            board_ = copy.deepcopy(node.board)
            n = Node(board_, 0, 0, 0, parents=node)
            node.child.append(n)
            n.board.board[move_] = n.board.side
            n.move = move_
            n.board.valid_move.remove(move_)
            n.board.check_win()
            if n.board.side == 'x':
                n.board.side = '0'
            else:
                n.board.side = 'x'
            if n.board.winner != None:
                self.improve_grade(n, n.board.winner)
                continue
            elif len(n.board.valid_move) == 1:
                self.improve_draw(n)

            self.generate_tree(n)

    def improve_grade(self, node, winner):
        if winner == 'x':
            node.win_x += 1
        else:
            node.win_0 += 1
        if node.parents:
            self.improve_grade(node.parents, winner)

    def improve_draw(self, node):
        node.draw += 1
        if node.parents:
            self.improve_draw(node.parents)


bd = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
n = [0, 1, 2, 3, 4, 5, 6, 7, 8]
a = 0
board = Board(bd, n)
root = Node(board)
tree = Tree(root)
tree.generate_tree(root)
board.print_board()

