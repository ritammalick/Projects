import pygame
from pygame.locals import *
pygame.init()

main_screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Colour Changer - Ritam')


# variables
exit_game = False
# colurs
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
PURPLE = (255, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (24, 181, 186)
LIGHTBLUE = (0, 98, 255)
PINK = (255, 0, 174)
BLACK = (0, 0, 0)


background = BLACK


while not exit_game:
    for each in pygame.event.get():
        if each.type == pygame.QUIT:
            exit_game = True 
        if each.type == pygame.KEYDOWN:
            if each.key == pygame.K_r:
                background = RED
            elif each.key == pygame.K_b:
                background = BLUE
            elif each.key == pygame.K_w:
                background = WHITE
            elif each.key == pygame.K_y:
                background = YELLOW
            elif each.key == pygame.K_g:
                background = GREEN
            elif each.key == pygame.K_v:
                background = PURPLE
            elif each.key == pygame.K_l:
                background = LIGHTBLUE
            elif each.key == pygame.K_c:
                background = CYAN
            elif each.key == pygame.K_p:
                background = PINK
        
            elif each.type == pygame.MOUSEBUTTONDOWN:
                print(each)
                background = RED
        
    main_screen.fill(background)
    pygame.display.flip()

            

    

pygame.quit()



