import pygame
pygame.init()
import random
import math
counter = 0
Screen_width = 800
Screen_height = 800
points = 0
button_width = 100
button_height = 50
main_button = pygame.Rect(Screen_width/2 - button_width/2, Screen_height/2, button_width, button_height)
Screen = pygame.display.set_mode((Screen_width, Screen_height))
value = 1
Color = (255, 0 , 0)
color3 = (0, 255, 0)
font = pygame.font.Font(None, 40)
text = font.render(f"Dopamine points: {points}", True, (255, 255, 255))
text_rect = text.get_rect(center= (Screen_width/2, Screen_height/2 - 80))
powerup1 = pygame.Rect(Screen_width/2 - 10, Screen_height/2 + 100, 30, 30)
powerup2 = pygame.Rect(Screen_width/2 - 50, Screen_height/2 + 100, 30, 30)
not_on_screen = True
up = 2
color2 = (0, 0, 255)
List = []
new = True
new2 = True
counter2 = 0
for n in range(100):
    List.append(random.randint(1, Screen_height))
RectList = []
for n in List:
    RectList.append(pygame.Rect(0, n, 50, 50))
RectDict2 = {}
for n in range(10):
    RectDict2[frozenset((random.randint(0, 2), random.randint(0, 2)))] =  pygame.Rect(Screen_width/2, Screen_height/2, 20, 20)
speed_x = 1
speed_y = 10
while True:
    text = font.render(f"Dopamine points: {points}", True, (255, 255, 255))
    Screen.fill((0, 0, 0))
    pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if main_button.collidepoint(pos):
                points += 1 * value
            if powerup1.collidepoint(pos):
                new = True
                counter += 1
            if powerup2.collidepoint(pos):
                new2 = True
                counter2 += 1
    if main_button.collidepoint(pos):
        Color = (0, 255, 0)
    else:
        Color = (255, 0, 0)
    if counter > 0:
        for i, n in enumerate(range(counter)):
            pygame.draw.rect(Screen, (144, 144, 144), RectList[i])
        if new:
            RectList[counter].move_ip(-RectList[i].x, 0)
            new = False
        for i, n in enumerate(RectList):
            n.move_ip(1, 0)
            if n.x > Screen_width:
                n.move_ip(-Screen_width, 0)
    if counter2 > 0:
        for n, i in enumerate(range(counter)):
            pygame.draw.rect(Screen, (100, 100, 100), list(RectDict2.values())[i])
        if new2:
            RectList[counter2].x = Screen_width/2
            RectList[counter2].y = Screen_height/2
            new2 = False
        for s, n in RectDict2.items():
            if n.y > Screen_height or n.y < 0:
                speed_y = speed_y * -1
            if n.x > Screen_width or n.x < 0:
                speed_x = speed_x * -1
            n.move_ip(int(next(iter(s))) * speed_x, int(next(iter(s))) * speed_y)
            


    Screen.blit(text, text_rect)
    pygame.draw.rect(Screen, Color, main_button)
    pygame.draw.rect(Screen, color2, powerup1)
    pygame.draw.rect(Screen, color3, powerup2)
    pygame.display.update()
    pygame.time.delay(5)

