import pygame
import multiprocessing

def run_popup():
    # Initialize Pygame for the pop-up
    pygame.init()
    pop_up_screen = pygame.display.set_mode((300, 200))
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Update and draw pop-up window contents here

        pygame.display.update()

def main_game():
    # Initialize Pygame for the main game
    pygame.init()
    main_screen = pygame.display.set_mode((800, 600))
    running = True
    
    # Create and start the pop-up process
    pop_up_process = multiprocessing.Process(target=run_popup)
    pop_up_process.start()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update and draw main game contents here

        pygame.display.update()

    # Close the pop-up when the main game is closed
    pop_up_process.terminate()

if __name__ == "__main__":
    main_game()