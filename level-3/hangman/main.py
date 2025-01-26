import pygame

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1280, 720
FPS = 60

# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Hangman")
clock = pygame.time.Clock()

#background
background = pygame.image.load("python-nuggets/level-3/hangman/assets/background/homebackground.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

#font
font = pygame.font.Font("python-nuggets/level-3/hangman/assets/font/VPPixel-Simplified.otf", 74)
text = font.render("H A N G M A N", True, (255,255,255))
text_rect = text.get_rect(center = (WIDTH//2,100))

# Main game loop
running = True
while running:
    clock.tick(FPS)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #add background
    screen.blit(background, (0,0))

    #add text
    screen.blit(text, text_rect)

    

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()