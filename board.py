import random
import math
import copy

WIDTH = 800
HEIGHT = 800
FPS = 30


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class Tile:
    num = 0

    def __init__(self):
        self.value = 0
        self.tid = Tile.num
        Tile.num += 1

    def __repr__(self):
        return str(self.value)

    def next(self):
        self.value += 1

    def generate_shade(self):
        return (round(self.value/11*255) + 50, round(self.value/11*123) + 50, round(self.value/11*55) + 50)


class Board:
    def __init__(self, pygame, screen):
        Board.pygame = pygame
        Board.screen = screen

        self.board = [[Tile() for _ in range(4)] for _ in range(4)]
        self.generate_new_nums(2)
        self.old_board = copy.deepcopy(self.board)
        self.animation_frame = 0

        Board.size_100 = pygame.font.SysFont(None, 100)
        Board.size_150 = pygame.font.SysFont(None, 150)
        Board.size_175 = pygame.font.SysFont(None, 150)
        Board.size_200 = pygame.font.SysFont(None, 200)
        Board.size_300 = pygame.font.SysFont(None, 300)

    def __eq__(self, other):
        if (isinstance(other, Board)):
            for row in range(4):
                for col in range(4):
                    if self.board[row][col].value != other.board[row][col].value:
                        return False
            return True
        return False

    def display_board(self):
        for row in range(0, 4):
            for col in range(0, 4):
                if self.board[row][col].value != 0:
                    Board.pygame.draw.rect(Board.screen, self.board[row][col].generate_shade(
                    ), (col*WIDTH/4 + 10, row*HEIGHT/4 + 10, WIDTH/4-20, HEIGHT/4-20))
                    if 2**self.board[row][col].value < 100:
                        text = Board.size_200
                    elif 2**self.board[row][col].value < 1000:
                        text = Board.size_175
                    else:
                        text = Board.size_150
                    text = text.render(
                        str(2**self.board[row][col].value), True, WHITE)

                    Board.screen.blit(text, (col*WIDTH/4 + WIDTH/8 - text.get_rect().width /
                                             2, row*HEIGHT/4 + HEIGHT/8 - text.get_rect().height/2))

    def display_status(self):
        if self.check_status() == 0:
            pass
        elif self.check_status() == 1:
            text = Board.pygame.font.SysFont(
                None, 200).render("You Lose :(", True, WHITE)
            Board.screen.blit(text, (WIDTH / 2 - text.get_rect().width /
                                     2, HEIGHT / 2 - text.get_rect().height/2))
        elif self.check_status() == 2:
            text = Board.pygame.font.SysFont(
                None, 200).render("You Win!!!", True, WHITE)
            Board.screen.blit(text, (WIDTH / 2 - text.get_rect().width /
                                     2, HEIGHT / 2 - text.get_rect().height/2))

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
        self.old_board = copy.deepcopy(self.board)
        self.shift_up()
        for row in range(3):
            for col in range(4):
                if self.board[row][col].value == self.board[row+1][col].value and self.board[row][col].value != 0:
                    self.board[row][col].value += 1
                    self.board[row+1][col].value = 0
        self.shift_up()

    def move_down(self):
        self.old_board = copy.deepcopy(self.board)
        self.shift_down()
        for row in range(3, 0, -1):
            for col in range(4):
                if self.board[row][col].value == self.board[row-1][col].value and self.board[row][col].value != 0:
                    self.board[row][col].value += 1
                    self.board[row-1][col].value = 0
        self.shift_down()

    def move_left(self):
        self.old_board = copy.deepcopy(self.board)
        self.shift_left()
        for row in range(4):
            for col in range(3):
                if self.board[row][col].value == self.board[row][col+1].value and self.board[row][col].value != 0:
                    self.board[row][col].value += 1
                    self.board[row][col+1].value = 0
        self.shift_left()

    def move_right(self):
        self.old_board = copy.deepcopy(self.board)
        self.shift_right()
        for row in range(4):
            for col in range(3, 0, -1):
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

    def animate(self, animation_frame):  # does animation in 15 frames
        for row in range(0, 4):
            for col in range(0, 4):
                if self.board[row][col].value != 0:
                    pygame.draw.rect(screen, self.board[row][col].generate_shade(
                    ), (col*WIDTH/4 + 10, row*HEIGHT/4 + 10, WIDTH/4-20, HEIGHT/4-20))
                    if 2**self.board[row][col].value < 100:
                        text = pygame.font.SysFont(None, 200).render(
                            str(2**self.board[row][col].value), True, WHITE)
                    elif 2**self.board[row][col].value < 1000:
                        text = pygame.font.SysFont(None, 175).render(
                            str(2**self.board[row][col].value), True, WHITE)
                    else:
                        text = pygame.font.SysFont(None, 150).render(
                            str(2**self.board[row][col].value), True, WHITE)
                    screen.blit(text, (col*WIDTH/4 + WIDTH/8 - text.get_rect().width /
                                       2, row*HEIGHT/4 + HEIGHT/8 - text.get_rect().height/2))

# for i in range(999):
#     a = Board()

#     a.move_up()


# print(self.board[0])
# print(self.board[1])
# print(self.board[2])
# print(self.board[3])
# print('\n')
