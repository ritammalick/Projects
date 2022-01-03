# # import datetime
# # import tkinter.messagebox as tsmg
# # game = True

# # i = datetime.datetime.now()
# # while game:
# #     i = datetime.datetime.today()
# #     print(i)

# #     if '21:07:00' in str(i):
# #         break
# # tsmg.showinfo("It works")
# #
# # def t():
# #     """
# #     HI
# #     """
# #
# # print(t.__doc__)

# # import pygame
# # pygame.init()

# # # Colors
# # white = (255, 255, 255)
# # red = (255, 0, 0)
# # black = (0, 0, 0)

# # # Creating window
# # screen_width = 900
# # screen_height = 600
# # gameWindow = pygame.display.set_mode((screen_width, screen_height))

# # # Game Title
# # pygame.display.set_caption("SnakesWithHarry")
# # pygame.display.update()

# # # Game specific variables
# # exit_game = False
# # game_over = False
# # snake_x = 45
# # snake_y = 55
# # snake_size = 10

# # clock = pygame.time.Clock()
# # # Game Loop
# # while not exit_game:
# #     for event in pygame.event.get():
# # #         if event.type == pygame.QUIT:
# # #             exit_game = True

# # #     gameWindow.fill(white)
# # #     pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])
# # #     pygame.display.update()


# # # pygame.quit()
# # # quit()


# # from tkinter import *



# # tk = Tk()
# # tk.geometry('380x320')


# # def com():
# #     global c
# #     code = name.get()
# #     c = code
# #     # k()
# # name = Entry(tk, width=45)
# # name.pack()

import pygame
import random

pygame.init()

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

# Creating window
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# Game Title
pygame.display.set_caption("SnakesWithHarry")
pygame.display.update()

# Game specific variables
exit_game = False
game_over = False
snake_x = 45
snake_y = 55
velocity_x = 0
velocity_y = 0

food_x = random.randint(20, screen_width/2)
food_y = random.randint(20, screen_height/2)
score = 0
init_velocity = 5
snake_size = 30
fps = 20

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])


def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])


snk_list = []
snk_length = 1

# Game Loop
while not exit_game:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                velocity_x = init_velocity
                velocity_y = 0

            if event.key == pygame.K_LEFT:
                velocity_x = - init_velocity
                velocity_y = 0

            if event.key == pygame.K_UP:
                velocity_y = - init_velocity
                velocity_x = 0

            if event.key == pygame.K_DOWN:
                velocity_y = init_velocity
                velocity_x = 0

    snake_x = snake_x + velocity_x
    snake_y = snake_y + velocity_y

    if abs(snake_x - food_x)<20 and abs(snake_y - food_y)<15:
        score +=1
        food_x = random.randint(20, screen_width / 2)
        food_y = random.randint(20, screen_height / 2)
        snk_length +=5

    gameWindow.fill(white)
    text_screen("Score: " + str(score * 10), red, 5, 5)
    pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])


    head = []
    head.append(snake_x)
    head.append(snake_y)
    snk_list.append(head)

    if len(snk_list)>snk_length:
        del snk_list[0]

    # pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])
    plot_snake(gameWindow, black, snk_list, snake_size)
    pygame.display.update()
    clock.tick(fps)

pygame.quit()
quit()
# import pygame
# from pygame import mixer


# pygame.mixer.init()
# while True:
#     pygame.mixer.music.load("D:\\My projects\\Vs code\\songg.wav")
#     pygame.mixer.music.play()



  
    