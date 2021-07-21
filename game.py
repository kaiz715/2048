import pygame
import random
import copy
from board import Board


WIDTH = 800
HEIGHT = 800
FPS = 30

# Define Colors 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

## initialize pygame and create window
pygame.init()
pygame.mixer.init()  ## For sound
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2048")
clock = pygame.time.Clock()     ## For syncing the FPS
size_100 = pygame.font.SysFont(None, 100)
size_150 = pygame.font.SysFont(None, 150)
size_175 = pygame.font.SysFont(None, 150)
size_200 = pygame.font.SysFont(None, 200)
size_300 = pygame.font.SysFont(None, 300)



## group all the sprites together for ease of update
all_sprites = pygame.sprite.Group()


#game

board = Board()

## Game loop
running = True
while running:
    old_board = copy.deepcopy(board)

    #1 Process input/events
    clock.tick(FPS)     ## will make the loop run at the same speed all the time
    for event in pygame.event.get():        # gets all the events which have occured till now and keeps tab of them.
        ## listening for the the X button at the top
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
    


    #2 Update
    all_sprites.update()


    #3 Draw/render
    screen.fill(GREEN)

    

    all_sprites.draw(screen)
    ########################



    for row in range(0,4):
        for col in range(0,4):
            if board.board[row][col].value != 0:
                if 2**board.board[row][col].value < 100:
                    pygame.draw.rect(screen, board.board[row][col].generate_shade(), (col*WIDTH/4 + 10,row*HEIGHT/4 + 10,WIDTH/4-20,HEIGHT/4-20))
                    text = size_200.render(str(2**board.board[row][col].value), True, WHITE)
                    screen.blit(text, (col*WIDTH/4 +WIDTH/8 - text.get_rect().width/2, row*HEIGHT/4 +HEIGHT/8 - text.get_rect().height/2))
                elif 2**board.board[row][col].value < 1000:
                    pygame.draw.rect(screen, board.board[row][col].generate_shade(), (col*WIDTH/4 + 10,row*HEIGHT/4 + 10,WIDTH/4-20,HEIGHT/4-20))
                    text = size_175.render(str(2**board.board[row][col].value), True, WHITE)
                    screen.blit(text, (col*WIDTH/4 +WIDTH/8 - text.get_rect().width/2, row*HEIGHT/4 +HEIGHT/8 - text.get_rect().height/2))
                else:
                    pygame.draw.rect(screen, board.board[row][col].generate_shade(), (col*WIDTH/4 + 10,row*HEIGHT/4 + 10,WIDTH/4-20,HEIGHT/4-20))
                    text = size_150.render(str(2**board.board[row][col].value), True, WHITE)
                    screen.blit(text, (col*WIDTH/4 +WIDTH/8 - text.get_rect().width/2, row*HEIGHT/4 +HEIGHT/8 - text.get_rect().height/2))
    
    if board.check_status() == 2:
        text = size_200.render("You Win!!!", True, WHITE)
        screen.blit(text, (WIDTH / 2 - text.get_rect().width/2, HEIGHT / 2 - text.get_rect().height/2))
    ########################

    ## Done after drawing everything to the screen
    pygame.display.flip()       

pygame.quit()