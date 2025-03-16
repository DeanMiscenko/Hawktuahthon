

import pygame, os, time, random
import cv2 # type: ignore
import numpy as np #type: ignore
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
info = pygame.display.Info()
video_path = "videoplayback.mp4"
cap = cv2.VideoCapture(video_path)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) / 2
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) / 2
video_path1 = "Roulette Wheel Spinning.mp4"
cap1 = cv2.VideoCapture(video_path1)
width1 = int(cap1.get(cv2.CAP_PROP_FRAME_WIDTH)) / 2
height1 = int(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT)) / 2
button_width = 100
button_height = 50
colorcounter = 0
Circle_color = (255, 255, 255)

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
starimg = pygame.transform.scale(pygame.image.load('shootingstar.png'), (50, 50))
dvdimg = pygame.transform.scale(pygame.image.load('dvdimg.png'), (100, 100))
powerup2 = pygame.Rect(window_width / 2 - 50, window_height / 2, 100, 100)  # Position of the blue button
# Initialize game state
bouncing_squares = []  # List to store bouncing squares
font = pygame.font.Font(None, 40)
color_powerup2 = (0, 0, 255)  # Color for the blue button
print(clickimg.get_size())

def get_random_velocity():
    direction = random.choice(['top_left', 'top_right', 'bottom_left', 'bottom_right'])  # Random corner direction
    speed = random.uniform(2, 5)  # Random speed between 2 and 5

    if direction == 'top_left':
        speed_x = -speed
        speed_y = -speed
    elif direction == 'top_right':
        speed_x = speed
        speed_y = -speed
    elif direction == 'bottom_left':
        speed_x = -speed
        speed_y = speed
    elif direction == 'bottom_right':
        speed_x = speed
        speed_y = speed

    return speed_x, speed_y


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
        self.order = order

    def clicking(self, surface, window_width, degree):
        global handle, doubleB, subwaySurfersB, autoB, critB, value, starB, dvdB
        global one, two, three, four
        if 0 < self.order < 3:
            pygame.transform.scale(self.image, (50, 50))
            self.rect = pygame.Rect(1300, 400 + 100*abs(self.order % 2 - 1), 50, 50)
            pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(pos):
                surface.blit(pygame.transform.scale(self.image, (52.5, 52.5)), 
                            (1300 - (2.5 / 2), 400 + 100*abs(self.order % 2 - 1) - (2.5/ 2)))
                if pygame.mouse.get_pressed()[0] == 1 and self.image == doubleP:
                    doubleB = True
                    one = False
                    value = 2
                    print('clicked')
                elif pygame.mouse.get_pressed()[0] == 1 and self.image == starP:
                    starB = True
                    one = False
                    print('clicked')
                    
                if pygame.mouse.get_pressed()[0] == 1 and self.image == subwaySurfersP:
                    subwaySurfersB = True
                    two = False
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
                    three = False
                    print('clicked')
                elif pygame.mouse.get_pressed()[0] == 1 and self.image == dvdP:
                    dvdB = True
                    three = False
                    print('clicked')
                if pygame.mouse.get_pressed()[0] == 1 and self.image == autoP:
                    autoB = True
                    four = False
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
subwaySurfersP = font.render(f'Subway surfers', True, (0, 0, 0), (255, 255, 255))
critP = font.render(f'CRIT', True, (0, 0, 0), (255, 255, 255))
autoP = font.render(f'AUTO', True, (0, 0, 0), (255, 255, 255))
starP = font.render(f'STAR', True, (0, 0, 0), (255, 255, 255))
dvdP = font.render(f'DVD', True, (0, 0, 0), (255, 255, 255))
colorP = font.render(f'COLOR', True, (0, 0, 0), (255, 255, 255))
click = Button(200, clickimg)
dopamine = Button(270, text)
one = True
two = True
three = True
four = True
new = True

color = Powerup(5, colorP)
colorB = False
double = Powerup(1, doubleP)
doubleB = False
subwaySurfers = Powerup(2, subwaySurfersP)
subwaySurfersB = False
crit = Powerup(3, critP)
critB = False
auto = Powerup(4, autoP)
autoB = False
starB = False
value = 1
run = True
handled = False
handle = False
dvdB = False
things = True
Color_change = False
List = []
for n in range(20):
    List.append(random.randint(1, window_height))
