# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import time
import random


class Game:
    Alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G',
                'H', 'I', 'J']
    e1 = 0
    e1Wins=0
    totalE1 = 0
    e2 = 0
    e2Wins=0
    totalE2 = 0
    totalTime = 0
    timeInstances = 0

    def __init__(self, n=None, b=None, s=None, t=None, blocks=None, d1=None, d2=None, a=None, player_1=None,
                 player_2=None, recommend=True):
        self.n = n
        self.n = int(input('n='))
        while self.n < 3 or self.n > 10:
            print('Try again. ', end='')
            self.n = int(input('n='))
        self.b = b
        self.b = int(input('b='))
        while self.b < 0 or self.b > 2 * self.n:
            print('Try again. ', end='')
            self.b = int(input('b='))
        self.s = s
        self.s = int(input('s='))
        while self.s < 3 or self.s > self.n:
            print('Try again. ', end='')
            self.s = int(input('s='))
        self.t = t
        self.t = int(input('t='))
        while self.t < 1:
            print('Try again. ', end='')
            self.t = int(input('t='))
        self.blocks = blocks
        self.blocks = [[0 for i in range(2)] for j in range(self.b)]
        for x in range(0, self.b):
            for y in range(0, 2):
                self.blocks[x][y] = random.choice(range(0, self.n))
        print('Blocks=', self.blocks)
        print()
        print('Player 1:')
        self.player_1 = player_1
        self.player_1 = str(input('Human or AI? '))
        self.d1 = d1
        self.d1 = int(input('d='))
        while self.d1 < 1:
            print('Try again. ', end='')
            self.d1 = int(input('d='))
        self.a = a
        self.a = str(input('a='))

        print()
        print('Player 2:')
        self.player_2 = player_2
        self.player_2 = str(input('Human or AI? '))
        self.d2 = d2
        self.d2 = int(input('d='))
        while self.d2 < 1:
            print('Try again. ', end='')
            self.d2 = int(input('d='))
        print(F'a={self.a}')
        self.initialize_game()
        self.recommend = recommend

    def initialize_game(self):

        if self.n == 3:
            self.current_state = [[' ', ' ', 'A', 'B', 'C'],
                                  [' ', '+', '-', '-', '-'],
                                  ['0', '|', '.', '.', '.'],
                                  ['1', '|', '.', '.', '.'],
                                  ['2', '|', '.', '.', '.']]
            self.player_turn = 'X'  # Player X plays first
            px = None
            py = None
            for x in range(0, self.b):
                px = self.blocks[x][1]
                if px == self.n:
                    px = px
                py = self.blocks[x][0]
                if py == self.n:
                    py = py
                self.current_state[px + 2][py + 2] = '*'

        if self.n == 4:
            self.current_state = [[' ', ' ', 'A', 'B', 'C', 'D'],
                                  [' ', '+', '-', '-', '-', '-'],
                                  ['0', '|', '.', '.', '.', '.'],
                                  ['1', '|', '.', '.', '.', '.'],
                                  ['2', '|', '.', '.', '.', '.'],
                                  ['3', '|', '.', '.', '.', '.']]
            self.player_turn = 'X'  # Player X plays first
            px = None
            py = None
            for x in range(0, self.b):
                px = self.blocks[x][1]
                if px == self.n:
                    px = px - 1
                py = self.blocks[x][0]
                if py == self.n:
                    py = py - 1
                self.current_state[px + 2][py + 2] = '*'

        if self.n == 5:
            self.current_state = [[' ', ' ', 'A', 'B', 'C', 'D', 'E'],
                                  [' ', '+', '-', '-', '-', '-', '-'],
                                  ['0', '|', '.', '.', '.', '.', '.'],
                                  ['1', '|', '.', '.', '.', '.', '.'],
                                  ['2', '|', '.', '.', '.', '.', '.'],
                                  ['3', '|', '.', '.', '.', '.', '.'],
                                  ['4', '|', '.', '.', '.', '.', '.']]
            self.player_turn = 'X'  # Player X plays first
            px = None
            py = None
            for x in range(0, self.b):
                px = self.blocks[x][1]
                if px == self.n:
                    px = px - 1
                py = self.blocks[x][0]
                if py == self.n:
                    py = py - 1
                self.current_state[px + 2][py + 2] = '*'

        if self.n == 6:
            self.current_state = [[' ', ' ', 'A', 'B', 'C', 'D', 'E', 'F'],
                                  [' ', '+', '-', '-', '-', '-', '-', '-'],
                                  ['0', '|', '.', '.', '.', '.', '.', '.'],
                                  ['1', '|', '.', '.', '.', '.', '.', '.'],
                                  ['2', '|', '.', '.', '.', '.', '.', '.'],
                                  ['3', '|', '.', '.', '.', '.', '.', '.'],
                                  ['4', '|', '.', '.', '.', '.', '.', '.'],
                                  ['5', '|', '.', '.', '.', '.', '.', '.']]
            self.player_turn = 'X'  # Player X plays first
            px = None
            py = None
            for x in range(0, self.b):
                px = self.blocks[x][1]
                if px == self.n:
                    px = px - 1
                py = self.blocks[x][0]
                if py == self.n:
                    py = py - 1
                self.current_state[px + 2][py + 2] = '*'

        if self.n == 7:
            self.current_state = [[' ', ' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G'],
                                  [' ', '+', '-', '-', '-', '-', '-', '-', '-'],
                                  ['0', '|', '.', '.', '.', '.', '.', '.', '.'],
                                  ['1', '|', '.', '.', '.', '.', '.', '.', '.'],
                                  ['2', '|', '.', '.', '.', '.', '.', '.', '.'],
                                  ['3', '|', '.', '.', '.', '.', '.', '.', '.'],
                                  ['4', '|', '.', '.', '.', '.', '.', '.', '.'],
                                  ['5', '|', '.', '.', '.', '.', '.', '.', '.'],
                                  ['6', '|', '.', '.', '.', '.', '.', '.', '.']]
            self.player_turn = 'X'  # Player X plays first
            px = None
            py = None
            for x in range(0, self.b):
                px = self.blocks[x][1]
                if px == self.n:
                    px = px - 1
                py = self.blocks[x][0]
                if py == self.n:
                    py = py - 1
                self.current_state[px + 2][py + 2] = '*'

        if self.n == 8:
            self.current_state = [[' ', ' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'],
                                  [' ', '+', '-', '-', '-', '-', '-', '-', '-', '-'],
                                  ['0', '|', '.', '.', '.', '.', '.', '.', '.', '.'],
                                  ['1', '|', '.', '.', '.', '.', '.', '.', '.', '.'],
                                  ['2', '|', '.', '.', '.', '.', '.', '.', '.', '.'],
                                  ['3', '|', '.', '.', '.', '.', '.', '.', '.', '.'],
                                  ['4', '|', '.', '.', '.', '.', '.', '.', '.', '.'],
                                  ['5', '|', '.', '.', '.', '.', '.', '.', '.', '.'],
                                  ['6', '|', '.', '.', '.', '.', '.', '.', '.', '.'],
                                  ['7', '|', '.', '.', '.', '.', '.', '.', '.', '.']]
            self.player_turn = 'X'  # Player X plays first
            px = None
            py = None
            for x in range(0, self.b):
                px = self.blocks[x][1]
                if px == self.n:
                    px = px - 1
                py = self.blocks[x][0]
                if py == self.n:
                    py = py - 1
                self.current_state[px + 2][py + 2] = '*'

        if self.n == 9:
            self.current_state = [[' ', ' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
                                  [' ', '+', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                                  ['0', '|', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                                  ['1', '|', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                                  ['2', '|', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                                  ['3', '|', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                                  ['4', '|', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                                  ['5', '|', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                                  ['6', '|', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                                  ['7', '|', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                                  ['8', '|', '.', '.', '.', '.', '.', '.', '.', '.', '.']]
            self.player_turn = 'X'  # Player X plays first
            px = None
            py = None
            for x in range(0, self.b):
                px = self.blocks[x][1]
                if px == self.n:
                    px = px - 1
                py = self.blocks[x][0]
                if py == self.n:
                    py = py - 1
                self.current_state[px + 2][py + 2] = '*'

        if self.n == 10:
            self.current_state = [[' ', ' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
                                  [' ', '+', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                                  ['0', '|', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                                  ['1', '|', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                                  ['2', '|', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                                  ['3', '|', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                                  ['4', '|', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                                  ['5', '|', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                                  ['6', '|', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                                  ['7', '|', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                                  ['8', '|', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                                  ['9', '|', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']]
            self.player_turn = 'X'  # Player X plays first
            px = None
            py = None
            for x in range(0, self.b):
                px = self.blocks[x][1]
                if px == self.n:
                    px = px - 1
                py = self.blocks[x][0]
                if py == self.n:
                    py = py - 1
                self.current_state[px + 2][py + 2] = '*'

    def draw_board(self):
        print()
        for x in range(0, self.n + 2):
            for y in range(0, self.n + 2):
                print(F'{self.current_state[x][y]}', end="")
            print()
        print()

    def is_end(self):
        if self.s == 3:
            # Vertical win
            for i in range(2, self.n + 2):
                for j in range(2, self.n + 2):
                    if (i <= self.n - self.s + 2 and self.current_state[i][j] != '.' and
                            self.current_state[i][j] == self.current_state[i + 1][j] and
                            self.current_state[i + 1][j] == self.current_state[i + 2][j]):
                        return self.current_state[i][j]
            # Horizontal win
            for j in range(2, self.n + 2):
                for i in range(2, self.n + 2):
                    if (j <= self.n - self.s + 2 and self.current_state[i][j] == 'X' and
                            self.current_state[i][j] == self.current_state[i][j + 1] and
                            self.current_state[i][j + 1] == self.current_state[i][j + 2]):
                        return 'X'
                    elif (j <= self.n - self.s + 2 and self.current_state[i][j] == 'O' and
                          self.current_state[i][j] == self.current_state[i][j + 1] and
                          self.current_state[i][j + 1] == self.current_state[i][j + 2]):
                        return 'O'
            # Main diagonal win
            for i in range(2, self.n + 2):
                for j in range(2, self.n + 2):
                    if (i <= self.n - self.s + 2 and j <= self.n - self.s + 2 and
                            self.current_state[i][j] != '.' and
                            self.current_state[i][j] == self.current_state[i + 1][j + 1] and
                            self.current_state[i][j] == self.current_state[i + 2][j + 2]):
                        return self.current_state[i][j]
            # Second diagonal win
            for i in range(2, self.n + 2):
                for j in range(self.n + 1, 1, -1):
                    if (i <= self.n - self.s + 2 <= j and
                            self.current_state[i][j] != '.' and
                            self.current_state[i][j] == self.current_state[i + 1][j - 1] and
                            self.current_state[i][j] == self.current_state[i + 2][j - 2]):
                        return self.current_state[i][j]
            # Is whole board full?
            for i in range(2, self.n + 2):
                for j in range(2, self.n + 2):
                    # There's an empty field, we continue the game
                    if self.current_state[i][j] == '.':
                        return None
            # It's a tie!
            return '.'

        if self.s == 4:
            # Vertical win
            for i in range(2, self.n + 2):
                for j in range(2, self.n + 2):
                    if (i <= self.n - self.s + 2 and self.current_state[i][j] != '.' and
                            self.current_state[i][j] == self.current_state[i + 1][j] and
                            self.current_state[i + 1][j] == self.current_state[i + 2][j] and
                            self.current_state[i + 2][j] == self.current_state[i + 3][j]):
                        return self.current_state[i][j]
            # Horizontal win
            for j in range(2, self.n + 2):
                for i in range(2, self.n + 2):
                    if (j <= self.n - self.s + 2 and self.current_state[i][j] == 'X' and
                            self.current_state[i][j] == self.current_state[i][j + 1] and
                            self.current_state[i][j + 1] == self.current_state[i][j + 2] and
                            self.current_state[i][j + 2] == self.current_state[i][j + 3]):
                        return 'X'
                    elif (j <= self.n - self.s + 2 and self.current_state[i][j] == 'O' and
                          self.current_state[i][j] == self.current_state[i][j + 1] and
                          self.current_state[i][j + 1] == self.current_state[i][j + 2] and
                          self.current_state[i][j + 2] == self.current_state[i][j + 3]):
                        return 'O'
            # Main diagonal win
            for i in range(2, self.n + 2):
                for j in range(2, self.n + 2):
                    if (i <= self.n - self.s + 2 and j <= self.n - self.s + 2 and
                            self.current_state[i][j] != '.' and
                            self.current_state[i][j] == self.current_state[i + 1][j + 1] and
                            self.current_state[i][j] == self.current_state[i + 2][j + 2] and
                            self.current_state[i][j] == self.current_state[i + 3][j + 3]):
                        return self.current_state[i][j]
            # Second diagonal win
            for i in range(2, self.n + 2):
                for j in range(self.n + 1, 1, -1):
                    if (i <= self.n - self.s + 2 <= j and
                            self.current_state[i][j] != '.' and
                            self.current_state[i][j] == self.current_state[i + 1][j - 1] and
                            self.current_state[i][j] == self.current_state[i + 2][j - 2] and
                            self.current_state[i][j] == self.current_state[i + 3][j - 3]):
                        return self.current_state[i][j]
            # Is whole board full?
            for i in range(2, self.n + 2):
                for j in range(2, self.n + 2):
                    # There's an empty field, we continue the game
                    if self.current_state[i][j] == '.':
                        return None
            # It's a tie!
            return '.'

        if self.s == 5:
            # Vertical win
            for i in range(2, self.n + 2):
                for j in range(2, self.n + 2):
                    if (i <= self.n - self.s + 2 and self.current_state[i][j] != '.' and
                            self.current_state[i][j] == self.current_state[i + 1][j] and
                            self.current_state[i + 1][j] == self.current_state[i + 2][j] and
                            self.current_state[i + 2][j] == self.current_state[i + 3][j] and
                            self.current_state[i + 3][j] == self.current_state[i + 4][j]):
                        return self.current_state[i][j]
            # Horizontal win
            for j in range(2, self.n + 2):
                for i in range(2, self.n + 2):
                    if (j <= self.n - self.s + 2 and self.current_state[i][j] == 'X' and
                            self.current_state[i][j] == self.current_state[i][j + 1] and
                            self.current_state[i][j + 1] == self.current_state[i][j + 2] and
                            self.current_state[i][j + 2] == self.current_state[i][j + 3] and
                            self.current_state[i][j + 3] == self.current_state[i][j + 4]):
                        return 'X'
                    elif (j <= self.n - self.s + 2 and self.current_state[i][j] == 'O' and
                          self.current_state[i][j] == self.current_state[i][j + 1] and
                          self.current_state[i][j + 1] == self.current_state[i][j + 2] and
                          self.current_state[i][j + 2] == self.current_state[i][j + 3] and
                          self.current_state[i][j + 3] == self.current_state[i][j + 4]):
                        return 'O'
            # Main diagonal win
            for i in range(2, self.n + 2):
                for j in range(2, self.n + 2):
                    if (i <= self.n - self.s + 2 and j <= self.n - self.s + 2 and
                            self.current_state[i][j] != '.' and
                            self.current_state[i][j] == self.current_state[i + 1][j + 1] and
                            self.current_state[i][j] == self.current_state[i + 2][j + 2] and
                            self.current_state[i][j] == self.current_state[i + 3][j + 3] and
                            self.current_state[i][j] == self.current_state[i + 4][j + 4]):
                        return self.current_state[i][j]
            # Second diagonal win
            for i in range(2, self.n + 2):
                for j in range(self.n + 1, 1, -1):
                    if (i <= self.n - self.s + 2 <= j and
                            self.current_state[i][j] != '.' and
                            self.current_state[i][j] == self.current_state[i + 1][j - 1] and
                            self.current_state[i][j] == self.current_state[i + 2][j - 2] and
                            self.current_state[i][j] == self.current_state[i + 3][j - 3] and
                            self.current_state[i][j] == self.current_state[i + 4][j - 4]):
                        return self.current_state[i][j]
            # Is whole board full?
            for i in range(2, self.n + 2):
                for j in range(2, self.n + 2):
                    # There's an empty field, we continue the game
                    if self.current_state[i][j] == '.':
                        return None
            # It's a tie!
            return '.'

        if self.s == 6:
            # Vertical win
            for i in range(2, self.n + 2):
                for j in range(2, self.n + 2):
                    if (i <= self.n - self.s + 2 and self.current_state[i][j] != '.' and
                            self.current_state[i][j] == self.current_state[i + 1][j] and
                            self.current_state[i + 1][j] == self.current_state[i + 2][j] and
                            self.current_state[i + 2][j] == self.current_state[i + 3][j] and
                            self.current_state[i + 3][j] == self.current_state[i + 4][j] and
                            self.current_state[i + 4][j] == self.current_state[i + 5][j]):
                        return self.current_state[i][j]
            # Horizontal win
            for j in range(2, self.n + 2):
                for i in range(2, self.n + 2):
                    if (j <= self.n - self.s + 2 and self.current_state[i][j] == 'X' and
                            self.current_state[i][j] == self.current_state[i][j + 1] and
                            self.current_state[i][j + 1] == self.current_state[i][j + 2] and
                            self.current_state[i][j + 2] == self.current_state[i][j + 3] and
                            self.current_state[i][j + 3] == self.current_state[i][j + 4] and
                            self.current_state[i][j + 4] == self.current_state[i][j + 5]):
                        return 'X'
                    elif (j <= self.n - self.s + 2 and self.current_state[i][j] == 'O' and
                          self.current_state[i][j] == self.current_state[i][j + 1] and
                          self.current_state[i][j + 1] == self.current_state[i][j + 2] and
                          self.current_state[i][j + 2] == self.current_state[i][j + 3] and
                          self.current_state[i][j + 3] == self.current_state[i][j + 4] and
                          self.current_state[i][j + 4] == self.current_state[i][j + 5]):
                        return 'O'
            # Main diagonal win
            for i in range(2, self.n + 2):
                for j in range(2, self.n + 2):
                    if (i <= self.n - self.s + 2 and j <= self.n - self.s + 2 and
                            self.current_state[i][j] != '.' and
                            self.current_state[i][j] == self.current_state[i + 1][j + 1] and
                            self.current_state[i][j] == self.current_state[i + 2][j + 2] and
                            self.current_state[i][j] == self.current_state[i + 3][j + 3] and
                            self.current_state[i][j] == self.current_state[i + 4][j + 4] and
                            self.current_state[i][j] == self.current_state[i + 5][j + 5]):
                        return self.current_state[i][j]
            # Second diagonal win
            for i in range(2, self.n + 2):
                for j in range(self.n + 1, 1, -1):
                    if (i <= self.n - self.s + 2 <= j and
                            self.current_state[i][j] != '.' and
                            self.current_state[i][j] == self.current_state[i + 1][j - 1] and
                            self.current_state[i][j] == self.current_state[i + 2][j - 2] and
                            self.current_state[i][j] == self.current_state[i + 3][j - 3] and
                            self.current_state[i][j] == self.current_state[i + 4][j - 4] and
                            self.current_state[i][j] == self.current_state[i + 5][j - 5]):
                        return self.current_state[i][j]
            # Is whole board full?
            for i in range(2, self.n + 2):
                for j in range(2, self.n + 2):
                    # There's an empty field, we continue the game
                    if self.current_state[i][j] == '.':
                        return None
            # It's a tie!
            return '.'

        if self.s == 7:
            # Vertical win
            for i in range(2, self.n + 2):
                for j in range(2, self.n + 2):
                    if (i <= self.n - self.s + 2 and self.current_state[i][j] != '.' and
                            self.current_state[i][j] == self.current_state[i + 1][j] and
                            self.current_state[i + 1][j] == self.current_state[i + 2][j] and
                            self.current_state[i + 2][j] == self.current_state[i + 3][j] and
                            self.current_state[i + 3][j] == self.current_state[i + 4][j] and
                            self.current_state[i + 4][j] == self.current_state[i + 5][j] and
                            self.current_state[i + 5][j] == self.current_state[i + 6][j]):
                        return self.current_state[i][j]
            # Horizontal win
            for j in range(2, self.n + 2):
                for i in range(2, self.n + 2):
                    if (j <= self.n - self.s + 2 and self.current_state[i][j] == 'X' and
                            self.current_state[i][j] == self.current_state[i][j + 1] and
                            self.current_state[i][j + 1] == self.current_state[i][j + 2] and
                            self.current_state[i][j + 2] == self.current_state[i][j + 3] and
                            self.current_state[i][j + 3] == self.current_state[i][j + 4] and
                            self.current_state[i][j + 4] == self.current_state[i][j + 5] and
                            self.current_state[i][j + 5] == self.current_state[i][j + 6]):
                        return 'X'
                    elif (j <= self.n - self.s + 2 and self.current_state[i][j] == 'O' and
                          self.current_state[i][j] == self.current_state[i][j + 1] and
                          self.current_state[i][j + 1] == self.current_state[i][j + 2] and
                          self.current_state[i][j + 2] == self.current_state[i][j + 3] and
                          self.current_state[i][j + 3] == self.current_state[i][j + 4] and
                          self.current_state[i][j + 4] == self.current_state[i][j + 5] and
                          self.current_state[i][j + 5] == self.current_state[i][j + 6]):
                        return 'O'
            # Main diagonal win
            for i in range(2, self.n + 2):
                for j in range(2, self.n + 2):
                    if (i <= self.n - self.s + 2 and j <= self.n - self.s + 2 and
                            self.current_state[i][j] != '.' and
                            self.current_state[i][j] == self.current_state[i + 1][j + 1] and
                            self.current_state[i][j] == self.current_state[i + 2][j + 2] and
                            self.current_state[i][j] == self.current_state[i + 3][j + 3] and
                            self.current_state[i][j] == self.current_state[i + 4][j + 4] and
                            self.current_state[i][j] == self.current_state[i + 5][j + 5] and
                            self.current_state[i][j] == self.current_state[i + 6][j + 6]):
                        return self.current_state[i][j]
            # Second diagonal win
            for i in range(2, self.n + 2):
                for j in range(self.n + 1, 1, -1):
                    if (i <= self.n - self.s + 2 <= j and
                            self.current_state[i][j] != '.' and
                            self.current_state[i][j] == self.current_state[i + 1][j - 1] and
                            self.current_state[i][j] == self.current_state[i + 2][j - 2] and
                            self.current_state[i][j] == self.current_state[i + 3][j - 3] and
                            self.current_state[i][j] == self.current_state[i + 4][j - 4] and
                            self.current_state[i][j] == self.current_state[i + 5][j - 5] and
                            self.current_state[i][j] == self.current_state[i + 6][j - 6]):
                        return self.current_state[i][j]
            # Is whole board full?
            for i in range(2, self.n + 2):
                for j in range(2, self.n + 2):
                    # There's an empty field, we continue the game
                    if self.current_state[i][j] == '.':
                        return None
            # It's a tie!
            return '.'

        if self.s == 8:
            # Vertical win
            for i in range(2, self.n + 2):
                for j in range(2, self.n + 2):
                    if (i <= self.n - self.s + 2 and self.current_state[i][j] != '.' and
                            self.current_state[i][j] == self.current_state[i + 1][j] and
                            self.current_state[i + 1][j] == self.current_state[i + 2][j] and
                            self.current_state[i + 2][j] == self.current_state[i + 3][j] and
                            self.current_state[i + 3][j] == self.current_state[i + 4][j] and
                            self.current_state[i + 4][j] == self.current_state[i + 5][j] and
                            self.current_state[i + 5][j] == self.current_state[i + 6][j] and
                            self.current_state[i + 6][j] == self.current_state[i + 7][j]):
                        return self.current_state[i][j]
            # Horizontal win
            for j in range(2, self.n + 2):
                for i in range(2, self.n + 2):
                    if (j <= self.n - self.s + 2 and self.current_state[i][j] == 'X' and
                            self.current_state[i][j] == self.current_state[i][j + 1] and
                            self.current_state[i][j + 1] == self.current_state[i][j + 2] and
                            self.current_state[i][j + 2] == self.current_state[i][j + 3] and
                            self.current_state[i][j + 3] == self.current_state[i][j + 4] and
                            self.current_state[i][j + 4] == self.current_state[i][j + 5] and
                            self.current_state[i][j + 5] == self.current_state[i][j + 6] and
                            self.current_state[i][j + 6] == self.current_state[i][j + 7]):
                        return 'X'
                    elif (j <= self.n - self.s + 2 and self.current_state[i][j] == 'O' and
                          self.current_state[i][j] == self.current_state[i][j + 1] and
                          self.current_state[i][j + 1] == self.current_state[i][j + 2] and
                          self.current_state[i][j + 2] == self.current_state[i][j + 3] and
                          self.current_state[i][j + 3] == self.current_state[i][j + 4] and
                          self.current_state[i][j + 4] == self.current_state[i][j + 5] and
                          self.current_state[i][j + 5] == self.current_state[i][j + 6] and
                          self.current_state[i][j + 6] == self.current_state[i][j + 7]):
                        return 'O'
            # Main diagonal win
            for i in range(2, self.n + 2):
                for j in range(2, self.n + 2):
                    if (i <= self.n - self.s + 2 and j <= self.n - self.s + 2 and
                            self.current_state[i][j] != '.' and
                            self.current_state[i][j] == self.current_state[i + 1][j + 1] and
                            self.current_state[i][j] == self.current_state[i + 2][j + 2] and
                            self.current_state[i][j] == self.current_state[i + 3][j + 3] and
                            self.current_state[i][j] == self.current_state[i + 4][j + 4] and
                            self.current_state[i][j] == self.current_state[i + 5][j + 5] and
                            self.current_state[i][j] == self.current_state[i + 6][j + 6] and
                            self.current_state[i][j] == self.current_state[i + 7][j + 7]):
                        return self.current_state[i][j]
            # Second diagonal win
            for i in range(2, self.n + 2):
                for j in range(self.n + 1, 1, -1):
                    if (i <= self.n - self.s + 2 <= j and
                            self.current_state[i][j] != '.' and
                            self.current_state[i][j] == self.current_state[i + 1][j - 1] and
                            self.current_state[i][j] == self.current_state[i + 2][j - 2] and
                            self.current_state[i][j] == self.current_state[i + 3][j - 3] and
                            self.current_state[i][j] == self.current_state[i + 4][j - 4] and
                            self.current_state[i][j] == self.current_state[i + 5][j - 5] and
                            self.current_state[i][j] == self.current_state[i + 6][j - 6] and
                            self.current_state[i][j] == self.current_state[i + 7][j - 7]):
                        return self.current_state[i][j]
            # Is whole board full?
            for i in range(2, self.n + 2):
                for j in range(2, self.n + 2):
                    # There's an empty field, we continue the game
                    if self.current_state[i][j] == '.':
                        return None
            # It's a tie!
            return '.'

        if self.s == 9:
            # Vertical win
            for i in range(2, self.n + 2):
                for j in range(2, self.n + 2):
                    if (i <= self.n - self.s + 2 and self.current_state[i][j] != '.' and
                            self.current_state[i][j] == self.current_state[i + 1][j] and
                            self.current_state[i + 1][j] == self.current_state[i + 2][j] and
                            self.current_state[i + 2][j] == self.current_state[i + 3][j] and
                            self.current_state[i + 3][j] == self.current_state[i + 4][j] and
                            self.current_state[i + 4][j] == self.current_state[i + 5][j] and
                            self.current_state[i + 5][j] == self.current_state[i + 6][j] and
                            self.current_state[i + 6][j] == self.current_state[i + 7][j] and
                            self.current_state[i + 7][j] == self.current_state[i + 8][j]):
                        return self.current_state[i][j]
            # Horizontal win
            for j in range(2, self.n + 2):
                for i in range(2, self.n + 2):
                    if (j <= self.n - self.s + 2 and self.current_state[i][j] == 'X' and
                            self.current_state[i][j] == self.current_state[i][j + 1] and
                            self.current_state[i][j + 1] == self.current_state[i][j + 2] and
                            self.current_state[i][j + 2] == self.current_state[i][j + 3] and
                            self.current_state[i][j + 3] == self.current_state[i][j + 4] and
                            self.current_state[i][j + 4] == self.current_state[i][j + 5] and
                            self.current_state[i][j + 5] == self.current_state[i][j + 6] and
                            self.current_state[i][j + 6] == self.current_state[i][j + 7] and
                            self.current_state[i][j + 7] == self.current_state[i][j + 8]):
                        return 'X'
                    elif (j <= self.n - self.s + 2 and self.current_state[i][j] == 'O' and
                          self.current_state[i][j] == self.current_state[i][j + 1] and
                          self.current_state[i][j + 1] == self.current_state[i][j + 2] and
                          self.current_state[i][j + 2] == self.current_state[i][j + 3] and
                          self.current_state[i][j + 3] == self.current_state[i][j + 4] and
                          self.current_state[i][j + 4] == self.current_state[i][j + 5] and
                          self.current_state[i][j + 5] == self.current_state[i][j + 6] and
                          self.current_state[i][j + 6] == self.current_state[i][j + 7] and
                          self.current_state[i][j + 7] == self.current_state[i][j + 8]):
                        return 'O'
            # Main diagonal win
            for i in range(2, self.n + 2):
                for j in range(2, self.n + 2):
                    if (i <= self.n - self.s + 2 and j <= self.n - self.s + 2 and
                            self.current_state[i][j] != '.' and
                            self.current_state[i][j] == self.current_state[i + 1][j + 1] and
                            self.current_state[i][j] == self.current_state[i + 2][j + 2] and
                            self.current_state[i][j] == self.current_state[i + 3][j + 3] and
                            self.current_state[i][j] == self.current_state[i + 4][j + 4] and
                            self.current_state[i][j] == self.current_state[i + 5][j + 5] and
                            self.current_state[i][j] == self.current_state[i + 6][j + 6] and
                            self.current_state[i][j] == self.current_state[i + 7][j + 7] and
                            self.current_state[i][j] == self.current_state[i + 8][j + 8]):
                        return self.current_state[i][j]
            # Second diagonal win
            for i in range(2, self.n + 2):
                for j in range(self.n + 1, 1, -1):
                    if (i <= self.n - self.s + 2 <= j and
                            self.current_state[i][j] != '.' and
                            self.current_state[i][j] == self.current_state[i + 1][j - 1] and
                            self.current_state[i][j] == self.current_state[i + 2][j - 2] and
                            self.current_state[i][j] == self.current_state[i + 3][j - 3] and
                            self.current_state[i][j] == self.current_state[i + 4][j - 4] and
                            self.current_state[i][j] == self.current_state[i + 5][j - 5] and
                            self.current_state[i][j] == self.current_state[i + 6][j - 6] and
                            self.current_state[i][j] == self.current_state[i + 7][j - 7] and
                            self.current_state[i][j] == self.current_state[i + 8][j - 8]):
                        return self.current_state[i][j]
            # Is whole board full?
            for i in range(2, self.n + 2):
                for j in range(2, self.n + 2):
                    # There's an empty field, we continue the game
                    if self.current_state[i][j] == '.':
                        return None
            # It's a tie!
            return '.'

        if self.s == 10:
            # Vertical win
            for i in range(2, self.n + 2):
                for j in range(2, self.n + 2):
                    if (i <= self.n - self.s + 2 and self.current_state[i][j] != '.' and
                            self.current_state[i][j] == self.current_state[i + 1][j] and
                            self.current_state[i + 1][j] == self.current_state[i + 2][j] and
                            self.current_state[i + 2][j] == self.current_state[i + 3][j] and
                            self.current_state[i + 3][j] == self.current_state[i + 4][j] and
                            self.current_state[i + 4][j] == self.current_state[i + 5][j] and
                            self.current_state[i + 5][j] == self.current_state[i + 6][j] and
                            self.current_state[i + 6][j] == self.current_state[i + 7][j] and
                            self.current_state[i + 7][j] == self.current_state[i + 8][j] and
                            self.current_state[i + 8][j] == self.current_state[i + 9][j]):
                        return self.current_state[i][j]
            # Horizontal win
            for j in range(2, self.n + 2):
                for i in range(2, self.n + 2):
                    if (j <= self.n - self.s + 2 and self.current_state[i][j] == 'X' and
                            self.current_state[i][j] == self.current_state[i][j + 1] and
                            self.current_state[i][j + 1] == self.current_state[i][j + 2] and
                            self.current_state[i][j + 2] == self.current_state[i][j + 3] and
                            self.current_state[i][j + 3] == self.current_state[i][j + 4] and
                            self.current_state[i][j + 4] == self.current_state[i][j + 5] and
                            self.current_state[i][j + 5] == self.current_state[i][j + 6] and
                            self.current_state[i][j + 6] == self.current_state[i][j + 7] and
                            self.current_state[i][j + 7] == self.current_state[i][j + 8] and
                            self.current_state[i][j + 8] == self.current_state[i][j + 9]):
                        return 'X'
                    elif (j <= self.n - self.s + 2 and self.current_state[i][j] == 'O' and
                          self.current_state[i][j] == self.current_state[i][j + 1] and
                          self.current_state[i][j + 1] == self.current_state[i][j + 2] and
                          self.current_state[i][j + 2] == self.current_state[i][j + 3] and
                          self.current_state[i][j + 3] == self.current_state[i][j + 4] and
                          self.current_state[i][j + 4] == self.current_state[i][j + 5] and
                          self.current_state[i][j + 5] == self.current_state[i][j + 6] and
                          self.current_state[i][j + 6] == self.current_state[i][j + 7] and
                          self.current_state[i][j + 7] == self.current_state[i][j + 8] and
                          self.current_state[i][j + 8] == self.current_state[i][j + 9]):
                        return 'O'
            # Main diagonal win
            for i in range(2, self.n + 2):
                for j in range(2, self.n + 2):
                    if (i <= self.n - self.s + 2 and j <= self.n - self.s + 2 and
                            self.current_state[i][j] != '.' and
                            self.current_state[i][j] == self.current_state[i + 1][j + 1] and
                            self.current_state[i][j] == self.current_state[i + 2][j + 2] and
                            self.current_state[i][j] == self.current_state[i + 3][j + 3] and
                            self.current_state[i][j] == self.current_state[i + 4][j + 4] and
                            self.current_state[i][j] == self.current_state[i + 5][j + 5] and
                            self.current_state[i][j] == self.current_state[i + 6][j + 6] and
                            self.current_state[i][j] == self.current_state[i + 7][j + 7] and
                            self.current_state[i][j] == self.current_state[i + 8][j + 8] and
                            self.current_state[i][j] == self.current_state[i + 9][j + 9]):
                        return self.current_state[i][j]
            # Second diagonal win
            for i in range(2, self.n + 2):
                for j in range(self.n + 1, 1, -1):
                    if (i <= self.n - self.s + 2 <= j and
                            self.current_state[i][j] != '.' and
                            self.current_state[i][j] == self.current_state[i + 1][j - 1] and
                            self.current_state[i][j] == self.current_state[i + 2][j - 2] and
                            self.current_state[i][j] == self.current_state[i + 3][j - 3] and
                            self.current_state[i][j] == self.current_state[i + 4][j - 4] and
                            self.current_state[i][j] == self.current_state[i + 5][j - 5] and
                            self.current_state[i][j] == self.current_state[i + 6][j - 6] and
                            self.current_state[i][j] == self.current_state[i + 7][j - 7] and
                            self.current_state[i][j] == self.current_state[i + 8][j - 8] and
                            self.current_state[i][j] == self.current_state[i + 9][j + 9]):
                        return self.current_state[i][j]
            # Is whole board full?
            for i in range(2, self.n + 2):
                for j in range(2, self.n + 2):
                    # There's an empty field, we continue the game
                    if self.current_state[i][j] == '.':
                        return None
            # It's a tie!
            return '.'

    def check_end(self):
        self.result = self.is_end()
        # Printing the appropriate message if the game has ended
        if self.result != None:
            if self.result == 'X':
                print('The winner is X!')
                print(F'i   Average evaluation time: {round(self.totalTime / self.timeInstances, 7)}')
                print(F'ii  Total heuristic evaluations: {self.totalE1 + self.totalE2}')
                self.e1Wins=self.e1Wins+1
            elif self.result == 'O':
                print('The winner is O!')
                print(F'i   Average evaluation time: {round(self.totalTime / self.timeInstances, 7)}')
                print(F'ii  Total heuristic evaluations: {self.totalE1 + self.totalE2}')
                self.e2Wins = self.e2Wins + 1
            elif self.result == '.':
                print("It's a tie!")
                print(F'i   Average evaluation time: {round(self.totalTime / self.timeInstances, 7)}')
                print(F'ii  Total heuristic evaluations: {self.totalE1 + self.totalE2}')
                self.totalTime = 0
                self.timeInstances = 0
                self.totalE1 = 0
                self.totalE2 = 0

            self.initialize_game()
        return self.result

    def switch_player(self):
        if self.player_turn == 'X':
            self.player_turn = 'O'
        elif self.player_turn == 'O':
            self.player_turn = 'X'
        return self.player_turn

    def minimax(self, max=False):
        # Minimizing for 'X' and maximizing for 'O'
        # Possible values are:
        # -1 - win for 'X'
        # 0  - a tie
        # 1  - loss for 'X'
        # We're initially setting it to 2 or -2 as worse than the worst case:
        value = 2
        if max:
            value = -2
        x = None
        y = None
        result = self.is_end()
        if result == 'X':
            return -1, x, y
        elif result == 'O':
            return 1, x, y
        elif result == '.':
            return 0, x, y
        for i in range(2, self.n + 2):
            for j in range(2, self.n + 2):
                if self.current_state[i][j] == '.':
                    if max:
                        self.current_state[i][j] = 'O'
                        self.e2 = self.e2 + 1
                        (v, _, _) = self.minimax(max=False)
                        if v > value:
                            value = v
                            x = i - 2
                            y = self.current_state[0][j]
                    else:
                        self.current_state[i][j] = 'X'
                        self.e1 = self.e1 + 1
                        (v, _, _) = self.minimax(max=True)
                        if v < value:
                            value = v
                            x = i - 2
                            y = self.current_state[0][j]
                    self.current_state[i][j] = '.'
        return value, x, y

    def alphabeta(self, alpha=-2, beta=2, max=False):
        # Minimizing for 'X' and maximizing for 'O'
        # Possible values are:
        # -1 - win for 'X'
        # 0  - a tie
        # 1  - loss for 'X'
        # We're initially setting it to 2 or -2 as worse than the worst case:
        value = 2
        if max:
            value = -2
        x = None
        y = None
        result = self.is_end()
        if result == 'X':
            return -1, x, y
        elif result == 'O':
            return 1, x, y
        elif result == '.':
            return 0, x, y
        for i in range(2, self.n + 2):
            for j in range(2, self.n + 2):
                if self.current_state[i][j] == '.':
                    if max:
                        self.current_state[i][j] = 'O'
                        self.e2 = self.e2 + 1
                        (v, _, _) = self.alphabeta(alpha, beta, max=False)
                        if v > value:
                            value = v
                            x = i - 2
                            y = self.current_state[0][j]
                    else:
                        self.current_state[i][j] = 'X'
                        self.e1 = self.e1 + 1
                        (v, _, _) = self.alphabeta(alpha, beta, max=True)
                        if v < value:
                            value = v
                            x = i - 2
                            y = self.current_state[0][j]
                    self.current_state[i][j] = '.'
                    if max:
                        if value >= beta:
                            return value, x, y
                        if value > alpha:
                            alpha = value
                    else:
                        if value <= alpha:
                            return value, x, y
                        if value < beta:
                            beta = value
        return value, x, y

    def is_valid(self, px, py):
        if px < 0 or px > self.n or py < 0 or py > self.n:
            return False
        elif self.current_state[px + 2][py + 2] != '.':
            return False
        else:
            return True

    def input_move(self):
        while True:
            print(F'Player {self.player_turn}, enter your move:')
            px = int(input('enter the x coordinate: '))
            py = int(input('enter the y coordinate: '))
            if self.is_valid(px, py):
                return px, py
            else:
                print('The move is not valid! Try again.')

    def play(self):

        if self.a is None:
            self.a = 'True'
        if self.player_1 is None:
            self.player_1 = 'Human'
        if self.player_2 is None:
            self.player_2 = 'Human'
        while True:
            self.draw_board()
            if self.check_end():
                return
            start = time.time()
            if self.a == 'False':
                print('Minimax:')
                if self.player_turn == 'X':
                    (_, x, y) = self.minimax(max=False)
                else:
                    (_, x, y) = self.minimax(max=True)
            else:  # algo == self.ALPHABETA
                print('Alpha-Beta:')
                if self.player_turn == 'X':
                    (m, x, y) = self.alphabeta(max=False)
                else:
                    (m, x, y) = self.alphabeta(max=True)
            end = time.time()
            currTime = 0
            if self.player_turn == 'X' and self.player_1 == 'Human':
                if self.recommend:
                    currTime = round(end - start, 7)
                    print(F'Evaluation time: {currTime}s')
                    self.totalTime = self.totalTime + currTime
                    self.timeInstances = self.timeInstances + 1
                    print(F'Heuristic evaluations: {self.e1}')
                    self.totalE1 = self.totalE1 + self.e1
                    self.e1 = 0
                    self.e2 = 0
                    print(F'Recommended move: x = {x}, y = {y}')
                (x, y) = self.input_move()
            if self.player_turn == 'O' and self.player_2 == 'Human':
                if self.recommend:
                    currTime = round(end - start, 7)
                    print(F'Evaluation time: {currTime}s')
                    self.totalTime = self.totalTime + currTime
                    self.timeInstances = self.timeInstances + 1
                    print(F'Heuristic evaluations: {self.e2}')
                    self.totalE2 = self.totalE2 + self.e2
                    self.e1 = 0
                    self.e2 = 0
                    print(F'Recommended move: x = {x}, y = {y}')
                (x, y) = self.input_move()
            if self.player_turn == 'X' and self.player_1 == 'AI':
                currTime = round(end - start, 7)
                print(F'Evaluation time: {currTime}s')
                self.totalTime = self.totalTime + currTime
                self.timeInstances = self.timeInstances + 1
                print(F'Heuristic evaluations: {self.e1}')
                self.totalE1 = self.totalE1 + self.e1
                self.e1 = 0
                self.e2 = 0
                print(F'Player {self.player_turn} under AI control plays: x = {x}, y = {y}')
                if currTime > self.t:
                    print(F'Player {self.player_turn} took too long to play. The player loses by default')
                    return
            if self.player_turn == 'O' and self.player_2 == 'AI':
                currTime = round(end - start, 7)
                print(F'Evaluation time: {currTime}s')
                self.totalTime = self.totalTime + currTime
                self.timeInstances = self.timeInstances + 1
                self.totalTime = self.totalTime + currTime
                self.timeInstances = self.timeInstances + 1
                print(F'Heuristic evaluations: {self.e2}')
                self.totalE2 = self.totalE2 + self.e2
                self.e1 = 0
                self.e2 = 0
                print(F'Player {self.player_turn} under AI control plays: x = {x}, y = {y}')
                if currTime > self.t:
                    print(F'Player {self.player_turn} took too long to play. The player loses by default')
                    return

            PosY = None
            for i in range(0, len(self.Alphabet)):
                if y == self.Alphabet[i]:
                    PosY = i
            self.current_state[x + 2][PosY + 2] = self.player_turn
            self.switch_player()


def main():
    g = Game(recommend=True)
    print()
    for i in range(1, 11):
        print(F'Match {i}')
        g.play()
        print()

    print(F'n={self.n}, b={self.b}, s={self.s}, t={self.t}')
    print()
    print(F'Player 1: d={self.d1}, a={self.a}')
    print(F'Player 2: d={self.d2}, a={self.a}')
    print()
    print('10 Games')
    print()
    print(F'Total wins for heuristic e1: {self.e1Wins}, ({self.e1Wins/10*100}%)')
    print(F'Total wins for heuristic e2: {self.e2Wins}, ({self.e2Wins/10*100}%)')
    print()
    print(F'i   Average evaluation time: {self.totalTime}')
    print(F'ii  Heuristic evaluation: {self.totalE2+self.totalE1} ')

if __name__ == "__main__":
    main()
