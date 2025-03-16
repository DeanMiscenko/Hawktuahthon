import pygame
import random

pygame.init()

# Constants
Screen_width = 800
Screen_height = 800
button_width = 100
button_height = 50
powerup2 = pygame.Rect(Screen_width / 2 - 50, Screen_height / 2, 30, 30)  # Position of the blue button

# Initialize game state
bouncing_squares = []  # List to store bouncing squares
font = pygame.font.Font(None, 40)
color_powerup2 = (0, 0, 255)  # Color for the blue button

# Pygame setup
Screen = pygame.display.set_mode((Screen_width, Screen_height))
pygame.display.set_caption("Bouncing Rectangles Game")
clock = pygame.time.Clock()

# Function to generate random velocity from the corners (diagonal directions)
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

running = True
while running:
    Screen.fill((0, 0, 0))  # Fill screen with black
    pos = pygame.mouse.get_pos()

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if powerup2.collidepoint(pos):  # If blue button is clicked
                # Create a new bouncing square at powerup2's position with a random velocity
                new_bouncing_square = pygame.Rect(Screen_width / 2 - 50, Screen_height / 2, 30, 30)
                speed_x, speed_y = get_random_velocity()
                bouncing_squares.append({'rect': new_bouncing_square, 'speed_x': speed_x, 'speed_y': speed_y})

    # Draw the blue button (powerup2)
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

    # Update screen
    pygame.display.update()
    clock.tick(60)  # 60 frames per second

pygame.quit()
