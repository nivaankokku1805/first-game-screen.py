import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Game Screen with Image")

# Load an image (make sure the file is in the same folder or provide full path)
# Supported formats: PNG, JPG, BMP, GIF
player_image = pygame.image.load("baground.jpg")  # Replace with your image file
player_rect = player_image.get_rect()
player_rect.center = (screen_width // 2, screen_height // 2)

# Background color
background_color = (50, 50, 50)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(background_color)         # Fill background
    screen.blit(player_image, player_rect)  # Draw image

    pygame.display.flip()  # Update display

# Quit Pygame
pygame.quit()
sys.exit()

