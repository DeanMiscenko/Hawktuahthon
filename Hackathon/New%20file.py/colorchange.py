
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

 if powerup3.collidepoint(pos):
                Color_change = True #This stars the code

Circle_color = (255, 255 ,255) #Set this at the start
colorcounter = 0
pygame.draw.circle(Screen, Circle_color, (pos), 20 ) draws circle
        
