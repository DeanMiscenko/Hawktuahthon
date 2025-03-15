import pygame, os, time
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
    def __init__(self, x, y, image):
        self.image = image
        self.size = self.image.get_size()
        self.width = x
        self.height = y
        self.clicked = False

    def clicking(self, multiplier, surface, window_width, degree):
        global handle
        if degree == 1:
            self.clicked = False
        if degree == 2:
            return True
        self.rect = pygame.Rect(self.width, self.height, self.size[0] * multiplier, self.size[1] * multiplier)
        pos = pygame.mouse.get_pos()
        counter = 1.05
        if self.rect.collidepoint(pos):
            surface.blit(pygame.transform.scale(self.image, (self.size[0] * multiplier * counter, self.size[1] * multiplier * counter)), 
                         (self.width - (self.rect[2] * (counter - 1) / 2), self.height - (self.rect[3] * (counter - 1)/ 2)))
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False and not handle:
                self.clicked = True
                handle = pygame.mouse.get_pressed()[0]
                
                print('clicked')
            elif pygame.mouse.get_pressed()[0] == 1 and self.clicked == False and handle:
                pass
            else:
                handle = False
        else:
            surface.blit(pygame.transform.scale(self.image, (self.size[0] * multiplier, self.size[1] * multiplier)), 
                         (self.width, self.height))
            if pygame.mouse.get_pressed()[0] == 1:
                self.clicked = False

        #print(self.clicked)
        return self.clicked
    
font = pygame.font.SysFont('arial', 32)

counter = 0
text = font.render(f'Dopamine Points {counter}', True, (0, 0, 0), (255, 255, 255))
click = Button(200, clickimg)
dopamine = Button(270, text)
run = True
handled = False
handle = False

while run:
    dopamine = Button(270, text)
    print(counter)
    
    window.fill(color='white')
    
    if click.draw(0.6, window, window_width, 1):
        counter += 1
    dopamine.draw(0.6, window, window_width, 2)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    text = font.render(f'Dopamine Points {counter}', True, (0, 0, 0), (255, 255, 255))
    pygame.display.update()
    clock.tick(60)
    
    
pygame.quit()  
