import pygame
import random

pygame.init()

# Constants
Screen_width = 800
Screen_height = 800
button_width = 100
button_height = 50
main_button = pygame.Rect(Screen_width / 2 - button_width / 2, Screen_height / 2, button_width, button_height)
powerup1 = pygame.Rect(Screen_width / 2 - 10, Screen_height / 2 + 100, 30, 30)
powerup2 = pygame.Rect(Screen_width / 2 - 50, Screen_height / 2 + 100, 30, 30)

# Initialize game state
points = 0
counter = 0
counter2 = 0
color_main_button = (255, 0, 0)
color_powerup1 = (0, 255, 0)
color_powerup2 = (0, 0, 255)
font = pygame.font.Font(None, 40)
text_rect = pygame.Rect(Screen_width / 2 - 100, Screen_height / 2 - 80, 200, 50)
text = font.render(f"Dopamine points: {points}", True, (255, 255, 255))

# Pygame setup
Screen = pygame.display.set_mode((Screen_width, Screen_height))
pygame.display.set_caption("Dopamine Game")
clock = pygame.time.Clock()

# Game objects
RectList = []
speed_x = 1
speed_y = 10

# Create RectList of moving objects
for _ in range(100):
    y_pos = random.randint(1, Screen_height)
    RectList.append(pygame.Rect(0, y_pos, 50, 50))

# List to store new bouncing squares created by powerup2 (blue button)
bouncing_squares = []

running = True
while running:
    Screen.fill((0, 0, 0))
    pos = pygame.mouse.get_pos()

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if main_button.collidepoint(pos):
                points += 1
                text = font.render(f"Dopamine points: {points}", True, (255, 255, 255))
            if powerup1.collidepoint(pos):
                counter += 1
            if powerup2.collidepoint(pos):
                counter2 += 1
                # Create a new bouncing square at powerup2's position
                new_bouncing_square = pygame.Rect(Screen_width / 2 - 50, Screen_height / 2 + 100, 30, 30)
                # Assign a random speed and direction
                bouncing_squares.append({'rect': new_bouncing_square, 'speed_x': random.choice([1, -1]), 'speed_y': random.choice([1, -1])})

    # Change color of main button on hover
    if main_button.collidepoint(pos):
        color_main_button = (0, 255, 0)  # Green when hovered
    else:
        color_main_button = (255, 0, 0)  # Red when not hovered

    # Draw RectList (moving squares)
    for i, rect in enumerate(RectList[:counter]):
        pygame.draw.rect(Screen, (144, 144, 144), rect)
        rect.x += 1
        if rect.x > Screen_width:
            rect.x = -rect.width  # Reset to left side when it moves off-screen

    # Powerup 1 squares (adding more squares)
    if counter > 0:
        pygame.draw.rect(Screen, color_powerup1, powerup1)

    # Powerup 2 squares (creating new bouncing rectangles)
    if counter2 > 0:
        pygame.draw.rect(Screen, color_powerup2, powerup2)

    # Move and display the bouncing squares
    for bouncing_square in bouncing_squares:
        # Update position of each bouncing square
        bouncing_square['rect'].move_ip(bouncing_square['speed_x'], bouncing_square['speed_y'])
        
        # Bounce off the walls
        if bouncing_square['rect'].x <= 0 or bouncing_square['rect'].x + bouncing_square['rect'].width >= Screen_width:
            bouncing_square['speed_x'] *= -1  # Reverse X direction
        if bouncing_square['rect'].y <= 0 or bouncing_square['rect'].y + bouncing_square['rect'].height >= Screen_height:
            bouncing_square['speed_y'] *= -1  # Reverse Y direction

        # Draw the bouncing square
        pygame.draw.rect(Screen, (100, 100, 255), bouncing_square['rect'])

    # Render the points text
    Screen.blit(text, text_rect)

    # Draw buttons
    pygame.draw.rect(Screen, color_main_button, main_button)
    pygame.draw.rect(Screen, color_powerup1, powerup1)
    pygame.draw.rect(Screen, color_powerup2, powerup2)

    # Update screen
    pygame.display.update()
    clock.tick(60)  # 60 frames per second

pygame.quit()
