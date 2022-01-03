import pygame
import random
pygame.init()

def Wall_collison_detector():
    global snake_x
    global snake_y
    global velocity_x
    global velocity_y
    if snake_x < 3 :
        velocity_x = 0
        # velocity_y = 0
        snake_x = 3
    elif snake_y <3 :
        velocity_y = 0
        # velocity_x = 0
        snake_y = 3
    elif  snake_y > 477:
        velocity_y = 0
        # velocity_x = 0
        snake_y = 477
    elif snake_x > 477:
        velocity_x = 0
        # velocity_y = 0
        snake_x = 477
    
    # print(snake_x, snake_y)
    if snake_x == 0:
        velocity_x = 0
        velocity_y = 0
    elif snake_y == 0:
        velocity_y = 0
        velocity_x = 0


# Game Specific Variables
exit_game = False
snake_x = 250
snake_y = 250
size =20
FPS = 65

velocity_x = 0
velocity_y = 0
rnadom_x = 40
rnadom_y = 64
n = 1
# Colours
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

clock = pygame.time.Clock()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Snake Game")

while not exit_game:
    for events in pygame.event.get():
        
        if events.type == pygame.QUIT:
            exit_game = True
        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_LEFT:
                
                velocity_x = -2
                velocity_y = 0
            elif events.key == pygame.K_RIGHT:
                velocity_x = 2
                velocity_y = 0

            elif events.key == pygame.K_DOWN:
                velocity_y = 2
                velocity_x = 0
            elif events.key == pygame.K_UP:
                velocity_y = -2
                velocity_x = 0
            
    Wall_collison_detector()
    snake_x = snake_x+velocity_x
    snake_y = snake_y+velocity_y

    screen.fill(WHITE)

    food_x = rnadom_x
    food_y = rnadom_y
    
    if snake_x>food_x:
        if (snake_x-food_x) < 5 and (snake_y - food_y) < 5:

            rnadom_x = random.randint(20, 480)
            rnadom_y = random.randint(20, 480)
    elif snake_y>food_y:
        if (snake_x-food_x) < 5 and (snake_y - food_y) < 5:

            rnadom_x = random.randint(20, 480)
            rnadom_y = random.randint(20, 480)
            
   


    pygame.draw.rect(screen, GREEN, [snake_x, snake_y, size, size])
    pygame.draw.rect(screen, RED, [food_x, food_y, size, size])
    clock.tick(FPS)
    pygame.display.update()

pygame.quit()
quit()
