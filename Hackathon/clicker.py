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
class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.size = self.image.get_size()
        self.width = x
        self.height = y
        self.clicked = False

    def clicking(self, multiplier, surface, window_width, degree):
        global handled
        if degree == 1:
            self.clicked = False
        self.rect = pygame.Rect(self.width, self.height, self.size[0] * multiplier, self.size[1] * multiplier)
        pos = pygame.mouse.get_pos()
        counter = 1.05
        if self.rect.collidepoint(pos):
            surface.blit(pygame.transform.scale(self.image, (self.size[0] * multiplier * counter, self.size[1] * multiplier * counter)), 
                         (self.width - (self.rect[2] * (counter - 1) / 2), self.height - (self.rect[3] * (counter - 1)/ 2)))
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
                         (self.width, self.height))
            if pygame.mouse.get_pressed()[0] == 1:
                self.clicked = False

        #print(self.clicked)
        return self.clicked
click = Button(500, 200, clickimg)
run = True
handled = False
counter = 0
while run:
    print(counter)
    window.fill(color='white')
    if click.clicking(0.6, window, window_width, 1):
        counter += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    pygame.display.update()
    clock.tick(60)
    
    
pygame.quit()  
