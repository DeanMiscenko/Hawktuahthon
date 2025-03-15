import pygame
pygame.init()
import random
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
font = pygame.font.Font(None, 40)
text = font.render(f"Dopamine points: {points}", True, (255, 255, 255))
text_rect = text.get_rect(center= (Screen_width/2, Screen_height/2 - 80))
powerup1 = pygame.Rect(Screen_width/2 - 10, Screen_height/2 + 100, 60, 60)
not_on_screen = True
up = 2
color2 = (0, 0, 255)
List = []
for n in range(25):
    List.append(random.randint(1, Screen_width))
RectList = []
for n in List:
    RectList.append(pygame.Rect(0, n, 50, 50))
    

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
                counter += 1
    if main_button.collidepoint(pos):
        Color = (0, 255, 0)
    else:
        Color = (255, 0, 0)
    if counter > 0:
        for i, n in enumerate(range(counter)):
            pygame.draw.rect(Screen, (144, 144, 144), RectList[i])     
        for i, n in enumerate(RectList):
            n.move_ip(1, 0)
            if n.x > Screen_width:
                n.move_ip(-Screen_width, 0)

    Screen.blit(text, text_rect)
    pygame.draw.rect(Screen, Color, main_button)
    pygame.draw.rect(Screen, color2, powerup1)
    pygame.display.update()
    pygame.time.delay(5)
    Counter_checker = counter
