import pygame
import time
import random

from pygame import display
from pygame import font

pygame.init()

display_width = 1000
display_height = 700

display_frame = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption("Snake Game by laur-broski")

white = (255,255,255)
red = (255,0,0)
black = (0,0,0)


clock = pygame.time.Clock()
snake_speed = 15
snake_block = 10

font_style = pygame.font.SysFont(None, 40)

def the_snake(snake_block, snake_list):
    for index in snake_list:
        pygame.draw.rect(display_frame, black, [index[0], index[1], snake_block, snake_block])

def lost_game(msg, color):
    message = font_style.render(msg, True, color)
    display_frame.blit(message, [display_width/6, display_height/3])

def game_loop():

    game_over = False
    game_close = False

    x1 = display_width / 2
    y1 = display_height / 2

    snake_block = 10

    x1_modified = 0
    y1_modified = 0

    snake_list = []
    length_of_snake = 1

    foodx = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0

    while game_over != True:
        
        while game_close == True:
            display_frame.fill(white)
            lost_game("You lost, press q to quit or p to play again", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.K_q:
                    game_over = True
                    game_close = False
                if event.key == pygame.K_p:
                    game_loop()
        
        
        for event in pygame.event.get():

            if event.type==pygame.QUIT:
                game_over=True

            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_modified = -snake_block
                    y1_modified = 0
                elif event.key == pygame.K_RIGHT:
                    x1_modified = snake_block
                    y1_modified = 0
                elif event.key == pygame.K_UP:
                    x1_modified = 0
                    y1_modified = -snake_block
                elif event.key == pygame.K_DOWN:
                    x1_modified = 0
                    y1_modified = snake_block

        if x1>=display_width or x1<0 or y1>=display_height or y1<0:
            game_close = True

        x1 += x1_modified
        y1 += y1_modified
        display_frame.fill(white)

        pygame.draw.rect(display_frame, red, [foodx, foody, snake_block, snake_block])
        
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for index in snake_list[:-1]:
            if index == snake_head:
                game_close = True

        the_snake(snake_block, snake_list)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop()