RectList = []
for n in List:
    RectList.append(pygame.Rect(0, n, 50, 50))
print(RectList)

while run:
    pos = pygame.mouse.get_pos()
    dopamine = Button(270, text)
    window.fill(color='white')
    if one == False:
        star = Powerup(1, starP)
        if starB == False and counter > 175:
            star.clicking(window, window_width, 1)
    if two == False:
        pass
    if three == False:
        dvd = Powerup(3, dvdP)
        if dvdB == False and counter > 300:
            dvd.clicking(window, window_width, 1)
    if four == False:
        pass

    if click.draw(0.6, window, window_width, 1):
        if critB == True:
            xy = random.randint(1, 20)
            print(xy)
            if xy == 1:
                counter += 5*value
            else:
                counter += value
        else:
            counter += value
    dopamine.draw(0.6, window, window_width, 2)
    if doubleB == False and counter > 24:
        double.clicking(window, window_width, 1)
    if subwaySurfersB == False and counter > 249:
        subwaySurfers.clicking(window, window_width, 1)
    if critB == False and counter > 150:
        crit.clicking(window, window_width, 1)
    if autoB == False and counter > 99:
        auto.clicking(window, window_width, 1)
    if colorB == False and counter > 499:
        color.clicking(window, window_width, 1)
        Color_change = True
    elif autoB == True:
        counter += 1/60
    if starB == True:
        counter += 1/20
        for i, n in enumerate(range(5)):
            window.blit(starimg, RectList[i])
        if new:
            RectList[5].move_ip(-RectList[i].x, 0)
            new = False
        for i, n in enumerate(RectList):
            n.move_ip(2, 0)
            if n.x > window_width:
                n.move_ip(-window_width, 0)
    if dvdB == True and things == True:
        new_bouncing_square = pygame.Rect(window_width / 2 - 50, window_height / 2, 100, 100)
        speed_x, speed_y = get_random_velocity()
        bouncing_squares.append({'rect': new_bouncing_square, 'speed_x': speed_x, 'speed_y': speed_y})
        window.blit(dvdimg, powerup2)
        things = False
    for bouncing_square in bouncing_squares:
        # Update position of each bouncing square
        bouncing_square['rect'].move_ip(bouncing_square['speed_x'], bouncing_square['speed_y'])
        # Bounce off the walls
        if bouncing_square['rect'].x <= 0 or bouncing_square['rect'].x + bouncing_square['rect'].width >= window_width:
            bouncing_square['speed_x'] *= -1  # Reverse X direction
        if bouncing_square['rect'].y <= 0 or bouncing_square['rect'].y + bouncing_square['rect'].height >= window_height:
            bouncing_square['speed_y'] *= -1  # Reverse Y direction

        # Draw the bouncing square
        window.blit(dvdimg, bouncing_square['rect'])

    if Color_change == True:
        if colorcounter == 0: #THis cahnges the color
            Circle_color = (255, 0, 0)
            colorcounter += 1
            pygame.time.get_ticks()
        elif colorcounter == 1:
            Circle_color = (0, 255, 0)
            colorcounter += 1
            pygame.time.get_ticks()
        elif colorcounter == 2:
            Circle_color = (0, 0, 255)
            colorcounter = 0
            pygame.time.get_ticks()
    pygame.draw.circle(window, Circle_color, (pos), 20 )

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    ret, frame = cap.read()

    if not ret:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        ret, frame = cap.read()
    if counter > 250 and subwaySurfersB == True:
        counter += 1/15
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_surface = pygame.surfarray.make_surface(np.rot90(frame))
        window.blit(pygame.transform.scale(frame_surface, (width, height)), (0, 0))
    ret1, frame1 = cap1.read()
    if not ret1:
        cap1.set(cv2.CAP_PROP_POS_FRAMES, 0)
        ret1, frame1 = cap1.read()
    if counter > 1000:
        counter += 1/15
        frame1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2RGB)
        frame_surface1 = pygame.surfarray.make_surface(np.rot90(frame1))
        window.blit(pygame.transform.scale(frame_surface1, (width1, height1)), (0, window_height - height1))
    
    
    text = font.render(f'Dopamine Points {int(counter)}', True, (0, 0, 0), (255, 255, 255))
    pygame.display.update()
    clock.tick(60)
    
cap.release()
pygame.quit()  
