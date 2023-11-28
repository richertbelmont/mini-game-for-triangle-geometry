import pygame
import sys
import multiprocessing
import os

# Function to open a new window for "Tips"
def open_tips_window(pop_up):
    while pop_up:
        pygame.init()
        size = (500, 500)
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Tips")
        
        # Load and set background image
        bg = pygame.image.load('tangram\Picture3.png')
        bg = pygame.transform.scale(bg, size)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pop_up = False

            screen.blit(bg, (0, 0))
            pygame.display.flip()

        pygame.quit()

# Function to run a Python script (replace with your script's file path)
def run_script(script_path):
    os.system(f'python {script_path}')

# Initialize Pygame
pygame.init()
pop_up = False
# Screen setup
background = pygame.image.load('tangram\Picture1.png')
screen_width, screen_height = (800,800)
screen = pygame.display.set_mode((screen_width, screen_height))
background = pygame.transform.scale(background, (screen_width, screen_height))

pygame.display.set_caption("Main Window")

# Button setup
button_font = pygame.font.Font('tangram\Aharoni Bold V3.ttf', 36)
tips_button = pygame.Rect(50, 300, 300, 50)
script1_button = pygame.Rect(50, 400, 300, 50)
script2_button = pygame.Rect(50, 500, 300, 50)
script3_button = pygame.Rect(50, 600, 300, 50)




# Main loop
running = True
while running:
    screen.blit(background, (0, 0))

    # Draw buttons
    pygame.draw.rect(screen, (0, 43, 127), tips_button)
    pygame.draw.rect(screen, (252, 209, 22), script1_button)
    pygame.draw.rect(screen, (206, 17, 38), script2_button)
    pygame.draw.rect(screen, (0, 102, 0), script3_button)

    # Add text to buttons
    screen.blit(button_font.render('Tips', True, (252, 252, 252)), (175, 310))
    screen.blit(button_font.render('Crow Puzzle', True, (252, 252, 252)), (100, 410))
    screen.blit(button_font.render('Rabbit Puzzle', True, (252, 252, 252)), (90, 510))
    screen.blit(button_font.render('Child Puzzle', True, (252, 252, 252)), (100, 610))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if tips_button.collidepoint(event.pos):
                pop_up = True
                multiprocessing.Process(target=open_tips_window(pop_up)).start()
            elif script1_button.collidepoint(event.pos):
                run_script('tangram/tangram_crow.py')
            elif script2_button.collidepoint(event.pos):
                run_script('tangram/tangram_rabbit.py')
            elif script3_button.collidepoint(event.pos):
                run_script('tangram/tangram_Children.py')

    pygame.display.flip()

pygame.quit()
