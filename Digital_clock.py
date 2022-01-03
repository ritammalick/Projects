import pygame
import datetime
import time
pygame.init()

window = pygame.display.set_mode((300, 200))
pygame.display.set_caption('DIGITAL CLOCK')
running = True
BLACK = (190,255,190)
green = (0, 255, 10)
blue = (3, 190, 252)
fonts = pygame.font.SysFont(None, 90)

def text_screen(text, color, x, y):
    screen_text = fonts.render(text, True, color)
    window.blit(screen_text, [x,y])

while running:
    for events in pygame.event.get():
        
        if events.type == pygame.QUIT:
            running = False
        
    window.fill(BLACK)
    a = datetime.datetime.now()
    a = str(a)
    b = a[11:19]
    if int(b[0:1]) > 11:
        actual_time = 'AM'
    else:
        actual_time ='PM'
    # print(datetime.datetime.now())
    text_screen(f'{b}', green, 30, 60)
    text_screen(f'{actual_time}', blue, 85, 125)
    pygame.display.update()
    

exit()