import random
import math


class Tile:
    def __init__(self):
        self.value = 0

    def __repr__(self):
        return str(self.value)

    def next(self):
        self.value += 1

    def generate_shade(self):
        return (round(self.value/11*255) + 50, round(self.value/11*123) + 50, round(self.value/11*55) + 50)


class Board:
    def __init__(self):
        self.board = [[Tile() for _ in range(4)] for _ in range(4)]
        self.generate_new_nums(2)

    def __eq__(self, other):
        if (isinstance(other, Board)):
            for row in range(4):
                for col in range(4):
                    if self.board[row][col].value != other.board[row][col].value:
                        return False
            return True
        return False

    def generate_new_nums(self, num_to_generate):
        for _ in range(num_to_generate):
            rand_x = random.randint(0, 3)
            rand_y = random.randint(0, 3)
            if self.board[rand_x][rand_y].value == 0:
                self.board[rand_x][rand_y].next()
                if(random.random() > .75):
                    self.board[rand_x][rand_y].next()
            else:
                self.generate_new_nums(1)

    def check_status(self):  # 0 is continue game, 1 is lose game, 2 is win game
        for row in self.board:
            for tile in row:
                if tile.value == 2048:
                    return 2
        for row in self.board:
            for tile in row:
                if tile.value == 0:
                    return 0
        for row in range(4):
            for col in range(4):
                if row != 3 and self.board[row][col].value == self.board[row+1][col].value or col != 3 and self.board[row][col].value == self.board[row][col + 1].value:
                    return 0
        return 1

    def move_up(self):
        self.shift_up()
        for row in range(3):
            for col in range(4):
                if self.board[row][col].value == self.board[row+1][col].value and self.board[row][col].value != 0:
                    self.board[row][col].value += 1
                    self.board[row+1][col].value = 0
        self.shift_up()

    def move_down(self):
        self.shift_down()
        for row in range(3, -1, -1):
            for col in range(4):
                if self.board[row][col].value == self.board[row-1][col].value and self.board[row][col].value != 0:
                    self.board[row][col].value += 1
                    self.board[row-1][col].value = 0
        self.shift_down()

    def move_left(self):
        self.shift_left()
        for row in range(4):
            for col in range(3):
                if self.board[row][col].value == self.board[row][col+1].value and self.board[row][col].value != 0:
                    self.board[row][col].value += 1
                    self.board[row][col+1].value = 0
        self.shift_left()

    def move_right(self):
        self.shift_right()
        for row in range(4):
            for col in range(3, -1, -1):
                if self.board[row][col].value == self.board[row][col-1].value and self.board[row][col].value != 0:
                    self.board[row][col].value += 1
                    self.board[row][col-1].value = 0
        self.shift_right()

    def shift_up(self):
        for col in range(4):
            count = 0
            for row in range(4):
                if self.board[row][col].value != 0:
                    self.board[count][col].value = self.board[row][col].value
                    count += 1

            for i in range(4-count):
                self.board[3-i][col].value = 0

    def shift_down(self):
        for col in range(4):
            count = 3
            for row in range(3, -1, -1):
                if self.board[row][col].value != 0:
                    self.board[count][col].value = self.board[row][col].value
                    count -= 1

            for i in range(count+1):
                self.board[i][col].value = 0

    def shift_left(self):
        for row in range(4):
            count = 0
            for col in range(4):
                if self.board[row][col].value != 0:
                    self.board[row][count].value = self.board[row][col].value
                    count += 1

            for i in range(4-count):
                self.board[row][3-i].value = 0

    def shift_right(self):
        for row in range(4):
            count = 3
            for col in range(3, -1, -1):
                if self.board[row][col].value != 0:
                    self.board[row][count].value = self.board[row][col].value
                    count -= 1

            for i in range(count+1):
                self.board[row][i].value = 0


# for i in range(999):
#     a = Board()

#     a.move_up()


# print(self.board[0])
# print(self.board[1])
# print(self.board[2])
# print(self.board[3])
# print('\n')
