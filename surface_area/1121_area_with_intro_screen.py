import pygame
from pygame.locals import *
import math

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRID_COLOR = (226, 135, 67)
FPS = 30
font = pygame.font.Font(None, 36)
font2 = pygame.font.Font(None, 25)

# Grid settings
grid_spacing = 100

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Interactive Surface Area Calculator")

# Background screen
class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
BackGround = Background('1121_background_image.jpg', [0,0])

# List to store the vertices of the user-defined shape
vertices = []

# Function to calculate the surface area in pixel unit
def calculate_area(vertices):
    if len(vertices) <= 2:
        conclusion = "It's not a shape :("
        return conclusion, 0
    elif len(vertices) == 3:
        conclusion = "It's a triangle!"
        # Calculate area of a triangle using Heron's formula
        a = abs(math.dist(vertices[0], vertices[1]))
        b = abs(math.dist(vertices[1], vertices[2]))
        c = abs(math.dist(vertices[2], vertices[0]))
        s = (a + b + c) / 2
        return conclusion, math.sqrt(s * (s - a) * (s - b) * (s - c))
    elif len(vertices) == 4:
        # Handle the case of four vertices (a square/rectangle)
        a = abs(math.dist(vertices[0], vertices[1]))
        b = abs(math.dist(vertices[1], vertices[2]))
        if a == b : conclusion = "It's a square!"
        else : conclusion = "It's a rectangle!"
        return conclusion, a * b
    else:
        conclusion = "It's a polygon!"
        # Calculate area of a convex polygon 
        from shapely.geometry import Polygon
        pgon = Polygon(vertices) # Assuming x,y coordinates
        return conclusion, pgon.area

def blit_text(surface, text, pos, font, color=pygame.Color('black')):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.

# Introduction Scene and "Start" button
intro_text = font.render("Welcome to the Surface Area Calculator!", True, BLACK)
exp_text = "You can use this calculator to draw shapes and calculate their surface area! Just click on the screen to draw vertices and form them into a shape, click Calculate button and you're done! Have fun!"
start_button = pygame.Rect(300, 330, 200, 50)
start_text = font.render("Start", True, WHITE)
button_color = (100, 100, 100)

# Create "Calculate","Clear" and "Return" buttons
calculate_button = pygame.Rect(10, 10, 120, 30)
clear_button = pygame.Rect(140, 10, 80, 30)
return_button = pygame.Rect(10, 547, 90, 30)
button_color = (100, 100, 100)
calculate_text = font.render("Calculate", True, WHITE)
clear_text = font.render("Clear", True, WHITE)
return_text = font.render("Return", True, WHITE)

# Flags for buttons
calculate_clicked = False
drawing = False
selected_vertex = None

# Main game loop
intro_scene = True
drawing_scene = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN:
            x, y = event.pos
            if intro_scene and start_button.collidepoint(x, y):
                intro_scene = False
                drawing_scene = True
                vertices = []  # Clear vertices
                area = 0  # Clear the calculated area
            elif return_button.collidepoint(x, y):
                # Return to the intro scene
                intro_scene = True
                drawing_scene = False
                vertices = []  # Clear vertices
                area = 0  # Clear the calculated area
                calculate_clicked = False  # Re-enable drawing mode
            elif calculate_button.collidepoint(x, y):
                # Calculate the area when the "Calculate" button is clicked
                calculate_clicked = True
                drawing = False  # Disable drawing mode
            elif clear_button.collidepoint(x, y):
                vertices = []  # Clear vertices
                area = 0  # Clear the calculated area
                calculate_clicked = False  # Re-enable drawing mode
            else:
                if not calculate_clicked:
                    vertices.append((x, y))
                    selected_vertex = None
                else:
                    selected_vertex = None
            drawing = not drawing
        elif event.type == MOUSEMOTION:
            if drawing and selected_vertex is not None:
                x, y = event.pos
                vertices[selected_vertex] = (x, y)
        elif event.type == MOUSEBUTTONUP:
            if event.button == 1:
                drawing = False

    # Clear the screen
    screen.fill([255, 255, 255])
    screen.blit(BackGround.image, BackGround.rect)

    if intro_scene:
        # Draw the introduction scene
        intro_rect = intro_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
        screen.blit(intro_text, intro_rect)
        blit_text(screen, exp_text, (30, 270), font2)
        pygame.draw.rect(screen, button_color, start_button)
        start_rect = start_text.get_rect(center=start_button.center)
        screen.blit(start_text, start_rect)

    elif drawing_scene:
        # Draw the grid
        for x in range(0, SCREEN_WIDTH, grid_spacing):
            pygame.draw.line(screen, GRID_COLOR, (x, 0), (x, SCREEN_HEIGHT))
        for y in range(0, SCREEN_HEIGHT, grid_spacing):
            pygame.draw.line(screen, GRID_COLOR, (0, y), (SCREEN_WIDTH, y))

        # Draw the shape
        if len(vertices) > 1:
            pygame.draw.polygon(screen, BLACK, vertices, 1)

        # Draw the "Calculate","Clear" and "Return" buttons
        pygame.draw.rect(screen, button_color, calculate_button)
        screen.blit(calculate_text, (15, 15))
        pygame.draw.rect(screen, button_color, clear_button)
        screen.blit(clear_text, (145, 15))
        pygame.draw.rect(screen, button_color, return_button)
        screen.blit(return_text, (15, 550))

        if calculate_clicked:
            # Divide each coordinate value by 100 and round them off
            rounded_coordinates = [(round(x/100), round(y/100)) for x, y in vertices]
            # Display the calculated area on the screen
            conclusion, area = calculate_area(rounded_coordinates)
            area = round(area)
            font = pygame.font.Font(None, 36)
            text = font.render(f"{conclusion}", True, BLACK)
            text2 = font.render(f"Area: {area}", True, BLACK)
            text3 = font.render(f"Coordinates: {rounded_coordinates}", True, BLACK)
            screen.blit(text, (10, 50))
            screen.blit(text2, (10, 75))
            screen.blit(text3, (10, 100))

        # Draw vertices as small circles
        for vertex in vertices:
            pygame.draw.circle(screen, BLACK, vertex, 5)

    pygame.display.update()

# Quit Pygame
pygame.quit()
