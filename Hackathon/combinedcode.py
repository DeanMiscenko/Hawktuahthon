import pygame, os, time, random
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
info = pygame.display.Info()
#Import End



#Screen Declaration
name = 'Untitled'
print(info)
clock = pygame.time.Clock()
screen_width,screen_height = info.current_w,info.current_h
window_width,window_height = screen_width - 10,screen_height-50
window = pygame.display.set_mode((window_width,window_height), pygame.RESIZABLE)
pygame.display.set_caption(name)
clickimg = pygame.image.load('click me.png')
dvdimg = pygame.image.load('dvdimg.png')
print(clickimg.get_size())

class Button():
    def __init__(self, y, image):
        self.image = image
        self.size = self.image.get_size()
        self.height = y
        self.clicked = False

        
    def draw(self, multiplier, surface, window_width, degree):
        global handled
        if degree == 1:
            self.clicked = False
        self.rect = pygame.Rect((window_width + 10 - (self.size[0] * multiplier)) / 2, self.height, self.size[0] * multiplier, self.size[1] * multiplier)
        pos = pygame.mouse.get_pos()
        counter = 1.05
        if self.rect.collidepoint(pos): # DO NOT CHANGE THIS
            surface.blit(pygame.transform.scale(self.image, (self.size[0] * multiplier * counter, self.size[1] * multiplier * counter)), 
                         ((window_width + 10 - (self.size[0] * multiplier * counter)) / 2, self.height - (self.rect[3] * (counter - 1) / 2)))
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False and not handled:
                self.clicked = True
                handled = pygame.mouse.get_pressed()[0]
                
                print('clicked')
            elif pygame.mouse.get_pressed()[0] == 1 and self.clicked == False and handled:
                pass
            else:
                handled = False
        
        else:
            surface.blit(pygame.transform.scale(self.image, (self.size[0] * multiplier, self.size[1] * multiplier)), 
                         ((window_width + 10 - (self.size[0] * multiplier)) / 2, self.height))
            if pygame.mouse.get_pressed()[0] == 1:
                self.clicked = False

        #print(self.clicked)
        return self.clicked

class Powerup():
    def __init__(self, order, image):
        self.image = image
        self.size = self.image.get_size()
        self.order = order

    def clicking(self, surface, window_width, degree):
        global handle, doubleB, powerdoubleB, autoB, critB, value
        if 0 < self.order < 3:
            pygame.transform.scale(self.image, (50, 50))
            self.rect = pygame.Rect(1300, 400 + 100*abs(self.order % 2 - 1), 50, 50)
            pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(pos):
                surface.blit(pygame.transform.scale(self.image, (52.5, 52.5)), 
                            (1300 - (2.5 / 2), 400 + 100*abs(self.order % 2 - 1) - (2.5/ 2)))
                if pygame.mouse.get_pressed()[0] == 1 and self.image == doubleP:
                    doubleB = True
                    value = 2
                    print('clicked')
                if pygame.mouse.get_pressed()[0] == 1 and self.image == powerDoubleP:
                    powerdoubleB = True
                    print('clicked')

            else:
                surface.blit(pygame.transform.scale(self.image, (50, 50)), 
                            (1300, 400 + 100*abs(self.order % 2 - 1)))

            return True

        if 2 < self.order < 5:
            pygame.transform.scale(self.image, (50, 50))
            self.rect = pygame.Rect(1400, 400 + 100*abs(self.order % 2 - 1), 50, 50)
            pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(pos):
                surface.blit(pygame.transform.scale(self.image, (52.5, 52.5)), 
                            (1400 - (2.5 / 2), 400 + 100*abs(self.order % 2 - 1) - (2.5/ 2)))
                if pygame.mouse.get_pressed()[0] == 1 and self.image == critP:
                    critB = True
                    print('clicked')
                if pygame.mouse.get_pressed()[0] == 1 and self.image == autoP:
                    autoB = True
                    print('clicked')

            else:
                surface.blit(pygame.transform.scale(self.image, (50, 50)), 
                            (1400, 400 + 100*abs(self.order % 2 - 1)))
        else:
            return True
        

    
font = pygame.font.SysFont('arial', 32)

counter = 0
text = font.render(f'Dopamine Points {counter}', True, (0, 0, 0), (255, 255, 255))
doubleP = font.render(f'X2', True, (0, 0, 0), (255, 255, 255))
powerDoubleP = font.render(f'^X2^', True, (0, 0, 0), (255, 255, 255))
critP = font.render(f'CRIT', True, (0, 0, 0), (255, 255, 255))
autoP = font.render(f'AUTO', True, (0, 0, 0), (255, 255, 255))
click = Button(200, clickimg)
dopamine = Button(270, text)

double = Powerup(1, doubleP)
doubleB = False
powerdouble = Powerup(2, powerDoubleP)
powerdoubleB = False
crit = Powerup(3, critP)
critB = False
auto = Powerup(4, autoP)
autoB = False
#dvd = Powerup(random.randint(20, window_width), random.randint(20, window_height), dvdimg)
value = 1
run = True
handled = False
handle = False
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
    List.append(random.randint(1, Screen_width))
RectList = []
for n in List:
    RectList.append(pygame.Rect(0, n, 50, 50))
for n in range(50):
    pass
RectList2 = []
while True:
    dopamine = Button(270, text)
    if click.draw(0.6, window, window_width, 1):
        counter += value
    dopamine.draw(0.6, window, window_width, 2)
    if doubleB == False and counter > 4:
        double.clicking(window, window_width, 1)
    if powerdoubleB == False and counter > 20:
        powerdouble.clicking(window, window_width, 1)
    if critB == False and counter > 100:
        crit.clicking(window, window_width, 1)
    if autoB == False and counter > 50:
        auto.clicking(window, window_width, 1)
    elif autoB == True:
        counter += 1/60
    text = font.render(f'Dopamine Points {int(counter)}', True, (0, 0, 0), (255, 255, 255))
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
        if new2:

            new2 = False
        

    Screen.blit(text, text_rect)
    pygame.draw.rect(Screen, Color, main_button)
    pygame.draw.rect(Screen, color2, powerup1)
    pygame.draw.rect(Screen, color3, powerup2)
    pygame.display.update()
    pygame.time.delay(5)
    Counter_checker = counter
