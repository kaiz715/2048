import pygame
import random
import copy
from board import Board
# from board import Board


WIDTH = 800
HEIGHT = 800
FPS = 30


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2048")
clock = pygame.time.Clock()  # For syncing the FPS
size_100 = pygame.font.SysFont(None, 100)
size_150 = pygame.font.SysFont(None, 150)
size_175 = pygame.font.SysFont(None, 150)
size_200 = pygame.font.SysFont(None, 200)
size_300 = pygame.font.SysFont(None, 300)




# group all the sprites together
all_sprites = pygame.sprite.Group()


# game
board = Board(pygame, screen)


running = True
while running:
    old_board = copy.deepcopy(board)

    
    clock.tick(FPS)  

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                board.move_up()

            if event.key == pygame.K_DOWN:
                board.move_down()

            if event.key == pygame.K_LEFT:
                board.move_left()

            if event.key == pygame.K_RIGHT:
                board.move_right()

    if board != old_board:
        board.generate_new_nums(1)

    
    all_sprites.update()

    
    screen.fill(GREEN)

    all_sprites.draw(screen)
    

    board.display_board()

    board.display_status()
    

    
    pygame.display.flip()

pygame.quit()
