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

while run:
    dopamine = Button(270, text)
    
    window.fill(color='white')
    
    if click.draw(0.6, window, window_width, 1):
        counter += value
    dopamine.draw(0.6, window, window_width, 2)
    if doubleB == False:
        double.clicking(window, window_width, 1)
    if powerdoubleB == False:
        powerdouble.clicking(window, window_width, 1)
    if critB == False:
        crit.clicking(window, window_width, 1)
    if autoB == False:
        auto.clicking(window, window_width, 1)
    else:
        counter += 1/60
    
    
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    text = font.render(f'Dopamine Points {int(counter)}', True, (0, 0, 0), (255, 255, 255))
    pygame.display.update()
    clock.tick(60)
    
    
pygame.quit()  
