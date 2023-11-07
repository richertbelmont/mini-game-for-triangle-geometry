import pygame
import sys
import subprocess

# Initialize Pygame
pygame.init()
# Load the background image
background_image = pygame.image.load('./background/main_background.jpg')
background_rect = background_image.get_rect()
# Screen dimensions
screen_width, screen_height = background_image.get_size()
screen = pygame.display.set_mode((screen_width/2, screen_height))
pygame.display.set_caption('Geometry Learning Tool(for kids)')



# Button class
class ImageButton:
    def __init__(self, image_path, x, y, python_script):
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.python_script = python_script

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.run_script()

    def run_script(self):
        subprocess.Popen(["python", self.python_script])
#python script path
tangram = './tangram/tangram_main.py'
area = './surface_area/1105_area_live_with_calc_button.py'
trigonometry = './trigonometric/main.py'
#button image path
button_image_1 = './button/button_image1.png'
button_image_2 ='./button/button_image2.png'
button_image_3 = './button/button_image3.png'
# Load images and create image buttons
button1 = ImageButton(button_image_1, 50, screen_height/4-100, tangram)
button2 = ImageButton(button_image_2, 50, screen_height/2-50, area)
button3 = ImageButton(button_image_3, 50, screen_height/4*3, trigonometry)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        else:
            button1.handle_event(event)
            button2.handle_event(event)
            button3.handle_event(event)

    screen.blit(background_image, background_rect)

    button1.draw(screen)
    button2.draw(screen)
    button3.draw(screen)

    pygame.display.flip()

pygame.quit()
sys.exit()